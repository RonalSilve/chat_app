import socket
import threading


class Cliente():
    """docstring for Cliente"""
    name=input("usuario:")
    def __init__(self, host="192.168.43.253", port=31337,name=name):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))

        msg_recv = threading.Thread(target=self.msg_recv)

        msg_recv.daemon = True
        msg_recv.start()

        while True:
            msg = input('->')
            if msg != 'salir' :
                self.send_msg(name+":"+msg)
            else:
                self.sock.close()
                sys.exit()

    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print(str(data,"utf-8"))
            except:
                pass

    def send_msg(self, msg):
        self.sock.send(str.encode(msg,"utf-8"))


c = Cliente()
