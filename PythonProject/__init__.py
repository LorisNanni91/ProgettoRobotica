import server as S
import Agent

cane = Agent.Agent("0,0", 3, 4)
world = cane.useBrain().useMemory().getWorld()
print(world)
cane.useBrain().useMemory().insertSheepinWorld("2,1")
print(cane.useBrain().useMemory().getWorld())




# i = 0
#
while True:


    S.sock.SendData("ciao unity")
   # S.sock.SendData('Sent from Python: ') # Send this string to other application
#     i += 1
#
    data = S.sock.ReadReceivedData() # read data

    if data != None: # if NEW data has been received since last ReadReceivedData function call
        print(data) # print new received data
#
#     S.time.sleep(1)


