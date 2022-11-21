import socket
from threading import Thread

client = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM

)

client.connect(

    ("127.34.76.32", 5769)

)
name = str(input("Введите псевдоним: "))
client.send(name.encode("utf-8"))
global status
status = "{USER}"

data_mod = client.recv(2048)
print(data_mod.decode('utf-8'))
if data_mod.decode('utf-8') == "Moderator":
    print('Hi Moderator')
    status = "{MODERATOR}"


def listen_server():
    while True:
        data = client.recv(2048)

        print(data.decode("utf-8"))


def send_server():
    listen_thread = Thread(

        target=listen_server

    )

    listen_thread.start()

    while True:
        client.send((':::' + status + '' + name + ': ' + input()).encode("utf-8"))


if __name__ == '__main__':
    send_server()