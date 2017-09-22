from copy import deepcopy
import os

from AlphaBeta import play

INF = 9999999999

class State:
    def __init__(self,c,arr):
        self.c=c
        self.arr=arr

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
        return self.nil(self.myhole,self.arr) or self.nil(self.oppHole,self.arr)

    def heur(self):
        if self.arr[6]>24 or (self.arr[7]+self.arr[8]+self.arr[9]+self.arr[10]+self.arr[11]+self.arr[12]==0): return INF
        if self.arr[13]>24 or (self.arr[0]+self.arr[1]+self.arr[2]+self.arr[3]+self.arr[4]+self.arr[5]==0): return -INF
        
        r = self.arr[6]-self.arr[13]
        p = 0
        q = 0
        for i in range(14):
            if 0<=i<6: p+=self.arr[i]
            if 7<=i<13 : p-=self.arr[i]

            if 0<=i<6 and self.arr[i]==6-i: q+=1
            if 7<=i<13 and self.arr[i]==13-i: q-=1
            
        return 125*r+21*p+140*q

    def possbl_moves(self):
        for i in range(14):
            if self.myhole(i) and self.arr[i]>0:
                yield i

    def maxP(self):
        return self.c==0

    def result(self):
        if self.arr[6]>24: return 0
        if self.arr[13]>24: return 1
        return -1

    def __repr__(self):
        return str(self.c)+":"+str(self.arr)

    def __str__(state):
    	s = str(state.c+1)+"\n"
    	s += str(state.arr[6])+"\n"
    	s += ' '.join([str(i) for i in state.arr[:6]])+"\n"
    	s += str(state.arr[13])+"\n"
    	s += ' '.join([str(i) for i in state.arr[7:13]])+"\n"
    	return s


if __name__=='__main__':
    c = int(input())-1
    ma = int(input())
    tmp = list(map(int,input().split()))
    mb = int(input())
    tm2 = list(map(int,input().split()))
    arr = tmp+[ma]+tm2+[mb]
    s = State(c,arr)

    mv = play(s,6)
    if mv>6: mv=mv-6
    else : mv = mv + 1
    
    print(mv,flush=True)

    os._exit(0)


















