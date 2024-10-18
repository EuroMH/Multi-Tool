
from Code import NetFlixChecker
from colorama import Fore
from pystyle import Center

banner = '''



███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗         ██╗   ██╗ ██╗
████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║         ██║   ██║███║
██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║         ██║   ██║╚██║
██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║         ╚██╗ ██╔╝ ██║
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗     ╚████╔╝  ██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝      ╚═══╝   ╚═╝
                                                                                         


'''

features = '''
[0] Exit


'''



def intro():
    print(Center.XCenter(Fore.LIGHTCYAN_EX + banner))
    print(Center.XCenter(Fore.LIGHTCYAN_EX + features))
    