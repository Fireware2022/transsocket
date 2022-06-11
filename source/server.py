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
    


stampa(RED, Style.BRIGHT + "Transsocket Server *********** Fireware™ ")
s=socket.socket()
host = socket.gethostname()
local_ip = socket.gethostbyname(host)
stampa(GREEN,"Binding")
s.bind(('0.0.0.0',8080))
stampa(GREEN,"Listening")
s.listen()

c,addr = s.accept()
stampa(GREEN,"Received connection from {}".format(addr))

while True:
    
    file = c.recv(1024)
    
    sizetot = c.recv(1024)
    
    stampa(CYAN,"{}B".format(sizetot.decode()))
    stampa(CYAN,"{}".format(file.decode()))
    f = open("{}".format(file.decode()),"wb")
    
    size = 0
    
    while True:
        
        data_in=c.recv(38400)
        size += len(data_in)
        f.write(data_in)
        
        #print(int(sizetot.decode()))
        
        #if size >= int(sizetot.decode()):
            #i = False
        if len(data_in) != 38400:
            break
        
        #print(len(data_in), size)
    f.close()
    
        
        
       
    stampa(CYAN,"file received")
