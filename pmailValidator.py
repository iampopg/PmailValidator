try:
    import requests
    from colorama import init, Fore
    from yahoo import yahoo
    from outlook import outlook
    import threading, sys, os, time
    from concurrent.futures import ThreadPoolExecutor
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
except ModuleNotFoundError:
    import os, sys
    os.system('pip install requests')
    os.system('pip install colorama')
    print()
    input('ALL requirements has being installed, Please try again')
    sys.exit()

init(autoreset=True)

red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
blue = Fore.BLUE
yellow = Fore.YELLOW
cyan = Fore.CYAN
background = white + green


if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    
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
            with open('result/valid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(green + f"[{counter}] Valid => {email}")
        else:
            with open('result/invalid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(red + f"[{counter}] Invalid => {email}")
    except Exception as e:
        print(f"Error for {email}: {e}")

# def process_emails(emails):
#     # global counter
#     with concurrent.futures.ThreadPoolExecutor(max_workers=64) as executor:
#         futures = [executor.submit(process_email, email) for email in emails]
#         concurrent.futures.wait(futures)


def process_email(email, counter):
    # email = email.strip()
    counter +=1
#yahoo
    if email.split("@")[1] == 'yahoo.com' or email.split("@")[1] == 'myyahoo.com':
        response = yahoo(email)
        if response == 'valid':
            with open('result/valid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(green + f"[{counter}] Valid => {email}")
        elif response == 'Yahoo data':
            print(yellow+f"[{counter}] Unable to verify => {email}")
            with open('result/unknown', 'w') as w:
                w.write(f"{email}\n")
        elif response == 'Limited rate':
            print(yellow+f"[{counter}] Limit Yahoo rate(use proxy/vpn) => {email}")
            with open('result/unknown', 'w') as w:
                w.write(f"{email}\n")
        else:
            with open('result/invalid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(red + f"[{counter}] Invalid => {email}")

#outlook and hotmail
    elif email.split("@")[1] == 'outlook.com' or email.split("@")[1] == 'hotmail.com':
        response = outlook(email)
        if response == 'valid':
            with open('result/valid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(green + f"[{counter}] Valid => {email}")
        elif response == "dead":
            with open('result/dead.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
            print(yellow + f"[{counter}] Dead => {email}")
        else:
            with open('result/invalid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(red + f"[{counter}] Invalid => {email}")

    else:
        send_request(email)
def get_file_path():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = askopenfilename(filetypes=[("Text Files", "*")],title="Select email list file")
    root.destroy()
    return file_path

def main():
    try:
        
        
        
        
        if not os.path.exists('result'):
            os.makedirs('result')
            
        global counter
        counter = 1  # Initialize counter
        print("Choose your email file")
        time.sleep(1)
        file_path = get_file_path()

        with open(file_path, 'r') as file:
            emails = file.readlines()
            counter +=1
        with ThreadPoolExecutor(max_workers=30) as executor:
            executor.map(lambda email: process_email(email.strip(), counter), emails)
            # counter = 1

        # for email in emails:
        #     process_email(email, counter)
        #     counter += 1  # Increment counter after processing each email

        print()
        print(f'{len(emails)} emails checked')
        print(yellow + "Valid emails saved in result/valid.txt..")
        print(yellow + "Invalid emails saved in result/invalid.txt..")
    
    except Exception as e:
        print(f"Error: {e}")
        pass

if __name__ == "__main__":
    init(autoreset=True)
    main()

