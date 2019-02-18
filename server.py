from socket import *
import datetime
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

import socket
while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        currentDateTime = datetime.datetime.now()
        CurrentTime = (currentDateTime.strftime("%H:%M:%S"))
        CurrentDate = currentDateTime.strftime("%Y:%m:%d")
        IPHOSTNAME = socket.gethostname()
        IP = socket.gethostbyname(IPHOSTNAME)
        capitalizedSentence = sentence.upper()
        if sentence == 'W0676245':
            connectionSocket.send("Hi, pleased to meet .".encode())
            connectionSocket.send(capitalizedSentence.encode())
        elif sentence == 'REQTIME':
                    connectionSocket.send(CurrentTime.encode())
        elif sentence == 'REQDATE':
                        connectionSocket.send(CurrentDate.encode())
        elif sentence == 'REQIP':
                                connectionSocket.send(IP.encode())
        
        print('Got From Server: ', capitalizedSentence)
        connectionSocket.close()
