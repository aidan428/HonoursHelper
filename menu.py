from options.downloadArtefacts import run
from options.performDeletions import user_interaction

from colorama import Fore, Back, Style
from time import sleep
import welcome


menu_options = {
    1: "Download Forensic Artefacts",
    2: "Artefact Deletions",
    0: "Exit"
}

def print_menu():
    for key in menu_options.keys():
        print (Fore.CYAN, key, Style.RESET_ALL, "--", menu_options[key] )

def menu_handler():
    while(True):
        welcome.back_to_menu()
        print_menu()
        print("\n")
        option = ''
        try:
            option = int(input(Fore.YELLOW + 'Enter menu option: ' + Style.RESET_ALL))
        except:
            print(Fore.RED + 'Error detecting option. Did you enter a number?' + Style.RESET_ALL)
        #Check what choice was entered and act accordingly
        if option == 1:
            run()
        if option == 2:
            user_interaction()

        elif option == 0:
            print(Fore.GREEN + Style.BRIGHT + "Thank you for using this tool!" + Style.RESET_ALL)
            quit()
        else:
            print(Fore.RED + 'Invalid option. Please enter a number between 0 and 3.' + Style.RESET_ALL)
            print("\n")