'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@author: lhs3 (Luke Steffen)
@version Feb 29, 2020
'''

from probability import JointProbDist, enumerate_joint_ask

'''
Math to solve P(cavity | catch)

P(cavity | catch) = P(cavity && catch) / P(catch)

P(cavity && catch) = 0.108 + 0.072 = 0.18
P(catch) = 0.108 + 0.016 + 0.072 + 0.144 = 0.34

P(cavity && catch) / P(catch) = 0.18 / 0.34 = 0.5294117647 ~= 0.529

P(cavity | catch) = 0.529
'''

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Catch=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())

# The Joint Probability Distribution of flipping two coins
C = JointProbDist(['Coin1', 'Coin2'])
H, T = True, False
C[H, H] = 0.25; C[H, T] = 0.25
C[T, H] = 0.25; C[T, T] = 0.25

# Compute P(Coin2 | Coin1) (Coin2 = heads | Coin1 = heads)
CF = enumerate_joint_ask('Coin2', {'Coin1': H}, C)
print(CF.show_approx())


'''
This answer does confirm what I believe to be true about the probabilities of
flipping coins. Since the process of flipping coins is independent of each other,
The probability of getting heads or tails on one coin will not affect the
probability of the other coin. This means that the two coins are statistically
independent of each other.

I can see why full joing is not generally used in probablistic systems from this
exercise. The biggest reason why I think it is not used is because for every
variable added, the number of probabilities needed to fill the chart grows
exponentially. In most real life circumstances, like diagnosing an illness, the
tables of probabilities needed is extremely large and unweildy to keep and update
on a regular basis. Because of this issue, full joint is generally not used to 
solve these issues.
'''
