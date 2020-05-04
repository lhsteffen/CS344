/* This program creates a knowledge base for the logic used in Monty Python.
 *
 * Created by: Luke Steffen (lhs3)
 * Version: 05/03/2020
*/

weighs_as_much_as_duck(woman).

witch(X):-burn(X).
burn(X):-made_of_wood(W).
made_of_wood(Y):-floats(Y).
floats(Z):-weighs_as_much_as_duck(Z).

