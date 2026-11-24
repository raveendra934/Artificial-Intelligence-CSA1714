
% Facts
male(john).
male(peter).
male(david).
male(robert).

female(mary).
female(lisa).
female(anna).
female(susan).

parent(john, peter).
parent(mary, peter).
parent(john, lisa).
parent(mary, lisa).

parent(peter, david).
parent(anna, david).

parent(lisa, robert).
parent(susan, robert).

% Rules
father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

brother(X, Y) :-
    male(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

sister(X, Y) :-
    female(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

uncle(X, Y) :-
    brother(X, Z),
    parent(Z, Y).

aunt(X, Y) :-
    sister(X, Z),
    parent(Z, Y).

cousin(X, Y) :-
    parent(P1, X),
    parent(P2, Y),
    brother(P1, P2).

cousin(X, Y) :-
    parent(P1, X),
    parent(P2, Y),
    sister(P1, P2).
