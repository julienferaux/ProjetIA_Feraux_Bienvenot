#!/usr/bin/python           # This is client.py file

import socket
import sys, getopt

import re  # findall
import time  # sleep

d = 7


###############
### client ###
###############
def client(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    msg = s.recv(1024).decode()  # reception du joueur qui commence
    print(msg)
    if msg == "Serveur: A vous de jouer":
        myTurn = True

    else:
        myTurn = False

    while True:
        if myTurn:
            msg = minmax()
            # alphabeta
            print("envoie ", msg)
            if (msg[0] == "abandon") or (
                    len(msg) == 4 and (int(msg[0]) <= d) and (int(msg[1]) <= d) and (int(msg[2]) <= d) and (
                    int(msg[3]) <= d)):
                s.send(str(msg).encode())
                myTurn = False
                if msg[0] == "abandon":
                    s.close()  # Close the connection
                    exit()  # end the program
            else:
                print(msg, ": mauvais format")
        else:  # myTurn == False
            msg = s.recv(1024).decode()  # reception du joueur qui commence
            print("Serveur : l'adversaire envoie :", msg)
            if msg[2:9] == "abandon":
                print("Serveur : l'adversaire abandonne. Merci de vous êtes connectés. Au revoir.")
                s.close()  # Close the connection
                exit()  # end the program
            print(msg)  # print msg,"\a" affiche les donnees envoyees, suivi d'un bip sonore.
            vals = re.findall('\d+', msg)
            key1 = (int(vals[0]), int(vals[1]))
            key2 = (int(vals[2]), int(vals[3]))
            print(key1, key2)
            # move(key1, key2)
            myTurn = True


def minmax():
    res = ''

    return res


def main(argv):
    host = ''
    port = ''
    try:
        opts, args = getopt.getopt(argv, "hi:p:", ["host=", "port="])
    except getopt.GetoptError:
        print('awale-MulticlientGFX3.py -i <IPv4> -p <port>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('awale-MulticlientGFX3.py -i <IPv4> -p <port>')
            sys.exit()
        elif opt in ("-i", "--ip"):
            host = arg
            print('Adresse IP du serveur : ', host)
        elif opt in ("-p", "--port"):
            port = int(arg)
            print('N de port du serveur : ', port)
    client(host, port)


if __name__ == "__main__":
    main(sys.argv[1:])
