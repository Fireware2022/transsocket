import socket
import os

import time 
from colorama import Fore, Back, Style, init
init()
RED = Fore.RED
ORANGE = Fore.RED + Style.BRIGHT
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
def stampa(colore, testo):
    print(colore + testo + Fore.RESET)


stampa(ORANGE, "Transsocket *********** Fireware™ ")
s=socket.socket()
ipf = open("client.cfg","r")
ip = ipf.read()
ipf.close()
s.connect((ip,8080))
byte = 0

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(GREEN)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    print(Fore.RESET)
    # Print New Line on Complete
    if iteration == total: 
        print()
        
        
while True:
    byte = 0
    print(CYAN,"file to move:",end="")
    file = input("")
    file = r"{}".format(file)
    if os.path.exists(file):
        s.send(file.encode())
        #s.send("{:010d}".format(len(file)).encode())
        
    
    
        size = os.path.getsize('{}'.format(file))
        s.send("{:016d}".format(size).encode())
        print("size:{}B".format(size))
        f = open('{}'.format(file),'rb')
        data_in = f.read(38400)
        while data_in:
            s.send(data_in)
            data_in = f.read(38400)
            byte += len(data_in)
            printProgressBar(byte, size, prefix = 'Moving:', suffix = 'Complete',decimals = 1)
            os.system("cls")
        
        f.close()
        stampa(CYAN,"done")
    else:
        print(RED,"Error: the file doesn't exists")
    
 