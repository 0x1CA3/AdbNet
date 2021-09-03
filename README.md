<h1 align="center">
	<img src="https://image.flaticon.com/icons/png/512/160/160138.png" width="150px"><br>
    adb - An exploitation tool for android devices.
</h1>
<p align="center">
	A tool that allows you to search for vulnerable android devices across the world and exploit them.
</p>

<p align="center">
	<a href="https://deno.land" target="_blank">
    	<img src="https://img.shields.io/badge/Version-1.0.0-7DCDE3?style=for-the-badge" alt="Version">
</p>

# Features
```
Features:
  - Post-Exploitation modules to control and tinker with the device you are connected to.
  - Scanners to search for vulnerable android devices across the world to exploit.
  - Options for managing how many devices you have connected.
  - Options for checking whether the devices you are connected to are online or offline.
  - IP-Lookup for retrieving information on a certain IP.
  - Options to dump the IP Addresses of the vulnerable android devices. [This makes your life easier so you dont have to find it yourself]
```

# Getting the required API keys
Create an account on censys.io and then go to your account page and get your free api_id and api_secret key and open 'adbnet.py' and edit in your api id and api key here: 

![image](https://user-images.githubusercontent.com/86132648/124665489-c6588b00-de7a-11eb-984b-b9e3118aba81.png)

Create an account on shodan.io and go to your account to get your free api key, once you have it copied, open 'adbnet.py' and edit in your api key here:
![image](https://user-images.githubusercontent.com/86132648/124665543-d7090100-de7a-11eb-9ef6-e400227a1359.png)

# Simple Tutorial
```
First, run the 'dump shodan' or 'dump censy' (dump shodan is recommended) command to 
dump the IP addresses of the vulnerable devices.

Then, after you find an IP-address you want to try, run the 'connect' command and you will be prompted to enter
the target IP address, once you enter the target ip address, you will be prompter to enter the port. For the port,
you can try entering '5555' or '4444' since those are the most common ports. If you want, you can try finding the
specific port yourself, but it might take some time.

Now AdbNet will now try to connect to the vulnerable android device.
If it fails to connect, try another IP.

If you manage to connect to a device, now you can check if you are really connected by using the 'devices' command.

< Warning! > You can only be connected to one device at a time! To kill the sessions use the 'killall' command! < Warning! >

To open a shell and execute commands on the device, use the 'terminal' command.

To run post-exploitation modules, run the 'post' command for the post-exploitation menu to load. Then, you
can run any module you like.

REMEMBER: IF YOU WANT TO CONNECT TO A DIFFERENT DEVICE, RUN THE 'killall' COMMAND, AND REPEAT THE PROCESS AGAIN.
```

# Installation/How To Run
```
sudo apt install pq
sudo apt install adb
pip3 install colorama
pip3 install requests
python3 adbnet.py or python adbnet.py or py adbnet.py

TIP: For people that are new to this, if you are having issues install a certain python module, just do this: pip3 install <modulename>
```
# Screenshots
![image](https://user-images.githubusercontent.com/86132648/124667060-e2f5c280-de7c-11eb-8f69-2443aa7a7bd3.png)
![image](https://user-images.githubusercontent.com/86132648/124667104-f30da200-de7c-11eb-9da3-098fa211a910.png)

## Credits
```
https://github.com/0x1CA3
```
### Contributions 🎉
###### All contributions are accepted, simply open an Issue / Pull request.
