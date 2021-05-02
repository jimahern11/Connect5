import socket
from _thread import *

# HEADER = 64
PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(SERVER)

try:
    server.bind((SERVER, PORT))
except socket.error as e:
    str(e)

server.listen(4)
print("Waiting for a connection, Server has started")


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected.")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received: ", data)
                print("Sending : ", reply)


            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
print(currentPlayer)


while True:
    conn, addr = server.accept()
    print("Connected to :", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    print(currentPlayer)
