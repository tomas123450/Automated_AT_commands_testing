# arg_parser.py
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="AT Command Execution and CSV Output")
    parser.add_argument("--config", type=str, default="combined_config.json",
                         help="Combined configuration file of products to test, default is set to combined_config.json.")
    parser.add_argument("--connection-identifier", type=int, default=0,
                         help="Connection numbber identifier in config file, default is set to 0.")
    parser.add_argument("--connection-type", type=str, default="SSH",
                         help="Define connection type SSH for (rutx and rut9) SERIAL for (trm2).")
    parser.add_argument("--baud-rate", type=int, default=115200,
                         help="Serial port baud rate, default is set to 115200.")
    parser.add_argument("--serial-port", type=str, default="/dev/ttyUSB2",
                         help="Serial port, default is set to /dev/ttyUSB2.")
    parser.add_argument("--ssh-username", type=str, default="root",
                         help="SSH username, default is set to root.")
    parser.add_argument("--ssh-password", type=str, default="Admin123",
                         help="SSH password, default is set to Admin123")
    parser.add_argument("--ip", type=str, default="192.168.1.1",
                         help="IP address of a product that you want to test, default is 192.168.1.1")
    return parser.parse_args()