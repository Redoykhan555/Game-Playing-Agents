from random import choice

"""
Interface to be implemented State :
maxP() : bool
terminated() : bool
possbl_moves() : iterator to all moves
move(mv) : State
heur() : Number
buildState : State (take inputs and return root State)
"""

INF = 999999999

def prune(state,depth,alpha,beta):
    if depth==0 or state.terminated():
        return state.heur()
    
    if state.maxP():
        v = -INF
        for mv in state.possbl_moves():
            v = max(v,prune(state.move(mv),depth-1,alpha,beta))
            alpha = max(v,alpha)
            if beta<=alpha: break
                
    else:
        v = INF
        for mv in state.possbl_moves():
            v = min(v,prune(state.move(mv),depth-1,alpha,beta))
            beta = min(beta,v)
            if beta<=alpha:break

    return v

def play(state,depth=5):    
    ans = []
    for mv in state.possbl_moves():
        a = prune(state.move(mv),depth,-INF,INF)
        ans.append((a,mv))
        
    ans = sorted(ans)
    
    if state.maxP(): temp = ans[-1][0]
    else: temp = ans[0][0]
    tarr = [v for v in ans if v[0]==temp]
    return choice(tarr)[1]
































