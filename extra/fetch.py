import requests
import os

shodankey = "" # add your key here

ip_req = requests.get(f"https://api.shodan.io/shodan/host/search?key={shodankey}&query=android+debug+bridge").text
print(ip_req)
