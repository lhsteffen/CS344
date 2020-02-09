'''
This code presents a problem that the GPS cannot solve due to
the "prerequisite clobbers sibling" issue. In this problem, the
goal is to have money and have your kid be at school. The initial
states are your kid is at home, your car needs battery, you have money,
and you have a phone book. The solution is to repair your battery so
the car can be used to drive to school, but this means you lose money
for repairing your car. If you try to keep your money, your car cannot
drive your kid to school because it is broken. The achievement of one goal
erases the progress of another goal. Making this a problem that the GPS
cannot solve.

@author: Luke Steffen (lhs3)
@version: 02/07/2020
'''

from gps import gps


# Formulate the problem states and actions.
problem = {

    'initial': ['kid at home', 'car needs battery', 'have money', 'have phone book'],
    'goal': ['have money', 'kid at school'],

    'actions': [
        {
            'action': 'drive kid to school',
            'preconds': ['kid at home', 'car battery fixed'],
            'add': ['kid at school'],
            'delete': ['kid at home']
        },
        {
            'action': 'fix car battery',
            'preconds': ['car needs battery', 'paid mechanic', 'mechanic knows issue'],
            'add': ['car battery fixed'],
            'delete': ['car needs battery']
        },
        {
            'action': 'call mechanic',
            'preconds': ['have phone book'],
            'add': ['mechanic knows issue'],
            'delete': []
        },
        {
            'action': 'pay mechanic',
            'preconds': ['have money', 'mechanic knows issue'],
            'add': ['paid mechanic'],
            'delete': ['have money']
        }
    ]
}

if __name__ == '__main__':

    # Use GPS to solve the problem formulated above.
    actionSequence = gps(
        problem['initial'],
        problem['goal'],
        problem['actions']
    )

    # Print the solution, if there is one.
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')