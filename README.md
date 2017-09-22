My fascination with artificial game playing agents began with my introduction to alpha-beta 
pruning in class, and my discovery that a chess engine, which took a little more than a night
for me to build, has become intelligent enough almost to beat it's creator. 

This goal of this repository is to primarily work as laboratory where I test out different ideas
and techniques related to AI game  playing agents as I learn them. Of course, It doesn't promise 
the codes here to be bug-free or the most efficient implementation out there. But I would be really 
flattered if someone comes forward to make them better.

The primary language was supposed to be Python. But I strongly suspect Hackerrank, where codes here
are really tested, is biased against slow languages. So almost all of them is accompanied by a c++
implementation.

Files
--------------------------------
AlphaBeta-Mancala.py = The board game mancala based on "Alpha-Beta Pruning". Current score on HR: 47.02,
Rank : 30

AlphaBeta-Mancala.cpp = c++ version of above. HR score : 47.94, rank : 25

MCTS-Mancala.py = Mancala based on "Monte Carlo Search Tree", can make only 4,000 simulations per move in HR. 
However, it regularly beats above Alpha-Beta implementations around 50,000 simulations. HR score : 29.72,
rank : 220

