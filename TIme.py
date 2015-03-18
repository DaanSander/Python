import os
import time
hs=0
s=0
m=50
h=12
while hs<60:
    os.system('cls')
    print (h, "Uren", m, "Minuten", s, "Seconden", hs, "Honderdsten")
    time.sleep(0.01)
    hs+=1
    if hs == 60:
        hs=0
        s+=1
    if s == 60:
        m+=1
        s=0
    elif m == 60:
        h+=1
        m=0