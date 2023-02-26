import requests
import cgi
import os
from tqdm import tqdm
from colorama import Fore, Back, Style
from zipfile import ZipFile
from options.calculateHash import get_md5
import sys



download_link = r"https://honours.spaldotech.co.uk/Artefacts.zip"

def get_username():
  username = os.getlogin()
  return username

def determine_os():
    os = ""

    if sys.platform == "linux" or sys.platform == "linux2":
        os = "Linux"
    elif sys.platform == "win32":
        os = "Windows"
    return os
    

def download_zip():
    #url = r"https://repo.spaldotech.co.uk/Civ/LEKMOD_V28.zip"
    
    buffer_size = 1024
    response = requests.get(download_link, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))
    default_filename = download_link.split("/")[-1]
    content_disposition = response.headers.get("Content-Disposition")
    if content_disposition:
        # parse the header using cgi
        value, params = cgi.parse_header(content_disposition)
        # extract filename from content disposition
        filename = params.get("filename", default_filename)
    else:
        # if content dispotion is not available, just use default from URL
        filename = default_filename
    progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))
    return filename

def extract_forensic_artefacts():
    opsystem = determine_os()
    print(opsystem + " detected!") 
    mainPathWindows = "C:\\Users\\" + get_username() + "\\Desktop\\"
    mainPathLinux = "/home/" + get_username() + "\\Desktop\\"

    file_name = download_zip()

    try:
        with ZipFile(file_name, 'r') as zip_ref:
            if opsystem == "Windows":
                zip_ref.extractall(mainPathWindows)
            elif opsystem == "Linux":
                zip_ref.extractall(mainPathLinux)
            #zip.extractall(mainPath)
            print(Fore.GREEN + "Extraction Complete!" + Style.RESET_ALL)
            #print("\n")
    except Exception as e:
        print(e)
        print(download_link)
        print(Fore.RED + "Failed to install. Please contact Mr Spalding and show him the above error trace." + Style.RESET_ALL)
        
    
    try:
        get_md5()
    except Exception as e:
        print(e)
        print("Unable to check MD5")

    try:
        os.remove("Artefacts.zip")
    except Exception as e:
        print("Unable to remove installer files!")
        print(e)


def run():
    extract_forensic_artefacts()
