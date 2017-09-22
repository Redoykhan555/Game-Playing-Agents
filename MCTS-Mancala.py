from math import *
from random import *
from copy import deepcopy

class State:
    def __init__(self,c,arr):
        self.c=c
        self.arr=arr
        self.to_move = c

    def move(self,ind):
        v = self.arr[ind]
        newArr = deepcopy(self.arr)
        newArr[ind] = 0
        toPut = ind+1
        while v: #v Can Not be Zero
            if self.opCala()!=(toPut%14):
                newArr[toPut%14]+=1
                v-=1
            toPut+=1
 
        lastPut = (toPut-1)%14
        if self.myCala()==lastPut:
            return State(self.c,newArr)

        if self.myhole(lastPut) and newArr[lastPut]==1:
            oppHole = 12-lastPut
            if newArr[oppHole]>0:
                newArr[lastPut] = 1 + newArr[oppHole]
                newArr[oppHole] = 0
                

        if self.nil(self.myhole,newArr):
            newArr[self.opCala()] = 48 - newArr[self.myCala()]
        if self.nil(self.oppHole,newArr):
            newArr[self.myCala()] = 48 - newArr[self.opCala()]
            
        return State(1-self.c,newArr)
        
    def myhole(self,ind):
        if self.c==0: return 0<=ind<=5
        return 7<=ind<=12

    def oppHole(self,ind):
        return (not self.myhole(ind)) and (ind!=self.myCala()) and (ind!=self.opCala())
    
    def myCala(self):
        return 6+self.c*7

    def opCala(self):
        return 13-self.c*7

    def nil(self,func,arr):
        for i in range(14):
            if func(i) and arr[i]>0:
                return False
        return True

    def terminated(self):
        return sum(self.arr[:6])==0 or sum(self.arr[7:13])==0

    def possbl_moves(self):
        for i in range(14):
            if self.myhole(i) and self.arr[i]>0:
                yield i

    def result(self):
        if self.arr[6]>24 : return 0
        if self.arr[13]>24: return 1
        return -99

    def __repr__(self):
        return str(self.c)+":"+str(self.arr)



class Node:
    def __init__(self,state,parent=None):
        self.state = state
        self.wins = 0
        self.visits = 0
        self.parent = parent
        self.children = {mv:None for mv in state.possbl_moves()}

def select(root):
    """Recursively search until a node with at least one
    child remains to be created is found"""
    for move in root.children:
        if root.children[move]==None:
            return root

    #root has all childs expanded, so choose eligible one
    childs = [ch for mv,ch in root.children.items()]
    if not childs: return None

    best_one = max(childs,
            key=lambda c:c.wins/c.visits+sqrt(2*log(root.visits/c.visits)))
    return select(best_one)

def expand(root):
    """since children is a dictionary, keys should be randomized already"""
    for mv in root.children: 
        if root.children[mv]==None:
            root.children[mv] = Node(root.state.move(mv),root)
            return root.children[mv]

def simulate(state):
    while not state.terminated():
        possbl_moves = list(state.possbl_moves())
        state = state.move(choice(possbl_moves))
    return state.result()

def propagate(node,result):
    if node==None: return
    if node.state.to_move == 1-result:
        node.wins +=1
        
    node.visits += 1
    propagate(node.parent,result)

def episode(root):
    node = select(root)
    if not node: return

    node = expand(node)
    result = simulate(node.state) 
    propagate(node,result)

def play(st):
    nd = Node(st)
    for i in range(3800):
        episode(nd)
    return max(nd.children.items(),key=lambda c:c[1].visits)


c = int(input())-1
ma = int(input())
tmp = list(map(int,input().split()))
mb = int(input())
tm2 = list(map(int,input().split()))
arr = tmp+[ma]+tm2+[mb]

st = State(c,arr)
mv,a = play(st)

if mv>6:
    print(abs(6-mv))
else:
    print(mv+1)


