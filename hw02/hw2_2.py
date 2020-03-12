'''
This file creates a Bayesian Network and solves probabilities given
in the second question of homework 2 for CS-344: Artificial Intelligence.

@author: lhs3
@version: Mar 10, 2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T = True
F = False

cloudy = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.1, F: 0.5}),
    ('Rain', 'Cloudy', {T: 0.8, F: 0.2}),
    ('WetGrass', 'Rain Sprinkler', {(T, T): 0.99, (T, F): 0.9, (F, T): 0.9, (F, F): 0.0})
])

# Compute P(Cloudy)
print("P(Cloudy)")
print(enumeration_ask('Cloudy', dict(), cloudy).show_approx())

# Compute P(Sprinkler | Cloudy)
print("\nP(Sprinkler | Cloudy)")
print(enumeration_ask('Sprinkler', dict(Cloudy=T), cloudy).show_approx())

# Compute P(Cloudy | Sprinkler ^ Not Rain)
print("\nP(Cloudy | Sprinkler ^ Not Rain)")
print(enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), cloudy).show_approx())

# Compute P(WetGrass | Cloudy ^ Sprinkler ^ Rain)
print("\nP(WetGrass | Cloudy ^ Sprinkler ^ Rain)")
print(enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), cloudy).show_approx())

# Compute P(Cloudy | Not WetGrass)
print("\nP(Cloudy | Not WetGrass)")
print(enumeration_ask('Cloudy', dict(WetGrass=F), cloudy).show_approx())

'''
c. Based on the following representation of the Bayesian Network, there are 2 pairs
   of independent variables, sprinkler and rain, and Cloudy and WetGrass.
   
d. P(Cloudy) = <0.5, 0.5> (Given)

   P(Sprinkler | Cloudy) = <0.1, 0.9> (Given)
   
   P(Cloudy | Sprinkler ^ Not Rain) = alpha * (P(Sprinkler ^ Not Rain) * P(Cloudy))
   P(Cloudy | Sprinkler ^ Not Rain) = alpha * (0.1 * 0.8 * 0.5)
   P(Cloudy | Sprinkler ^ Not Rain) = alpha * 0.04
   P(Cloudy | Sprinkler ^ Not Rain) = <0.0476, 0.952>
   
   P(WetGrass | Cloudy ^ Sprinkler ^ Rain) = P(WetGrass | Sprinkler ^ Rain)
   P(WetGrass | Cloudy ^ Sprinkler ^ Rain) = <0.99, 0.01> (Given)
   This is because Cloudy has no effect on WetGrass, only Sprinkler and Rain
   have an effect. This is because Cloudy and WetGrass are independent.
   
   P(Cloudy | Not WetGrass)
   This portion shows a visual representation of the binary tree used to solve this
   problem. The tree is split into two subsections, the probability of it being cloudy
   and the probability of it not being cloudy. The numbers are multiplied down to each
   leaf, then summed to find the total probability.
   

                                                  P(C)
                                ___________________|______________________
                               /                                          \
                              /                                            \
                             /                                              \
                            /                                                \
                           /                                                  \
                    P(S | C) = 0.1                                    P(¬S | C) = 0.9
                   /             \                                   /                \
                  /               \                                 /                  \
                 /                 \                               /                    \
                /                   \                             /                      \
               /                     \                           /                        \
              /                       \                         /                          \
      P(R | S, C) = 0.8        P(¬R | S, C) = 0.2        P(R | ¬S, C) = 0.8        P(¬R | ¬S, C) = 0.2
             |                        |                         |                          |
             |                        |                         |                          |
   P(¬W | R, S, C) = 0.01    P(¬W | ¬R, S, C) = 0.1    P(¬W | R, ¬S, C) = 0.1    P(¬W | ¬R, ¬S, C) = 1.0
   
   
   P(C) = (0.1 * 0.8 * 0.01) + (0.1 * 0.2 * 0.1) + (0.9 * 0.8 * 0.1) + (0.9 * 0.2 * 1.0) = 0.2548 * alpha
   
   
                                                P(¬C)
                                ___________________|______________________
                               /                                          \
                              /                                            \
                             /                                              \
                            /                                                \
                           /                                                  \
                    P(S | ¬C) = 0.5                                   P(¬S | ¬C) = 0.5
                   /             \                                   /                \
                  /               \                                 /                  \
                 /                 \                               /                    \
                /                   \                             /                      \
               /                     \                           /                        \
              /                       \                         /                          \
      P(R | S, ¬C) = 0.2       P(¬R | S, ¬C) = 0.8        P(R | ¬S, ¬C) = 0.2        P(¬R | ¬S, ¬C) = 0.8
             |                        |                         |                          |
             |                        |                         |                          |
   P(¬W | R, S, ¬C) = 0.01   P(¬W | ¬R, S, ¬C) = 0.1    P(¬W | R, ¬S, ¬C) = 0.1    P(¬W | ¬R, ¬S, ¬C) = 1.0
   
   
   P(¬C) = (0.5 * 0.2 * 0.01) + (0.5 * 0.8 * 0.1) + (0.5 * 0.2 * 0.1) + (0.5 * 0.8 * 1.0) = 0.451 * alpha
   
   P(Cloudy | ¬WetGrass) = alpha <0.2548, 0.451>
   
   alpha = 1 / (0.2548 + 0.451) = 1.4168
   
   P(Cloudy | ¬WetGrass) = <0.361, 0.639>
'''
