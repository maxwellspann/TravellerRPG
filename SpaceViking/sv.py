#!/usr/bin/python
from random import randint

def attGen():
    return randint(1,6) + randint(1,6)

def hexForm(attrib):
    return str(hex(attrib)[2:].upper())


strng = attGen()
dex = attGen()
endu = attGen()
intel = attGen()
edu = attGen()
socSt = attGen()


print hexForm(strng) +  hexForm(dex) +  hexForm(endu) +  hexForm(intel) +  hexForm(edu) +  hexForm(socSt)


