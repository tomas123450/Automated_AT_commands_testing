# file_config.py
import json
import csv
import datetime
import platform
import os
from colorama import Fore 

def load_config(name):
    try:
        with open(f'{name}', 'r') as name:
            config = json.load(name)
            if not config:
                print("Failed to load configuration. Exiting.")
            return config
    except Exception as e:
        print(f"An error occurred while loading the configuration: {e}")
        return None
    

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def write_results_to_csv(test_results, config_filename, connection_number, manufacturer, model):
    config = load_config(config_filename)
    if config is None:
        print("Error: Config not loaded.")
        return

    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    # Define the folder path where you want to save the CSV files
    result_folder = "test_results"

    # Create the result folder if it doesn't exist
    os.makedirs(result_folder, exist_ok=True)

    ok_count = 0
    error_count = 0

    try:
        for command in config['connections'][connection_number]["commands"]:
            expected_result = command['expected_result']
            result = test_results.get(command['command'], 'N/A')

            clear_screen()

            print(Fore.CYAN + f"Testing AT command: {command['command']}")
            print(f"Expected: {expected_result}")
            print(f"Result: {result}")
            status = 'OK' if result == expected_result else 'ERROR'
            status_color = Fore.GREEN if status == 'OK' else Fore.RED
            print(status_color + f"Status: {status}")  
            print(Fore.RESET + "-" * 40)

            input("Press Enter to continue...")

            if status == 'OK':
                ok_count += 1
            else:
                error_count += 1

        # Write results to CSV after testing all commands
        filename = os.path.join(result_folder, f"{config['connections'][connection_number]['product_name']}_{current_datetime}.csv")
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Modem manufacturer", "Modem model", "Test Date", "Command tested", "Expected result", "Result", "OK/ERROR"])
            for command in config['connections'][connection_number]["commands"]:
                expected_result = command['expected_result']
                result = test_results.get(command['command'], 'N/A')
                status = 'OK' if result == expected_result else 'ERROR'
                writer.writerow([manufacturer, model, current_datetime, command['command'], expected_result, result, status])

        print(f"Total commands for testing: {len(config['connections'][connection_number]['commands'])}")
        print(f"Results written to {filename}")
        print(Fore.GREEN + f"{ok_count} succeeded" + f", {Fore.RED}{error_count} failed.")

    except Exception as e:
        print(f"An error occurred while writing to the CSV file: {e}")