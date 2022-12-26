#coding:utf8
import socket
import threading        
from operation import *
host, port = ('localhost', 5050)
TAILLE = 1024
FORMAT = "utf8"

# Création d'un verrou
lock = threading.Lock()

# Variable partagée
#statistiques = {'fact':0,'fib':0,'add':0, 'sous':0,'div':0,'mult':0}
#ou en plusieur variable
nbreFact = 0
nbreFib = 0
nbreAdd = 0
nbreSous = 0
nbreMult = 0
nbreDiv = 0
#Creer une socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Liez la socket a une adresse et un port
server_socket.bind((host, port))
print(">>>Le serveur est demarrer ...")
#Ecoutez les connecions entrantes
server_socket.listen(5)
print("En ecoute")

#Declaration des fonction
def voireStatistique():
    global nbreFact
    global nbreFib
    global nbreAdd
    global nbreSous
    global nbreMult
    global nbreDiv
    print("********************************")
    print("\les statistiques des fonction\n")
    print("Addtion : {}".format(nbreAdd))
    print("Soustraton : {}".format(nbreSous))
    print("Division : {}".format(nbreDiv))
    print("Multiplication : {}".format(nbreMult))
    print("Fibbonaci : {}".format(nbreFib))
    print("Factoriel: {}".format(nbreFact))
def faireOperation(message_server, client_socket):
    operation, *args = message_server.split()
    #conversion des arguments en entiers
    args = [int(arg) for arg in args]
    
    if operation == '1':
        lock.acquire()
        resultat = addition(*args)
        global nbreAdd
        nbreAdd += 1
    elif operation == '2':
        lock.acquire()
        resultat = soust(*args)
        global nbreSous
        nbreSous += 1
    elif operation == '3':
        lock.acquire()
        resultat = div(*args)
        global nbreDiv
        nbreDiv += 1
    elif operation == '4':
        lock.acquire()
        resultat = mult(*args)
        global nbreMult
        nbreMult += 1
    elif operation == '5':
        lock.acquire()
        resultat = fact(*args)
        global nbreFact
        nbreFact += 1
    elif operation == '6':
        lock.acquire()
        resultat = fibonacci(*args)
        global nbreFib
        nbreFib += 1
    else:
        print("Rien a faire")
    # Envoi du résultat au client
    client_socket.send(str(resultat).encode())
    # Libération du verrou
    lock.release()
def gerer_client(client,adrr) :
    print(f'> {adrr} client : connecté')
    while True :
        #Reception de message
        message_server = client.recv(1024).decode("utf8")
        if not message_server :
            print(f"Le client {adrr}est deconnecté ")
            break
        else:
            faireOperation(message_server, client)
            voireStatistique()
            
            

#FIN Declaration des fonction
while True:
    #Acceptez la connexion entrante
    client_socket, client_address = server_socket.accept()
    
     #création d'un thread pour gérer la connexion client
    thread = threading.Thread(target=gerer_client,args=(client_socket,client_address))
    thread.start()

#Fermez la connexion et la socket côté serveur
conn.close()
socket.close()
