# serial_connection.py
import serial
import time
import subprocess

def establish_serial_connection(serial_port, baud_rate, **kwargs):
    stop_modem_manager()

    try:
        ser = serial.Serial(serial_port, baud_rate)
        time.sleep(2)
        print("Serial connection successful.")
        time.sleep(2)
        return ser
    except serial.SerialException as e:
        print(f"An error occurred while opening the serial port: {e}. Make sure you turned off ModemManager and provided correct port")
        raise SystemExit()

def stop_modem_manager():
    stop_modem_manager_command = "sudo service ModemManager stop"

    try:
        subprocess.run(stop_modem_manager_command, shell=True, check=True)
        print("ModemManager service stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping ModemManager service: {e}")
        

