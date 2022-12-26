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
statistiques = {'fact':0,'fib':0,'add':0, 'sous':0,'div':0,'mult':0}

#Creer une socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Liez la socket a une adresse et un port
server_socket.bind((host, port))
print(">>>Le serveur est demarrer ...")
nbre = 0 
#Ecoutez les connecions entrantes
server_socket.listen(5)
print("En ecoute")

#Declaration des fonction

def faireOperation(message_server, client_socket):
    operation, *args = message_server.split()
    print("\n Operation : {}".format(operation))
    #conversion des arguments en entiers
    args = [int(arg) for arg in args]
    if operation == '1':
        resultat = addition(*args)
    elif operation == '2':
        resultat = soust(*args)
    elif operation == '3':
        resultat = div(*args)
    elif operation == '4':
        resultat = mult(*args)
    elif operation == '5':
        resultat = fact(*args)
    elif operation == '6':
        resultat = fibonacci(*args)
    else:
        print("Rien a faire")
    # Envoi du résultat au client
    client_socket.send(str(resultat).encode())

def gerer_client(client,adrr) :
    print(f'> {adrr} client : connecté')
    while True :
        #Reception de message
        message_server = client.recv(1024).decode("utf8")
        if not message_server :
            print(f"Le client {adrr}est deconnecté ")
            break
        else:
            #print("[\n Message recu de  {} client : {}".format(adrr, message_server))
            #print("\n]")
            operation, *args = message_server.split()
            print("\n Operation : {}".format(operation))
            #conversion des arguments en entiers
            args = [int(arg) for arg in args]
            if operation == '1':
                resultat = addition(*args)
            elif operation == '2':
                resultat = soust(*args)
            elif operation == '3':
                resultat = div(*args)
            elif operation == '4':
                resultat = mult(*args)
            elif operation == '5':
                resultat = fact(*args)
            elif operation == '6':
                resultat = fibonacci(*args)
            else:
                print("Rien a faire")
            # Envoi du résultat au client
            client_socket.send(str(resultat).encode())
            

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
