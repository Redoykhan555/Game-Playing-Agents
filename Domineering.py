from copy import deepcopy
import os

from AlphaBeta import play

class State:
    def __init__(self,c,a):
        self.c = c
        self.grid = a

    def maxP(state):
        return state.c=='v'
    
    def __str__(self):
        c='v\n'
        if self.c=='h': c='h\n'
        temp = [''.join(self.grid[i]) for i in range(8)]
        return c+'\n'.join(temp)

    def helper(state,func):
        ans = 0
        v = set()
        h = set()
        for i in range(7):
            for j in range(8):
                if func('v',i,j) and (i,j) not in v:
                    ans+=1
                    v.add((i+1,j))

        for i in range(8):
            for j in range(7):
                if func('h',i,j) and (i,j) not in h:
                    ans-=1
                    h.add((i,j+1))
        return ans

    def heur(state):
        def empty(c,i,j):
            #if both boxes for a move starting from i,j are empty
            if c=='v': return state.grid[i][j]=='-' and state.grid[i+1][j]=='-'
            else : return state.grid[i][j]=='-' and state.grid[i][j+1]=='-'

        def safe(c,i,j):
            #if a single box is safe, not move
            if c=='v':return (j==7 or not empty('h',i,j)) and (j==0 or not empty('h',i,j-1))
            else: return (i==7 or not empty('v',i,j)) and (i==0 or not empty('v',i-1,j))

        def socr(c,i,j):
            if not safe(c,i,j): return False
            if c=='v': return safe(c,i+1,j)
            return safe(c,i,j+1)
     
        real = state.helper(empty)
        safe = state.helper(socr)
        return real+safe



    def possbl_moves(state):
        if state.c=='v':
            for i in range(7):
                for j in range(8):
                    if state.grid[i][j]=='-' and state.grid[i+1][j]=='-':
                        yield (i,j)
                    
    
        if state.c=='h':
            for i in range(8):
                for j in range(7):
                    if state.grid[i][j]=='-' and state.grid[i][j+1]=='-':
                        yield (i,j)
                        

    def move(state,mv):
        i,j=mv
        arr = deepcopy(state.grid)
        if state.c=='v':
            arr[i][j] = 'v'
            arr[i+1][j] = 'v'
            return State('h',arr)
        else:
            arr[i][j] = 'h'
            arr[i][j+1] = 'h'
            return State('v',arr)

    def terminated(state):
        try:
            next(state.possbl_moves())
            return False
        except:
            return True

    def result(state):
        return state.c=='v' #if I am 'v' return 1 i.e winner is 'h'

if __name__=='__main__':
    c = input()
    arr = [None]*8
    for i in range(8):
        arr[i]=list(input())

    s = State(c,arr)
    mv = play(s,1)
    print(mv[0],mv[1],flush=True)

    os._exit(0)





