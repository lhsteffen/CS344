'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@author: lhs3
@version Feb 29, 2020
'''

from probability import JointProbDist, enumerate_joint_ask
import random

# The Joint Probability Distribution with an independent variable
P = JointProbDist(['Toothache', 'Cavity', 'Catch', 'Rain'])

# Random assignment of rain probability
#rain = random.uniform(0, 1)
#nrain = 1 - rain

# Assigned probability of rain
rain = 0.6
nrain = 1 - rain

T, F = True, False
P[T, T, T, T] = 0.108 * rain; P[T, T, F, T] = 0.012 * rain
P[T, T, T, F] = 0.108 * nrain; P[T, T, F, F] = 0.012 * nrain
P[F, T, T, T] = 0.072 * rain; P[F, T, F, T] = 0.008 * rain
P[F, T, T, F] = 0.072 * nrain; P[F, T, F, F] = 0.008 * nrain
P[T, F, T, T] = 0.016 * rain; P[T, F, F, T] = 0.064 * rain
P[T, F, T, F] = 0.016 * nrain; P[T, F, F, F] = 0.064 * nrain
P[F, F, T, T] = 0.144 * rain; P[F, F, F, T] = 0.576 * rain
P[F, F, T, F] = 0.144 * nrain; P[F, F, F, F] = 0.576 * nrain

print("Random chance of rain: " + str(rain))
print ("\nChance of getting a toothache given rain...")
# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print(PC.show_approx())

'''
a.
    i. My full joint distribution table now contains 16 entries. This is because 
        for each of the previous 8 entries, 2 new entries must be added to account
        for rain or no rain, making a total of 16 entries

    ii. The probabilities do sum up to 1.0. This is because the independent variable
        of rain or no rain is still factored in to the overall probability of that
        entry. P(toothache, catch, cavity, rain) = P(rain) * P(toothache, catch, cavity).
        This is true because rain is independent of tootaches, cavities, and catches.
        The chance of rain still remains the same whatever the other values are. It still
        adds to 1.0 because in order to factor rain into the table, each probability
        given must be both multiplied by the chance of rain and the chance of no rain.
        For example, if the chance of rain is 60%, 0.108 must be multiplied by 0.6 once
        for the chance of rain and multiplied by 0.4 for the chance of no rain. The two
        new entries created are 0.108*0.6 (0.0648) and 0.108*0.4 (0.0432). Adding these
        two new entries together will result in the original 0.108. This means that as
        long as the table originally summed up to 1.0 (which it does), the new table will
        also sum up to 1.0. The probabilities do sum up to 1.0, and they should.

    iii. You cannot use any other values besides T or F for the values of random variables.
        This is because the random variable, rain, can only be true or false. It can either
        rain (true) or not rain (false). The probabilities that these are based on can be 
        randomized, like the code above which chooses a random probability of rain. However,
        rain only has two states, rain or no rain. Because rain only has two states, rain,
        and all other variables, can only have a true or false state. The state of each
        variable is binary, but the probability of each state happening can be random.

    iv. Yes, regardless of what values are chosen for the probability of rain, the original
        probabilities of each other variable will remain unchanged. For example, the
        probability of getting a toothache remains at 0.2 regardless of what the probability
        of rain is. 

b. Hand calculation is done with chance of rain being 60%. The code has provisions for the
    probability of rain to be a randomly assigned number or 60%.

    P(Toothache | Rain) = P(Toothache && Rain) / P(Rain)

    P(Toothache && Rain) = 0.108 * 0.6 + 0.016 * 0.6 + 0.012 * 0.6 + 0.064 * 0.6
    P(Toothache && Rain) = 0.12

    P(Rain) = 0.6

    P(Toothache | Rain) = 0.12 / 0.6
    P(Toothache | Rain) = P(Toothache) = 0.2
'''
