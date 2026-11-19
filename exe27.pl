
% Fruit and its Colour using Backtracking

% Facts
fruit(apple, red).
fruit(banana, yellow).
fruit(mango, yellow).
fruit(orange, orange).
fruit(grapes, green).
fruit(guava, green).
fruit(strawberry, red).

% Display fruits and colours
find_fruit :-
    fruit(F, C),
    write('Fruit: '),
    write(F),
    write(' Colour: '),
    write(C),
    nl,
    fail.

find_fruit.
