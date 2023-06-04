import re
import dns.resolver
import socket
# from check_existing_email import verify_email
# from validate_email_address import validate_email

# Color codes
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'

# Define the 'POPG' ASCII art
popg_art = CYAN + f"""
  PPPP      OOO      PPPP      GGGGG  
 PP  PP   OO  OO   PP  PP   GG   GG 
PP    PP OO    OO PP    PP GG        
PP    PP OO    OO PP    PP GG   GGGG 
PPPPPPP  OO    OO PPPPPPP   GG    GG 
PP       OO    OO PP        GG    GG 
PP        OO  OO  PP         GG   GG 
PP          OOO    PP           GGGG  
                {GREEN}---------------------
                |{RED}PmailValidator v1.0 {GREEN}|
                {GREEN}---------------------
""" + RESET

# Print the 'POPG' ASCII art with color
print(popg_art)

print()
print()


def validate_email(email):
    # Check if the email address is properly formatted
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False

    # Extract the domain from the email address
    domain = email.split("@")[1]

    try:
        # Check if the domain has valid MX records
        dns.resolver.resolve(domain, 'MX')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        return False

    # Check if the domain has a reachable mail exchanger
    try:
        reachable = socket.getaddrinfo(domain, 25)
        # print(reachable)
    except socket.gaierror:
        return False

    return True

# Prompt the user for the file path
file_path = input(f"{BLUE}[+] Enter the file path: ")

try:
    with open(file_path, "r") as file:
        email_addresses = file.readlines()
except FileNotFoundError:
    print(f"{RED}[+] File not found!")
    exit()
except PermissionError:
    print(f"{RED}Permission denied to access the file!")
    exit()
except Exception as e:
    print(f"{RED}An error occurred while opening the file:", str(e))
    exit()

# Remove leading/trailing spaces from email addresses
email_addresses = [email.strip() for email in email_addresses]

valid_email_addresses = []

for email_address in email_addresses:
    if validate_email(email_address):
        valid_email_addresses.append(email_address)

output_file_path = "valid_emails.txt"

try:
    with open(output_file_path, "w") as output_file:
        for email_address in valid_email_addresses:
            output_file.write(f"{email_address}\n")
except PermissionError:
    print("Permission denied to write to the file!")
    exit()
except Exception as e:
    print("An error occurred while writing to the file:", str(e))
    exit()
print()
print(f"{GREEN}[+] Validation completed. Valid email addresses have been written to valid_emails.txt.")
