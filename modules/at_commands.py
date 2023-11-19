# at_commands.py
import file_config
import time

def get_at_command_ssh(ssh_client, connection_number, config, **kwargs):
    test_results = {}
    config = file_config.load_config(config)

    try:
        connection = config["connections"][connection_number]
        config = connection.get("commands", [])

        for command_entry in config:
            command = command_entry.get("command")
            stdin, stdout, stderr = ssh_client.exec_command(f'gsmctl -A {command}')
            result = stdout.read().decode().strip()
            test_results[command] = result

    except Exception as e:
        return str(e)

    print(f"Model being tested: {connection['product_name']}.")
    time.sleep(2)
    return test_results

def get_modem_info_ssh(ssh_client, **kwargs):
    stdin, stdout, stderr = ssh_client.exec_command('gsmctl -A AT+CGMI')
    modem_manufacturer = stdout.read().decode().strip()
    stdin, stdout, stderr = ssh_client.exec_command('gsmctl -A AT+CGMM')
    model_information = stdout.read().decode().strip()
    return modem_manufacturer, model_information



def get_modem_info_serial(ser, **kwargs):
    try:
        ser.write(b'ATI\r\n')
        response = ser.read_until(b'OK\r\n').decode().strip()

        lines = response.split('\r\n')
        manufacturer = lines[0].strip()
        model = lines[1].strip()

        return manufacturer, model
    except Exception as e:
        return str(e)
    
def get_at_command_serial(ser, connection_number, config, **kwargs):
    test_results = {}
    config = file_config.load_config(config)

    try:
        connection = config["connections"][connection_number]
        config = connection.get("commands", [])
        for command_entry in config:
            command = command_entry.get("command")
            ser.write(command.encode() + b'\r\n')
            response = ser.read_until(b'OK\r\n').decode().strip()
            test_results[command] = response

    except Exception as e:
        return str(e)

    print(f"Model being tested: {connection['product_name']}.")
    time.sleep(2)
    return test_results
