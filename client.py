#coding:utf-8
import socket
FORMAT = 'utf-8'
TAILLE = 1024
PORT = 5050
#host, port = ('localhost', 5050)
host, port = ('localhost', 5050)
#Creer une socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def send_message(message):
    message = message.encode("utf8")
    client_socket.sendall(message)
def receive_message(conn):
       message_server = conn.recv(1024).decode("utf8")
       return message_server
       ##cd Desktop\Python\client_serveur

def faireOperation() :
    choix = 0
    print("1_addition")
    print("2_Soustraction")
    print("3_Division")
    print("4_Multiplication")
    print("5_Factoriel")
    print("6_Fibbonaci")
    print("7_Fin")
    while( choix < 1 or choix > 6 ):
        choix = int(input("\>:"))
    if choix == 1:
        nbr1 = input("Nombre 1 ? : ")
        nbr2 = input("Nombre 2 ? : ")
        return str(choix) +' '+nbr1+ ' '+nbr2
    elif choix == 2:
        nbr1 = input("Nombre 1 ? : ")
        nbr2 = input("Nombre 2 ? : ")
        return str(choix) +' '+nbr1+ ' '+nbr2
    elif choix == 3:
        nbr1 = input("Nombre 1 ? : ")
        nbr2 = input("Nombre 2 ? : ")
        return str(choix) +' '+nbr1+ ' '+nbr2
    elif choix == 4:
        nbr1 = input("Nombre 1 ? : ")
        nbr2 = input("Nombre 2 ? : ")
        return str(choix) +' '+nbr1+ ' '+nbr2
    elif choix == 5:
        nbr1 = input("Nombre ? : ")
        return str(choix) +' '+nbr1
    elif choix == 6:
        nbr1 = input("Nombre 1 ? : ")
        return str(choix) +' '+nbr1
    else:
        return "fin"
try:
    #Connecterz la socket au serveur
    client_socket.connect((host, port))
    print(">Client connecté !")
    
    #if __name__ == "___main___":
    while True :
        #text = input("Merci de siaisr votre prenom : ")
        #send_message(text)
        messageT = faireOperation()
        send_message(messageT)
        print("En attente de resultat....")
        # Reception du résultat du serveur
        resultat = client_socket.recv(TAILLE).decode(FORMAT)

        #Affichage du résultat
        print(f"Résultat : {resultat}")

        verifie = '0'
        print("1__Oui")
        print("2__Non")
        while(verifie !='1' and verifie !='2') :
            verifie = input(">\: ")
        if verifie == '2' :
            break
except :
    print("> Connecton au serveur echouée ! ")
#finally:
#    client_socket.close()











