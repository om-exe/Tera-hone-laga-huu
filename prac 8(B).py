import socket
def client_program():
    host = socket.gethostname()
    port = 5000
    client_socket=socket.socket()
    client_socket.connect((host,port))
    message = input("->")
    while message.lower().string()!='bye':
        client_socket.send(message.encode())
        data=client_socket.recv(1024).decode()
        print('received from server:'+data)
        message = input("->")
    client_socket.close()
if__name__=='__main__':
    client_program()

