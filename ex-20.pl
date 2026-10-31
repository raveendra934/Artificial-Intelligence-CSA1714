
% Forward Chaining Program

% Declare dynamic predicate
:- dynamic fact/1.

% Initial Facts
fact(has_fever).
fact(has_cough).

% Rules
rule(flu) :-
    fact(has_fever),
    fact(has_cough).

rule(needs_rest) :-
    fact(flu).

rule(consult_doctor) :-
    fact(h
% FORWARD CHAINING PROGRAM

% Declare dynamic database
:- dynamic fact/1.

% Initial Facts
fact(has_fever).
fact(has_cough).

% Rules
rule(flu) :-
    fact(has_fever),
    fact(has_cough).

rule(needs_rest) :-
    fact(flu).

rule(consult_doctor) :-
    fact(has_fever),
    fact(has_cough).

% FORWARD CHAINING PROGRAM

% Declare dynamic database
:- dynamic fact/1.

% Initial Facts
fact(has_fever).
fact(has_cough).

% Rules
rule(flu) :-
    fact(has_fever),
    fact(has_cough).

rule(needs_rest) :-
    fact(flu).

rule(consult_doctor) :-
    fact(has_fever),
    fact(has_cough).

% Forward Chaining Algorithm
forward :-
    rule(X),
    \+ fact(X),
    assertz(fact(X)),
    write('New Fact Derived% FORWARD CHAINING PROGRAM

% Declare dynamic database
:- dynamic fact/1.

% Initial Facts
fact(has_fever).
fact(has_cough).

% Rules
rule(flu) :-
    fact(has_fever),
    fact(has_cough).

rule(needs_rest) :-
    fact(flu).

rule(consult_doctor) :-
    fact(has_fever),
    fact(has_cough).

% Forward Chaining Algorithm
forward :-
    rule(X),
    \+ fact(X),
    assertz(fact(X)),
    write('New Fact Derived: '),
    write(X),
    nl,
    fail.

forward :-
     write('Forward Chaining Completed.'),
    nl.

% Display all facts
display :-
    fact(X),
    write(X),
    nl,
    fail.

display.
