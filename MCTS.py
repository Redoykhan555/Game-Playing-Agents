from math import *
from random import *

"""
Interface for MCTS State:
possbl_moves() : iterator to all possible moves
move(mv) : State
result() : 0,1 (0 if first player wins,1 if second, -1 if draw)
terminated() : bool
maxP() : bool (if first player)
"""

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

def propagate(node,winner):
    if node==None: return
    if winner==-1: #Simulation ended in draw
        node.wins += .5
    else:
        assert winner==0 or winner==1
        player = (node.state.maxP()==False)
        if player!=winner:
            node.wins += 1
        
    node.visits += 1
    propagate(node.parent,winner)

def episode(root):
    node = select(root)
    if not node: return

    node = expand(node)
    result = simulate(node.state) 
    propagate(node,result)

def play(state,rounds=5000):
    root = Node(state)
    for i in range(rounds):
        episode(root)

    for mv,ch in root.children.items():
    	#print(mv,ch.wins,ch.visits,ch.wins/ch.visits)
    	pass

    return max(root.children.items(),key=lambda c:c[1].visits)[0]




