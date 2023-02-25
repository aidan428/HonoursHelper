from colorama import Fore, Back, Style
from send2trash import send2trash
from prettytable import from_csv
from options.downloadArtefacts import get_username
from options.downloadArtefacts import determine_os
from time import sleep
import sys
import os

def generate_table():
    try:
        with open('data//experiment.csv') as table_file:
            tab = from_csv(table_file)
            return tab
    except Exception as e:
        print("An error has occured while printing the table")
        print(e)

def automatic_deletions():
    mainPathWindows = "C:\\Users\\" + get_username() + "\\Desktop\\Artefacts\\"
    mainPathLinux = "/home/" + get_username() + "/Desktop/Artefacts/"

    a = [6, 7, 8, 9, 10]

    if determine_os() == "Linux":
        send2trash(mainPathLinux + "Artefact1 - ImportantAudio.mp3")
        send2trash(mainPathLinux + "Artefact2 - ImportantArchive.zip")
        send2trash(mainPathLinux + "Artefact3 - ImportantFile.docx")
        send2trash(mainPathLinux + "Artefact4 - IMG_20200706_181127.jpg")
        send2trash(mainPathLinux + "Artefact5 - IMG_20200706_181132.jpg")
        send2trash(mainPathLinux + "Artefact6 - IMG_20210929_190314.jpg")
        send2trash(mainPathLinux + "Artefact7 - IMG_20210929_190326.jpg")
        send2trash(mainPathLinux + "Artefact8 - CentralMoonIdent.mp4")
        send2trash(mainPathLinux + "Artefact9 - Scotland's Railway.mp4")
        send2trash(mainPathLinux + "Artefact10 - BBC Video 1990s ident.mp4")
        #Deletes artefacts 11 - 15 from cmd
        os.remove(mainPathLinux + "Artefact11 - Database.sql")
        os.remove(mainPathLinux + "Artefact12 - Exam Revision.pdf")
        os.remove(mainPathLinux + "Artefact13 - Blockchain Paper.pdf")
        os.remove(mainPathLinux + "Artefact14 - QuickStego.exe")
        os.remove(mainPathLinux + "Artefact15 - python-3.10.3-amd64.exe")
        
    elif determine_os() == "Windows":
        send2trash(mainPathWindows + "Artefact1 - ImportantAudio.mp3")
        send2trash(mainPathWindows + "Artefact2 - ImportantArchive.zip")
        send2trash(mainPathWindows + "Artefact3 - ImportantFile.docx")
        send2trash(mainPathWindows + "Artefact4 - IMG_20200706_181127.jpg")
        send2trash(mainPathWindows + "Artefact5 - IMG_20200706_181132.jpg")
        send2trash(mainPathWindows + "Artefact6 - IMG_20210929_190314.jpg")
        send2trash(mainPathWindows + "Artefact7 - IMG_20210929_190326.jpg")
        send2trash(mainPathWindows + "Artefact8 - CentralMoonIdent.mp4")
        send2trash(mainPathWindows + "Artefact9 - Scotland's Railway.mp4")
        send2trash(mainPathWindows + "Artefact10 - BBC Video 1990s ident.mp4")
        #Deletes artefacts 11 - 15 from cmd
        os.remove(mainPathWindows + "Artefact11 - Database.sql")
        os.remove(mainPathWindows + "Artefact12 - Exam Revision.pdf")
        os.remove(mainPathWindows + "Artefact13 - Blockchain Paper.pdf")
        os.remove(mainPathWindows + "Artefact14 - QuickStego.exe")
        os.remove(mainPathWindows + "Artefact15 - python-3.10.3-amd64.exe")

    sleep(2)

    print(Fore.LIGHTRED_EX + "In order to complete the process, please manually delete the following artefacts from the trash:" + Style.RESET_ALL)
    for x in range(len(a)):
        print(a[x]),
        sleep(1)
    print("Main tasks completed. Please remember to delete the above artefacts from the recycle bin!")
    sys.exit(1)

    


def user_interaction():
    print(Back.RED + Fore.WHITE + "This part requires manual interaction, Aidan." + Style.RESET_ALL)
    print(generate_table())
    print("The table above highlights what will happen to each artefact. For example, Artefact 1 will be moved to the recycle bin.")
    print("This tool will perform the vast majortiy of the work, however, it will require you to manually delete artefacts from the trash. \n" + Fore.RED + "Do you want to continue?")

    while(True):
        option = ''
        try:
            option = input(Fore.YELLOW + 'Y/N: ' + Style.RESET_ALL)
        except:
            print(Fore.RED + 'Error detecting option. Did you enter a letter?' + Style.RESET_ALL)
        #Check what choice was entered and act accordingly
        if option == "Y":
            print("continue")
            automatic_deletions()
            break

        elif option == "y":
            #print("continue")
            automatic_deletions()

        elif option == "N":
            #print("quit tool")
            sys.exit(1)
        
        elif option == "n":
            #print("quit tool")
            sys.exit(1)

        else:
            print(Fore.RED + 'Invalid option. Please enter either Y or N.' + Style.RESET_ALL)
            print("\n")



