#!/usr/bin/python
from random import randint





def attGen():
    return randint(1,6) + randint(1,6)

def hexForm(attrib):
    return str(hex(attrib)[2:].upper())

attributes = []

x = 0 
while x < 6:
   attributes.append(attGen())
   x = x + 1

strng = attGen()
dex = attGen()
endu = attGen()
intel = attGen()
edu = attGen()
socSt = attGen()

#print strng
print hexForm(strng) +  hexForm(dex) +  hexForm(endu) +  hexForm(intel) +  hexForm(edu) +  hexForm(socSt)

print ''.join(str(attributes)) 
#print str(hex(strng + dex + endu + intel + edu + socSt)[2:]).upper() 
