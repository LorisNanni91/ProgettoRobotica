hasValue("Goal",G) :- perception(G,_,_,_,_,_,_,_,_,_)
hasValue("Position 1,1",S1) :- perception(_,S1,_,_,_,_,_,_,_,_)
hasValue("Position 1,2",S2) :- perception(_,_,S2,_,_,_,_,_,_,_)
hasValue("Position 1,3",S3) :- perception(_,_,_,S3,_,_,_,_,_,_)
hasValue("Position 2,1",S4) :- perception(_,_,_,_,S4,_,_,_,_,_)
hasValue("Position 2,2",S5) :- perception(_,_,_,_,_,S5,_,_,_,_)
hasValue("Position 2,3",S6) :- perception(_,_,_,_,_,_,S6,_,_,_)
hasValue("Position 3,1",S7) :- perception(_,_,_,_,_,_,_,S7,_,_)
hasValue("Position 3,3",S8) :- perception(_,_,_,_,_,_,_,_,S8,_)
hasValue("Position 3,3",S9) :- perception(_,_,_,_,_,_,_,_,_,S9)


takeDecision("Rotate") :-
takeDecision("North") :- hasValue("Position 2,2","S"), hasValue("Goal","True")
takeDecision("South") :-
takeDecision("East") :-
takeDecision("West") :-
takeDecision("North-East") :-
takeDecision("North-West") :-
takeDecision("South-East") :-
takeDecision("South-West") :-