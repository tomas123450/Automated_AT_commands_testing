# Automated AT Commands Testing

## Overview

This Python script automates the testing of AT commands on different product series, including RUTXxx, TRM2xx, and RUT9xx. It allows for testing AT commands over SSH or serial connections and generates a detailed CSV report.

## Python Library Dependencies

The script depends on the following Python libraries:

- `json`: For loading and parsing JSON configuration files.
- `csv`: For working with CSV files.
- `datetime`: For generating timestamps.
- `colorama`: For colored terminal output.
- `paramiko`: For SSH connections.
- `serial`: For working with serial connections.

To install these libraries, you can use `pip`:

```bash
pip install json csv datetime colorama paramiko pyserial
```
## Configuration Files
### Configuration File Structure
The script relies on JSON configuration file.This JSON file contains the configuration for the devices and the AT commands to be tested. Default name is set to combined_config.json. Here's an example structure:

product_name: The name of the product series ("rutx" "rut9", "trm2").
connection_type: The type of connection to use ("SSH" or "SERIES").
commands: A list of AT commands to test, each with its expected result.
Here is an example configuration file structure:

```json
{
    "connections": [
        {
            "product_name": "rut9",
            "connection_type": "SSH",
            "commands": [
                {
                    "command": "AT+GMI",
                    "expected_result": "Quectel"
                },
                {
                    "command": "ATI",
                    "expected_result": "Quectel\r\nEC25\r\nRevision: EC25EUGAR06A07M4G"
                }
                // Add more commands
            ]
        },
        {
            "product_name": "rutx",
            "connection_type": "SSH",
            "commands": [
                {
                    "command": "AT+GMI",
                    "expected_result": "Quectel"
                },
                {
                    "command": "ATI",
                    "expected_result": "Quectel\r\nEG06\r\nRevision: EG06ELAR04A04M4G"
                },
                // Add more commands

    
            ]
        },
        {
            "product_name": "trm2",
            "connection_type": "SERIAL",
            "commands": [
                {
                    "command": "AT+GMI",
                    "expected_result": "Quectel\r\n\r\nOK"
                },
                {
                    "command": "ATI",
                    "expected_result": "Quectel\r\nEC21\r\nRevision: EC21ECGAR06A04M1G\r\n\r\nOK"
                },
                // Add more commands

            ]
        }
    ]
}

```

## Usage
Clone the script from the Git repository or download it.

Install the required Python libraries (see "Python Library Dependencies" section).

Create a JSON configuration file for products u want to test.

Run the script with the appropriate command line arguments:

```bash
python3 automated_at_commands_testing.py --config [CONFIG_FILE] --connection-type [CONNECTION_TYPE] --connection-identifier [CONNECTION-ID] --baud-rate [BAUD_RATE] --serial-port [SERIAL_PORT] --ssh-username [SSH_USERNAME] --ssh-password [SSH_PASSWORD] --ip [IP_ADDRESS]
```
Here's what each of the arguments means:

- --config: Specify the configuration file (default is combined_config.json).
- --connection-identifier: Set the connection number identifier in the config file (default is 0). You can change this value to select a specific connection configuration from your configuration file.
- --connection-type: Define the connection type. You can choose "SSH" for (rutx and rut9) or "SERIAL" for (trm2). The default is "SSH."
- --baud-rate: Set the serial port baud rate (default is 115200).
- --serial-port: Specify the serial port (e.g., /dev/ttyUSB2). The default is /dev/ttyUSB2.
- --ssh-username: Provide the SSH username (default is "root").
- --ssh-password: Provide the SSH password (default is "Admin123").
- --ip: Set the IP address of the product you want to test (default is "192.168.1.1").


Example with values:
```bash
python automated_at_commands_testing.py --config custom_config.json --connection-identifier 1 --connection-type SERIAL --baud-rate 9600 --serial-port /dev/ttyUSB2 --ssh-username user123 --ssh-password secret123 --ip 192.168.1.100
```

The script will execute the tests, generate a detailed CSV report, and display the test progress in the terminal.

### Additional Functions
<font size="4"><strong>`execute_at_command_ssh`</strong></font>

This function is used to execute AT commands over an SSH connection. It reads the configuration, runs each command, and records the results in a dictionary. The results are associated with the AT commands and stored for further processing.

<font size="4"><strong>`get_modem_info_ssh`</strong></font>

This function retrieves modem information over an SSH connection. It sends specific AT commands to retrieve the modem manufacturer and model information, which is useful for identifying the connected modem device.

<font size="4"><strong>`router_validation_ssh`</strong></font>

This function validates the connection to the router by retrieving the router name from the system configuration. It ensures that the SSH connection is established successfully and provides information about the connected

<font size="4"><strong>`serial_connection`</strong></font>

This function sets up a serial connection, primarily used for the "SERIAL" connection type. It opens a serial connection to the specified serial port with the given baud rate and prepares the connection for AT command execution.

<font size="4"><strong>`execute_at_command_serial`</strong></font>

This function is used for executing AT commands over a serial connection. It reads the configuration, runs each command, and records the results in a dictionary. The results are associated with the AT commands and stored for further analysis.

<font size="4"><strong>`get_modem_info_serial`</strong></font>

This function extracts modem information from the response after executing the "ATI" command over a serial connection. It parses the response to retrieve the modem manufacturer and model information, which is essential for modem identification.

## CSV Reporting
The script generates a CSV report for each test, naming it with the product name and the current date and time. The CSV report includes the following columns:
- Modem manufacturer
- Modem model
- Test Date
- Command tested
- Expected result
- Result
- OK/ERROR status

Example:

![CSV file](https://ibb.co/f2KdZYD)

For successful commands, the output is colored in green, and for failed commands, it is colored in red.

The script prints information about the testing progress in the terminal, including the product being tested, the current command, and the counts of successful and failed commands.

Example:

![Terminal](https://ibb.co/pdStr55)

## Notes
The script supports running tests for multiple products simultaneously.

For advanced customization and further details, please refer to the script's source code and comments.

## Documentation
This documentation is provided in Markdown format. The source code, along with this documentation, is hosted on gitlab.

For additional information, troubleshooting, and updates, please refer to the repository hosting this code.