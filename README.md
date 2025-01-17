### :warning:Disclaimer : This software is meant for educational purposes only. I'm not responsible for any malicious use of the app.

# :robot: Teardroid v4

![Screenshot](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/IMG-20220122-WA0000_RdKN5Rv3U.jpg)

🇮🇳 It's easy to use android botnet work without port forwarding, vps and android studio

[![GitHub issues](https://img.shields.io/github/issues/ScRiPt1337/Teardroid-phprat)](https://github.com/ScRiPt1337/Teardroid-phprat/issues)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Fhacksec42)](https://twitter.com/intent/tweet?text=Wow:&url=https://github.com/ScRiPt1337/Teardroid-phprat/)
[![Hacksec](https://img.shields.io/badge/Teardroid-4.0-red)](https://github.com/ScRiPt1337/Teardroid-phprat/)

### :rocket: Features

- Retrieve Contact
- Retrieve SMS
- Retrieve running Services
- Retrieve Device Location (:worried: Only work when the app is open on newer devices)
- Retrieve Call Logs
- Run Shell Command ( use findphno command in run shell command to get device phone number and use findx:pdf to find all the pdf files on the device )
- Change Wallpaper
- Send SMS
- Make Call
- Get Installed Apps
- Download File
- Read Notification
- Auto-Start
- Add webview in homepage
- Ignore Battery Optimisation
- Get device admin permission

![Homepage](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/fakescreen.gif)

### :warning: Requirement

- Python3
- Java
- Linux or Windows os (we don't support termux use gcloud)
- For android mobile users use github Codespaces

### Java version i used

```bash
$ java -version
openjdk version "11.0.13" 2021-10-19
OpenJDK Runtime Environment (build 11.0.13+8)
OpenJDK 64-Bit Server VM (build 11.0.13+8, mixed mode)
```

### Tested on

- Windows 11
- Windows 10
- Manjaro
- Kali linux
- Ubuntu

### Deploy the Teardroid control panel ( automatically ) ( recommend )

- Set up an account at [deta.sh](https://web.deta.sh/)
- Login into your account and go to settings ( [settings ](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/deta_dash.png) | [create access token ](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/token2.png) )
- click on create access token and copy the access token
- run python3 setup.py
- it will ask you for the access token paste the access token.
- ![TaskManager](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/20507b2c-0668-4b21-913b-aeab369f0229.gif)
- Done and here is your control panel url.
- ![TaskManager](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/control_url.png)

### Deploy the Teardroid control panel ( Manually )

- Set up an account at [deta.sh](https://web.deta.sh/)
- Install [Deta Cli](https://docs.deta.sh/docs/cli/install)
- Logging in to Deta via the CLI
- Create a new Python Micro using the command below

```bash
$ deta new --python teardroid_control # its will create an teardroid_control folder
```

- Clone [Teardroidv4_api](https://github.com/ScRiPt1337/Teardroidv4_api) repo using the command below

```bash
$ git clone https://github.com/ScRiPt1337/Teardroidv4_api
```

- Move all Teardroidv4_api Files to teardroid_control folder using the command below

```bash
$ cd Teardroidv4_api
$ cp -r * ../teardroid_control/
```

- Go back to the deta repo folder using the command below

```bash
$ cd ../teardroid_control/
```

- Deploy the Control panel using the following command.

```bash
$ deta deploy
```

### Run control panel on your own server

- Clone [Teardroidv4_api](https://github.com/ScRiPt1337/Teardroidv4_api) repo using the command below

```bash
$ git clone https://github.com/ScRiPt1337/Teardroidv4_api
```

- Install uvicorn

```bash
$ sudo apt-get install uvicorn
$ python3 -m pip install uvicorn
```

- Change dir to Teardroidv4_api

```bash
$ cd Teardroidv4_api
```

- Install all dependency

```bash
$ pip install -r requirements.txt
```

- Run teardroid api

```bash
$ screen
# press enter to go inside the screen session
$ uvicorn main:app --host 0.0.0.0 --port 80
# now close your terminal windows  and we are good to go
```

- Done

### How to setup

- Clone Teardroid-phprat repo with the following command.

```bash
$ git clone https://github.com/ScRiPt1337/Teardroid-phprat
```

- cd in the Teardroid-phprat directory, then type the command below to install all dependencies

```bash
$ pip install -r requirements.txt
```

- Run the following command to see the options that we can use with the builder.

```bash
$ python Teardroid.py
[+] Checking Python Version
[+] Python Version : 3.10 ✓
  ______                    __           _     __         __ __
 /_  __/__  ____ __________/ /________  (_)___/ /  _   __/ // /
  / / / _ \/ __ `/ ___/ __  / ___/ __ \/ / __  /  | | / / // /_
 / / /  __/ /_/ / /  / /_/ / /  / /_/ / / /_/ /   | |/ /__  __/
/_/  \___/\__,_/_/   \__,_/_/   \____/_/\__,_/    |___/  /_/


Teardroid v4.0 - A tool to build teardroid spyware for Android devices. 🕷
Contact us : https://t.me/script1337 🚀
usage: Teardroid.py [-h] [-v] [-b]

options:
  -h, --help     show this help message and exit
  -v, --version  Version of Teardroid 🥴
  -b , --build   Build Teardroid with custom name [ex: Teardroid.py -b teardroid] 😷
```

- To create an apk execute the following command.

```bash
$ python Teardroid.py -b your_app_name
```

- It will prompt you with your Control Panel url enter your deta micro URL (without / at the end of the url).
- You will also be prompted for the title and text of the notification. Enter what you want to display on the notification.
- DONE

- ![Build using codespace](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/625b8abb-089b-4896-98c9-43dc28ab740b.gif)

### Dashboard

- visit : https://{your server url}/v4/overview
- defualt username/password is : admin/admin

### Screenshot

- ![Builder](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/Builder_3oDdS0Tr7.png)

- ![Overview](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/2022-01-27_22-29_gYkI6tIvGmG.png)

- ![TaskManager](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/2022-01-27_22-49_RakvqeLWG.jpeg)

### Setup Video

- video : [setup control panel and build apk using browser only](https://www.instagram.com/reel/Ck1kbjWDvq6/?igshid=YmMyMTA2M2Y%3D)
- old Video : [how to hack android phone using Teardroid v4](https://www.instagram.com/tv/CZSu4y0osHo/?utm_source=ig_web_button_share_sheet)

### :atm: Want something with more advanced features try Scatter ALFA

- Scatter ALFA is paid.
- Get a live demo on google meet or zoom.
- Message me on telegram if you're interested => https://t.me/script1337
- join our telegram channel https://t.me/scatter1337

![Screenshot](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/scatter.png)

![dashboard](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/dashboard.png)

![1](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/1.png)

![2](https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/2.png)

### Support me

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/script1337x)

### Beware from scam

- Make sure the channel username is @scatter1337 beware from scam
- I am only available on telegram and script1337 is my only account please double check the username

### Contact info

- Email : anon42237@gmail.com
- Telegram : https://t.me/script1337
- Visit our website : https://www.hacksec.in
