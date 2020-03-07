'''
This file implements a Bayesian Network of the probability of
hapiness based on the weather and getting a raise.

@author: lhs3
@version: Mar 7, 2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

# Compute P(Raise | Sunny)
print("P(Raise | Sunny)")
print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())

# Compute P(Raise | Sunny ^ Happy)
print("\nP(Raise | Sunny ^ Happy)")
print(enumeration_ask('Raise', dict(Sunny=T, Happy=T), happy).show_approx())

'''
a. 
Because getting a raise and being sunny are independent events, they have no
effect on the other's probability. This means that the probability of getting a
raise given it's sunny is equal to the probability of getting a raise.

P(Raise | Sunny) = P(Raise) = 0.01

The probability of a raise given it's sunny and you're happy is similar to the
first problem because getting a raise an sunny weather are independent. 

P(Raise | Happy ^ Sunny)

ɑ < P(Raise) * P(Happy | Raise ^ Sunny), P(¬Raise) * P(Happy | ¬Raise ^ Sunny) >
ɑ < 0.01 * 1.0, 0.99 * 0.7 >
ɑ < 0.01, 0.693 >

<0.0142, 0.986>
'''

# Compute P(Raise | Happy)
print("\nP(Raise | Happy)")
print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())

# Compute P(Raise | Happy ^ ¬Sunny)
print("\nP(Raise | Happy ^ ¬Sunny")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())

'''
These results do make sense to me. For the first problem, you could be happy for
a number of reasons besides getting a raise. Because there are a number of reasons
that you could be happy without getting a raise combined with the low probability 
of getting a raise, the chance of getting a raise is low.

For the second problem, there should be slight increase of probability that you
earned a raise because the possibility of it being sunny has been removed. However,
because the chance of getting a raise is so low, there is a higher chance your
happy provided it's not sunny and you didn't get a raise as opposed to getting a raise.
'''

