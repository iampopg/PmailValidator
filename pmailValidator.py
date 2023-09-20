import requests
from colorama import init, Fore
from yahoo import yahoo
from outlook import outlook
import threading
import concurrent.futures

init(autoreset=True)

red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
blue = Fore.BLUE
yellow = Fore.YELLOW
cyan = Fore.CYAN
background = white + green

print()
print(blue+ '''
      
      Coded by Pop(G)
                    Blackcteam
      ''')
print()

def send_request(email):
    url = "https://app.woodpecker.co/sign-up/create-account"

    headers = {
    "Host": "app.woodpecker.co",
    "Content-Length": "1193",
    "Sec-Ch-Ua": "",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36",
    "Sec-Ch-Ua-Platform": '""',
    "Origin": "https://woodpecker.co",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://woodpecker.co/signup/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "close"
}

    payload = {
        "user": {
            "first_name": "james",
            "company_name": "smith",
            "email": f"{email}",
            "password": "Nopassword",
            "newsletter": False,
            "cookie_id": "eea6d0149334a37aa7a49685bda4440dc444def60a1a05a3f8f163c2ad6f97a2",
            "signup_shard_token": "your_signup_shard_token_here"
        },
        "parameters": {
            "product": "COLD_EMAIL",
            "use_case_profile": "LEAD_GENERATION"
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if "email_invalid" not in response.text:
            with open('valid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(green + f"[{counter}] Valid => {email}")
        else:
            with open('invalid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(red + f"[{counter}] Invalid => {email}")
    except Exception as e:
        print(f"Error for {email}: {e}")

def process_emails(emails):
    # global counter
    with concurrent.futures.ThreadPoolExecutor(max_workers=64) as executor:
        futures = [executor.submit(process_email, email) for email in emails]
        concurrent.futures.wait(futures)


def process_email(email, counter):
    email = email.strip()

    if email.split("@")[1] == 'yahoo.com' or email.split("@")[1] == 'myyahoo.com':
        response = yahoo(email)
        if response == 'valid':
            with open('valid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(green + f"[{counter}] Valid => {email}")
        elif response == 'Yahoo data':
            print(yellow+f"[{counter}] Unable to verify => {email}")
        else:
            with open('invalid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(red + f"[{counter}] Invalid => {email}")

    elif email.split("@")[1] == 'outlook.com' or email.split("@")[1] == 'hotmail.com':
        response = outlook(email)
        if response == 'valid':
            with open('valid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(green + f"[{counter}] Valid => {email}")
        else:
            with open('invalid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(red + f"[{counter}] Invalid => {email}")

    else:
        send_request(email)

def main():
    try:
        global counter
        counter = 1  # Initialize counter
        file_path = input(blue+ "Enter the path to the file containing emails: ")

        with open(file_path, 'r') as file:
            emails = file.readlines()

        for email in emails:
            process_email(email, counter)
            counter += 1  # Increment counter after processing each email

        print(yellow + "Valid emails saved in valid.txt..")
        print(yellow + "Invalid emails saved in invalid.txt..")
    except Exception as e:
        # print(f"Error: {e}")
        pass

if __name__ == "__main__":
    init(autoreset=True)
    main()