'''
This file implements a Bayesian Network of the probability of
having cancer and two tests that check for cancer.

@author: lhs3
@version: Mar 7, 2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
    ])

# Compute P(Cancer | Test1 ^ Test2)
print("P(Cancer | Test1 ^ Test2)")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

# Compute P(Cancer | Test1 ^ ¬Test2)
print("\nP(Cancer | Test1 ^ ¬Test2)")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

'''
Both of these results make sense. This is because even though having cancer results in a 
positive result for both tests  90% of the time, there is still only a 1% chance a person has
cancer. Since the probability of having cancer is so low, it is far more likely that the test
just returned a false positive. This is still the case even when both tests return positive.
One failed test has a large effect of around 10-15% difference on the probability of having cancer,
even though the probability of not having cancer is still high.

P(Cancer | Test1 ^ Test2) = ɑΣP(Cancer, Test1, Test2)

ɑ < P(Cancer) * P(Test1 | Cancer) * P(Test2 | Cancer), P(¬Cancer) * P(Test1 | ¬Cancer) * P(Test2 | ¬Cancer) >
ɑ < 0.01 * 0.9 * 0.9, 0.99 * 0.2 * 0.2 >
ɑ < 0.0081, 0.0396 >

<0.17, 0.83>

P(Cancer | Test1 ^ ¬Test2)

ɑ < P(Cancer) * P(Test1 | Cancer) * P(¬Test2 | Cancer), P(¬Cancer) * P(Test1 | ¬Cancer) * P(¬Test2 | ¬Cancer) >
ɑ < 0.01 * 0.9 * 0.1, 0.99 * 0.2 * 0.8 >
ɑ < 0.0009, .1584 >

<0.00565, 0.994>

'''
