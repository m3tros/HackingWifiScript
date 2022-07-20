<p align="center"> 
  <img src="https://user-images.githubusercontent.com/107058068/177764686-699cf3a2-bd2a-468a-92b5-9bf447237762.png" alt="HackingWifiScript" width="80" height="80">
</p>
<h1 align="center">HackingWifiScript</h1>

This script written in python3 was created for simplified brute force scanning using the aircrack-ng utility.<br><br>
__You can look at the repository where everything is described in detail. <a href="https://github.com/John-MetrosSoftware/HackingWifi">Link</a>.__
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

## Compilation
I usually compile my projects using the <a href="https://pypi.org/project/pyinstaller/">pyinstaller</a> compiler with the following parameters:
```
pyinstaller -F HackingWifiScript.py
pyinstaller -F Deauth.py
```
