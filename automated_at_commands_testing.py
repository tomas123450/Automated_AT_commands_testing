# automated_at_commands_testing.py
import importlib
import sys, os
from modules.dynamic_import import dynamic_import

def add_modules_directory_to_sys_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = os.path.join(script_dir, "modules")
    sys.path.append(script_dir)


def main():

    add_modules_directory_to_sys_path()

    # Importing arguments from command line
    command_line_args = importlib.import_module('arg_parser').parse_arguments()
    
    # Establishing ssh or serial connection
    connection = dynamic_import(f"{command_line_args.connection_type.lower()}_connection", 
                                f"establish_{command_line_args.connection_type.lower()}_connection", 
                                serial_port=command_line_args.serial_port, baud_rate=command_line_args.baud_rate, 
                                router_ip=command_line_args.ip, ssh_username=command_line_args.ssh_username, 
                                ssh_password=command_line_args.ssh_password) 

    # Receiving AT commands test results
    test_results = dynamic_import("at_commands", f"get_at_command_{command_line_args.connection_type.lower()}",
                                   ssh_client = connection, ser = connection, config = command_line_args.config, 
                                   connection_number = command_line_args.connection_identifier)

    # Receiving modem manufacturer and model
    manufacturer, model = dynamic_import("at_commands", f"get_modem_info_{command_line_args.connection_type.lower()}",
                                          ssh_client = connection, ser = connection)
    
    # Writing test results to csv file
    dynamic_import('file_config', 'write_results_to_csv', test_results = test_results,
                    config_filename = command_line_args.config, connection_number = command_line_args.connection_identifier, 
                    manufacturer = manufacturer, model = model)
    
    # Closing ssh or serial connection
    connection.close()
    
if __name__ == "__main__":
    main()
