import requests
import os

shodankey = "iiBjHE3TYIgavIGTrl6YIxJ0c6fiRQKz" # add your key here

ip_req = requests.get(f"https://api.shodan.io/shodan/host/search?key={shodankey}&query=android+debug+bridge").text
print(ip_req)