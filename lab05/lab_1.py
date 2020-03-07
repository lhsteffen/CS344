'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@author: lhs3
@version Mar 7, 2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Burglary | John and Mary both call).
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.

# Compute P(Alarm | burglary ^ ¬earthquake)
print("\nP(Alarm | burglary ^ ¬Earthquake)")
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# Compute P(John | burglary ^ ¬earthquake)
print("\nP(John | burglary ^ ¬Earthquake)")
print(enumeration_ask('John', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# Compute P(Burglary | Alarm)
print("\nP(Burglary | Alarm)")
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())

# Compute P(Burglary | John ^ Mary)
print("\nP(Burglary | John ^ Mary)")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

'''
The enumeration_ask and elimination_ask algorithms result in the exact same answer,
but the Gibbs sampling results in a slightly different answer. This is because both
enumeration_ask and elimination_ask use similar methods and estimates to find the
probabilities. Gibbs sampling uses a different method of finding probabilities, 
Markov blanket sample, which will result in a different result. Even though the
methods are different, they still give around the same probabilities. Both
enumeration_ask and elimination_ask are consistent methods while Gibbs is not
consistent, giving it a different answer. Enumeration and elimination are 
direct sampling methods. Since they are both direct sampling methods, they will
reach the same result. Gibbs is a Markov chain simulation, which uses a different
method of finding probability than direct sampling, meaning it will find a similar,
but different probability.
'''
