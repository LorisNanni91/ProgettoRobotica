hasValue('Goal',G) :- perception(G,_,_,_,_,_,_,_,_,_).
hasValue('Sensor 1,1',S1) :- perception(_,S1,_,_,_,_,_,_,_,_).
hasValue('Sensor 1,2',S2) :- perception(_,_,S2,_,_,_,_,_,_,_).
hasValue('Sensor 1,3',S3) :- perception(_,_,_,S3,_,_,_,_,_,_).
hasValue('Sensor 2,1',S4) :- perception(_,_,_,_,S4,_,_,_,_,_).
hasValue('Sensor 2,2',S5) :- perception(_,_,_,_,_,S5,_,_,_,_).
hasValue('Sensor 2,3',S6) :- perception(_,_,_,_,_,_,S6,_,_,_).
hasValue('Sensor 3,1',S7) :- perception(_,_,_,_,_,_,_,S7,_,_).
hasValue('Sensor 3,3',S8) :- perception(_,_,_,_,_,_,_,_,S8,_).
hasValue('Sensor 3,3',S9) :- perception(_,_,_,_,_,_,_,_,_,S9).


takeDecision('Rotate-Right') :- hasValue('Sensor 1,3','SHEEP').
takeDecision('Rotate-Left'):- hasValue('Sensor 1,3','EMPTY').
takeDecision('Rotate-Back'):- hasValue('Sensor 1,3','EMPTY').
takeDecision('North') :- hasValue('Sensor 1,2','EMPTY'), hasValue('Sensor 2,2','SHEEP'), hasValue('Goal','True').
takeDecision('North-East') :- hasValue('Sensor 1,3','EMPTY').
takeDecision('North-West') :- hasValue('Sensor 1,1','EMPTY').

