from math import *
from random import *
from copy import deepcopy
import subprocess as sp

from Mancala import State


def call(player,state):
    fh = open("inp.txt","w")
    fh.write(str(state))
    fh.close()

    fh = open("inp.txt")
    cp = sp.run(player,stdin=fh,stdout = sp.PIPE,stderr=sp.PIPE,shell=True)
    if cp.stderr:
        print(cp.stderr.decode())
    return cp.stdout.decode()

p2 = ["python","c:/Users/USER/Desktop/playground/test.py"]
p1 = ["python","c:/Users/USER/Desktop/playground/MancalaMCTS.py"]

board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]

s = State(0,board)

while not s.terminated():
    print(s)
    if s.maxP():
        m = call(p1,s)
    else:
        m = call(p2,s)

    m=int(m)

    print(m,"\n")
    
    if s.maxP(): m = m -1
    else : m = 6+m
    s = s.move(m)

    
print(s)






















