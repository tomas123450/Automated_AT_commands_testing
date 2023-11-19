# ssh_connection.py
import paramiko
import time

def establish_ssh_connection(router_ip, ssh_username, ssh_password, timeout=3, **kwargs):
    ssh_client = None

    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(router_ip, username=ssh_username, password=ssh_password, timeout=timeout)
        print("Successfully established an SSH connection.")
        time.sleep(2)
        stdin, stdout, stderr = ssh_client.exec_command('uci get system.system.routername')
        router_validation = stdout.read().decode().strip()
        print(f'You are connected to: {router_validation}.')
        time.sleep(2)
    except paramiko.AuthenticationException as e:
        print(f"SSH Authentication Error: {e}")
        raise SystemError("SSH Authentication Error")
    except paramiko.SSHException as e:
        print(f"SSH Connection Error: {e}")
        raise SystemError("SSH Connection Error")
    except Exception as e:
        print(f"An error occurred while connecting to the router: {e}")
        raise SystemError("Connection Error")

    if ssh_client is None:
        print("Failed to establish an SSH connection. Exiting.")
        raise SystemError("Failed to establish an SSH connection")

    return ssh_client
