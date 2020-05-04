/* This program creates a knowledge base from the 2.1 & 2.2 exercises from Learn Prolog Now
 *
 * Created by: Luke Steffen (lhs3)
 * Version: 05/03/2020
*/

/*
 * a. Exercise 2.1:
 *     1. yes
 *     2. no
 *     8. yes
 *     9. yes
 *     14. yes
 *
 *    Exercise 2.2:
 *      Queries 1, 4, and 5 are all satisfied. Queries 1 and 4 return True while query 5 returns dobby, hermoine, 'McGonagal', and rita_skeeter
 *
 *      Prolog does its unification and reasoning first by searching the knowledge database to find a term or head of rule to match to. Once it
 *      has found a matching rule, it unifies the variable in the query with the variable in the term or head of rule by created a new shared
 *      variable that points to both variables. Prolog then replaces the original queries with the definition provided by the rule it unified
 *      with. After, Prolog will then go through each atom and set it equal to the shared variable it created earlier to see if it matches all
 *      conditions needed. If so, Prolog will return that variable.
 *
 * b. Inference in propositonal logic does use unification. The most basic for of propositional logic is if both P and P->Q hold, then Q can be
 * concluded. This idea is essentially the same as unification which states that two variables can be unified if the result of these variables are
 * the same. While not exactly the same, inference does use unification in the sense that because P->Q and P exists, P is essentially Q, or unified
 * with Q.
 *
 * c. Prolog inference uses resolution. Resolution is essentially applying each variable to the formula to see if the formula is correct or incorrect.
 * Prolog infers by taking every atom and applying it to the term to see if it can unify with a variable, which is resolution.
*/