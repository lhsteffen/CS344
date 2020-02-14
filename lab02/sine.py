"""
This module implements local search on a simple abs sin function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden, lhs3
@version 13feb2020
"""
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class SinVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """
    
    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta
        
    def actions(self, state):
        return [state + self.delta, state - self.delta]
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, x):
        return abs(x * math.sin(x))


if __name__ == '__main__':

    # Formulate a problem with a 2D abs sin function and a single maximum value.
    maximum = 30
    bestHill = 0
    bestSim = 0
    for x in range(0, 10):
        initial = randrange(0, maximum)
        p = SinVariant(initial, maximum, delta=1.0)

        # Solve the problem using hill-climbing.
        hill_solution = hill_climbing(p)

        if p.value(bestHill) <= p.value(hill_solution):
            bestHill = hill_solution

        # Solve the problem using simulated annealing.
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )

        if p.value(bestSim) <= p.value(annealing_solution):
            bestSim = annealing_solution

    print('\nHill-climbing solution       x: ' + str(bestHill)
       + '\tvalue: ' + str(p.value(bestHill))
    )

    print('Simulated annealing solution x: ' + str(bestSim)
       + '\tvalue: ' + str(p.value(bestSim))
    )
