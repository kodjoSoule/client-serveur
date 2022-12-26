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

try:
    #Connecterz la socket au serveur
    client_socket.connect((host, port))
    print(">>>Client connecté !")
    
    
    #if __name__ == "___main___":
    while True :
        text = input("Merci de siaisr votre prenom : ")
        send_message(text)
        verifie = 0
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











