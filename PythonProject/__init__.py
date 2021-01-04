import server as S
import Agent

i = 0

while True:
    S.sock.SendData('Sent from Python: ' + str(i)) # Send this string to other application
    i += 1

    data = S.sock.ReadReceivedData() # read data

    if data != None: # if NEW data has been received since last ReadReceivedData function call
        print(data) # print new received data

    S.time.sleep(1)