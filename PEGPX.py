import requests
import threading
import time
import os
import json
from colorama import Fore, Style, init
init(autoreset=True)

WEBHOOKS_FILE = "webhooks.json"

# ──────────────────────────────
# 🔧 Utility Functions
# ──────────────────────────────

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear()
    print(Fore.CYAN + Style.BRIGHT + """
██████╗ ███████╗ ██████╗ ██████╗ ██╗  ██╗
██╔══██╗██╔════╝██╔════╝ ██╔══██╗██║ ██╔╝
██████╔╝█████╗  ██║  ███╗██████╔╝█████╔╝ 
██╔═══╝ ██╔══╝  ██║   ██║██╔═══╝ ██╔═██╗ 
██║     ███████╗╚██████╔╝██║     ██║  ██╗
╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝
    """)
    print(Fore.MAGENTA + "       made by b4for3 on dc \n" + Style.RESET_ALL)


# ──────────────────────────────
# 📁 Webhook Management
# ──────────────────────────────

def load_webhooks():
    if not os.path.exists(WEBHOOKS_FILE):
        return {}
    with open(WEBHOOKS_FILE, 'r') as f:
        return json.load(f)

def save_webhooks(webhooks):
    with open(WEBHOOKS_FILE, 'w') as f:
        json.dump(webhooks, f, indent=4)

def select_webhook():
    webhooks = load_webhooks()
    if not webhooks:
        print(Fore.YELLOW + "No saved webhooks.")
        return input("Enter Webhook URL: ").strip()
    print("Saved Webhooks:")
    for i, key in enumerate(webhooks):
        print(f"[{i+1}] {key}")
    print(f"[{len(webhooks)+1}] Enter manually")
    choice = input("Select option: ")
    try:
        idx = int(choice) - 1
        if idx == len(webhooks):
            return input("Enter Webhook URL: ").strip()
        return list(webhooks.values())[idx]
    except:
        print(Fore.RED + "Invalid selection.")
        return select_webhook()

def save_new_webhook():
    name = input("Save this webhook as (name): ")
    url = input("Enter Webhook URL: ")
    webhooks = load_webhooks()
    webhooks[name] = url
    save_webhooks(webhooks)
    print(Fore.GREEN + f"Saved webhook as '{name}'.")


# ──────────────────────────────
# ✅ Core Functions
# ──────────────────────────────

def validate_webhook(url):
    r = requests.get(url)
    return r.status_code == 200

def get_webhook_info(url):
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        print(f"\nName: {data['name']}")
        print(f"Channel ID: {data['channel_id']}")
        print(f"Guild ID: {data['guild_id']}")
    else:
        print(Fore.RED + "Invalid webhook.")

def change_webhook_name(url):
    name = input("New webhook name: ")
    r = requests.patch(url, json={"name": name})
    if r.status_code == 200:
        print(Fore.GREEN + f"Webhook name changed to '{name}'")
    else:
        print(Fore.RED + "Failed to change name.")

def spam_webhook(url):
    msg = input("Message to spam: ")
    count = int(input("How many times: "))
    delay = float(input("Delay between messages (seconds): "))

    def spam():
        for i in range(count):
            r = requests.post(url, json={"content": msg})
            if r.status_code == 204:
                print(Fore.GREEN + f"[{i+1}/{count}] Sent")
            else:
                print(Fore.RED + f"[{i+1}] Failed")
            time.sleep(delay)

    threading.Thread(target=spam).start()

def send_embed(url):
    title = input("Embed Title: ")
    description = input("Embed Description: ")
    color = int(input("Color (decimal): "))
    embed = {
        "embeds": [{
            "title": title,
            "description": description,
            "color": color
        }]
    }
    r = requests.post(url, json=embed)
    if r.status_code in (200, 204):
        print(Fore.GREEN + "Embed sent.")
    else:
        print(Fore.RED + "Failed to send embed.")

def send_file(url):
    path = input("File path: ")
    try:
        with open(path, 'rb') as f:
            file = {'file': f}
            r = requests.post(url, files=file)
        if r.status_code == 200:
            print(Fore.GREEN + "File sent.")
        else:
            print(Fore.RED + "Failed to send.")
    except:
        print(Fore.RED + "File not found.")

def delete_webhook(url):
    confirm = input(Fore.YELLOW + "Are you sure you want to delete this webhook? (y/n): ")
    if confirm.lower() == 'y':
        r = requests.delete(url)
        if r.status_code == 204:
            print(Fore.RED + "Webhook deleted.")
        else:
            print(Fore.RED + "Failed to delete webhook.")

def mass_spam(url):
    msg = input("Message: ")
    threads = int(input("Threads: "))
    count = int(input("Messages per thread: "))

    def spam():
        for _ in range(count):
            requests.post(url, json={"content": msg})

    for _ in range(threads):
        threading.Thread(target=spam).start()

def clone_webhook():
    src = input("Source Webhook URL: ")
    dest = input("Target Webhook URL: ")
    try:
        info = requests.get(src).json()
        payload = {
            "name": info['name'],
            "avatar": info['avatar']
        }
        r = requests.patch(dest, json=payload)
        if r.status_code == 200:
            print(Fore.GREEN + "Webhook cloned.")
        else:
            print(Fore.RED + "Failed to clone webhook.")
    except:
        print(Fore.RED + "Invalid source/target webhook.")

# ──────────────────────────────
# 🚀 Main Program
# ──────────────────────────────

def main():
    print_banner()
    webhook = select_webhook()

    if not validate_webhook(webhook):
        print(Fore.RED + "Invalid webhook URL.")
        return

    while True:
        print_banner()
        print(Fore.YELLOW + f"Current Webhook: {webhook}\n")
        print(Fore.CYAN + """
[1] Change Webhook Name
[2] Spam Webhook
[3] Delete Webhook
[4] Send Embed
[5] Send File
[6] View Webhook Info
[7] Mass Spam (Threaded)
[8] Clone Webhook to Another
[9] Save This Webhook
[10] Exit
""")
        choice = input(Fore.GREEN + "Choose option: ")

        if choice == "1":
            change_webhook_name(webhook)
        elif choice == "2":
            spam_webhook(webhook)
        elif choice == "3":
            delete_webhook(webhook)
        elif choice == "4":
            send_embed(webhook)
        elif choice == "5":
            send_file(webhook)
        elif choice == "6":
            get_webhook_info(webhook)
        elif choice == "7":
            mass_spam(webhook)
        elif choice == "8":
            clone_webhook()
        elif choice == "9":
            save_new_webhook()
        elif choice == "10":
            print(Fore.CYAN + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option.")

        input(Fore.MAGENTA + "\nPress Enter to continue...")

if __name__ == "__main__":
    main()
