/* This file does the two LPN! exercises from lab 13. 
 *
 * Author: Luke Steffen (lhs3)
 * Version: 05/10/2020
*/

/* a. Exercise 3.2: */

directly_in(katarina, olga).
directly_in(olga, natasha).
directly_in(natasha, irina).

in(X, Y) :- directly_in(X, Y).
in(X,Y) :- directly_in(X, Z), in(Z, Y).


/* Exercise 4.5 */

tran(eins, one).
tran(zwei, two).
tran(drei, three).
tran(vier, four).
tran(fuenf, five).
tran(sechs, six).
tran(sieben, seven).
tran(acht, eight).
tran(neun, nine).

listtran([], []).
listtran([Gh | Gt], [Eh | Et]) :- tran(Gh, Eh), listtran(Gt, Et).