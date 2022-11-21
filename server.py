import socket
import threading

server = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM

)


server.bind(

    ("127.34.76.32", 5769)

)

server.listen(5)
print("Server is listening")

users = []


def send_all(data):
    for user in users:
        user.send(data)


def listen_user(user):
    print('Listening user')
    name = user.recv(2048)
    print(f"User name is: {name.decode('utf-8')}")
    while True:
        data = user.recv(2048)
        print(data.decode("utf-8"))
        send_all(data)


def start_server():
    while True:
        user_socket, address=server.accept()
        print(f"User <{address[0]}> connected!")

        users.append(user_socket)
        mods = "Moderator"

        users[0].send(mods.encode('utf-8'))

        listen_accepted_user = threading.Thread(target=listen_user, args=(user_socket,))

        listen_accepted_user.start()


start_server()