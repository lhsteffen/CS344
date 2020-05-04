/* This program creates a knowledge base from the 1.4 exercise from Learn Prolog Now
 *
 * Created by: Luke Steffen (lhs3)
 * Version: 05/03/2020
*/

killer(butch).
married(mia, marsellus).
dead(zed).

kills(marsellus, X):-foot_massage(X, mia).
loves(mia, Y):-good_dancer(Y).
eats(julian, Z):-nutricious(Z); tasty(Z).

/* For the first three representations, I built them the way I did because the nouns of the exercise sentences (butch, mia, marsellus, and zed) are all
 * atoms which should have the ability to be referrenced in the future. The descriptiors of the nouns (killer, married, dead) are predicates because they
 * in order to ascribe attribute to an atom, Prolog requires the function-style syntax. I made the last three sentences rules because a rule is the basic
 * structure for an if-then statement. Since the last three sentences can all be rephrased as an if-then statement, it makes sense to make these rules.
 *
 * Exercise 1.5:
 * 
 * 1. True
 * 2. False
 * 3. False
 * 4. False
 * 5. True
 * 6. ron; harry
 * 7. (nothing)
 * 
 * Prolog comes up with these answers by looking firstly to see if the noun (ron, harry) is defined. If so, Prolog looks throught its knowledge base to
 * see if the right predicate has been applied to the noun already. If not, Prolog then looks through the rules to see if it can use rules to end at the
 * right predicate. If Prolog can find the right predicate or come to it, it returns True. Otherwise, it returns False. For the queries with a variable,
 * Prolog will look through all its atoms to see if that atom satisfies the predicate. If so, the query will return that variable.
 *
 * b. Prolog does implement the modus ponens. The way this is done in Prolog is by using the :- syntax. (Example: predicate(atom):-predicate2(noun2)).
 * This is known as a rule in Prolog.
 *
 * c. The Horn Clause implementation allows logical comparisions/progressions that allow for if X then Y logic. This is very helpful for defining atoms
 * based off of other predicates. Propositional logic allows the combination of multiple predicates on an atom to define another predicate of that atom
 * (Example: predicate(X) and predicate2(X)). When combined, both of these allow for powerful logic comparisons and if then statements (Example: if 
 * predicate(X) and predicate2(X) then predicate3(X)). This allows for many powerful logical statements.
 *
 * d. Prolog does differentiate between TELL and ASK. TELL is defined in the pl file which defines predicates and rules. When running a Prolog file, the
 * -? prompt represents the ASK function, which is known as a query.
*/




