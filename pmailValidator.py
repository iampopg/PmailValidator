import requests
from colorama import init, Fore
from yahoo import yahoo
from outlook import outlook
init(autoreset=True)

red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
blue = Fore.BLUE
yellow = Fore.YELLOW
cyan = Fore.CYAN
background = white + green

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
        # text = response.txt
        if "email_invalid" not in response.text:
            with open('valid.txt', 'a') as valid_file:
                valid_file.write(f"{email}\n")
                print(green + f"Valid => {email}")
        else:
            print(red + f"Invalid => {email}")
    except Exception as e:
        print(f"Error for {email}: {e}")

def main():
    try:
        file_path = input(blue+ "Enter the path to the file containing emails: ")

        with open(file_path, 'r') as file:
            emails = file.readlines()

        for email in emails:
            email = email.strip()
            
            #for yahooo mail
            if email.split("@")[1] == 'yahoo.com':
                response = yahoo(email)
                # print(response)
                if response == 'valid':
                    with open('valid.txt', 'a') as valid_file:
                        valid_file.write(f"{email}\n")
                        print(green + f"Valid => {email}")
                else:
                    print(red + f"Invalid => {email}")
                    
            #for outlook
            elif email.split("@")[1] == 'outlook.com':
                response = outlook(email)
                # print(response)
                # print(response)
                if response == 'valid':
                    with open('valid.txt', 'a') as valid_file:
                        valid_file.write(f"{email}\n")
                        print(green + f"Valid => {email}")
                else:
                    print(red + f"Invalid => {email}")
            
            
            #for other email
            else:
                send_request(email)

        print(yellow + "Valid once saved in valid email.txt..")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
