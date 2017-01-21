from time import time

fram = open("../1.png",'rb').read()
for i in fram:
    print("%x")%i