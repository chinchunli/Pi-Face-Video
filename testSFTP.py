from connection.mySFTP import uploadVideoSFTP

myDict = {'ip': '1.34.62.109', 'username' : 'guest', 'password' : 'guest',
              'home': '/home/guest/knightVideo/'}

a = uploadVideoSFTP('test3.png',**myDict)
print(a)
