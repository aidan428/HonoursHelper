import os
import hashlib
from colorama import Fore, Back, Style


def get_md5():
    filename = "Artefacts.zip"
    originalHash = "49301a58c1c60d1d58af056b5be4fdfc"

    with open(filename, 'rb') as file_to_check:
        data = file_to_check.read()
        md5_artefacts = hashlib.md5(data).hexdigest()

    if originalHash == md5_artefacts:
        print(Fore.GREEN + 'MD5 Match!' + Style.RESET_ALL)
    else:
        print(Fore.RED + 'MD5 Mismatch! Do not use this file!' + Style.RESET_ALL)

