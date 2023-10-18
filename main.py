import os
import paramiko

global hostname, username, password, first_hostname, last_hostname

hostname = None
username = None
password = None

first_hostname = None
last_hostname = None

def test_ssh_connection(hostname:str, user:str, psswd:str) -> None:
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=user, password=psswd)

        print(f"Connection to {hostname} successful.")
        client.close()

    except Exception as e:
        print(f"Connection to {hostname} failed: {str(e)}")

def test_ssh_connection_range(user:str, psswd:str, first_hostname:str, last_hostname:str) -> None:
    first_hostname_parts = first_hostname.split(".")
    last_hostname_parts = last_hostname.split(".")
    first_ip_base = ".".join(first_hostname_parts[:3]) + "."
    # last_ip_base = ".".join(last_hostname_parts[:3]) + "."
    first_ip_number = first_hostname_parts[-1]
    last_ip_number = last_hostname_parts[-1]

    ip_list = []
    for i in range(int(first_ip_number), int(last_ip_number)+1):
        ip_list.append(f"{first_ip_base}{i}")

    for i in ip_list:
        test_ssh_connection(i, user, psswd)

def first_option() -> None:
    global hostname, username, password, first_hostname, last_hostname
    os.system("cls")
    print("Testing an SSH connection:")
    if hostname != None and username != None and password != None:
        test_ssh_connection(hostname, username, password)
    else:
        hostname_input = str(input("Hostname: "))
        username_input = str(input("Username: "))
        password_input = str(input("Password: "))
    
        test_ssh_connection(hostname_input, username_input, password_input)

def second_option() -> None:
    global hostname, username, password, hostname_range
    os.system("cls")
    print("Testing SSH connections over a range of hostnames:")
    if hostname != None and username != None and password != None and first_hostname != None and last_hostname != None:
        test_ssh_connection_range(username, password, first_hostname, last_hostname)
    else:
        first_hostname_input = str(input("First hostname: "))
        last_hostname_input = str(input("Last hostname: "))
        username_input = str(input("Username: "))
        password_input = str(input("Password: "))
    
        test_ssh_connection_range(username_input, password_input, first_hostname_input, last_hostname_input)


option = input("[1] Test an SSH connectionn\n[2] Test an SSH connection over a hostname range\nChoose an option: ")
if option == "1":
    first_option()
elif option == "2":
    second_option()
else:
    input("Error in selection... Press enter to exit.")
    exit()