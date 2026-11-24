% Rules
gains_knowledge(X) :-
    studies(X).

passes_exam(X) :-
    gains_knowledge(X).

% Fact
studies(ravi).

% Query
% ?- passes_exam(ravi).
