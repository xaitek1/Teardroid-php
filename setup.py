# echo "Teardroid 4.0 installation script"
# curl -fsSL https://get.deta.dev/cli.sh | sh
# deta new --python teardroid_control
# git clone https://github.com/ScRiPt1337/Teardroidv4_api
# cd Teardroidv4_api
# cp -r * ../teardroid_control/
# cd ../teardroid_control/
# deta deploy

import os
from Teardroid import banner
from colorama import Fore, Style
import subprocess


def run_without_output(command: str) -> None:
    os.system(command)


def setup():
    print(Fore.GREEN + banner())
    print(Fore.GREEN + "Running teardroid control panel setup...")
    print(Fore.RED + "Please make sure your running this script as root.")
    print(Fore.GREEN + "Please login into your deta account and go to settings and get the access token")
    access_token = input("Please Enter your access token here : ")
    if (os.name != "posix"):
        print(Fore.RED + "This script is not for windows use wsl or codespace if your using windows or setup control panel manually...")
        os._exit(0)
    print(Fore.GREEN + "updating your system.")
    run_without_output("sudo apt-get update")
    print(Fore.GREEN + "installing git...")
    run_without_output("sudo apt-get install git")
    print(Fore.GREEN + "installing deta-cli...")
    run_without_output("curl -fsSL https://get.deta.dev/cli.sh | sh")
    print(Fore.GREEN + "setting your access token...")
    run_without_output(
        "source ~/.bashrc && export DETA_ACCESS_TOKEN=" + access_token)
    print(Fore.GREEN + "creating new micro in deta...")
    run_without_output(
        "deta new --python teardroid_control")
    print(Fore.GREEN + "cloning teardroid_api repo")
    run_without_output(
        "git clone https://github.com/ScRiPt1337/Teardroidv4_api")
    print(Fore.GREEN + "Moving all the important files...")
    run_without_output("cp -r ./Teardroidv4_api/* ../teardroid_control/")
    print(Fore.GREEN + "Deploying code into the cloud...")
    run_with_output("cd ../teardroid_control/ && deta deploy")


setup()
