goal('False').
sensorLineH1('Sensor 1,1',S1) :- perception(S1,_,_,_,_,_,_,_,_).
sensorLineH1('Sensor 1,2',S2) :- perception(_,S2,_,_,_,_,_,_,_).
sensorLineH1('Sensor 1,3',S3) :- perception(_,_,S3,_,_,_,_,_,_).
sensorLineH2('Sensor 2,1',S4) :- perception(_,_,_,S4,_,_,_,_,_).
sensorLineH2('Sensor 2,2',S5) :- perception(_,_,_,_,S5,_,_,_,_).
sensorLineH2('Sensor 2,3',S6) :- perception(_,_,_,_,_,S6,_,_,_).
sensorLineH3('Sensor 3,1',S7) :- perception(_,_,_,_,_,_,S7,_,_).
sensorLineH3('Sensor 3,2',S8) :- perception(_,_,_,_,_,_,_,S8,_).
sensorLineH3('Sensor 3,3',S9) :- perception(_,_,_,_,_,_,_,_,S9).
sensorLineV1('Sensor 1,1',S1) :- perception(S1,_,_,_,_,_,_,_,_).
sensorLineV2('Sensor 1,2',S2) :- perception(_,S2,_,_,_,_,_,_,_).
sensorLineV3('Sensor 1,3',S3) :- perception(_,_,S3,_,_,_,_,_,_).
sensorLineV1('Sensor 2,1',S4) :- perception(_,_,_,S4,_,_,_,_,_).
sensorLineV2('Sensor 2,2',S5) :- perception(_,_,_,_,S5,_,_,_,_).
sensorLineV3('Sensor 2,3',S6) :- perception(_,_,_,_,_,S6,_,_,_).
sensorLineV1('Sensor 3,1',S7) :- perception(_,_,_,_,_,_,S7,_,_).
sensorLineV2('Sensor 3,2',S8) :- perception(_,_,_,_,_,_,_,S8,_).
sensorLineV3('Sensor 3,3',S9) :- perception(_,_,_,_,_,_,_,_,S9).


takeDecision('Forward').
takeDecision('Forward-Left').
takeDecision('Forward-Right').
takeDecision('Left').
takeDecision('Right').
takeDecision('Rotate-Left').
takeDecision('Rotate-Right').
takeDecision('Rotate-Back').


takeDecision('Rotate-Right') :- goal('False'), sensorLineH3(_,'WALL'); goal('False'), sensorLineH2(_,'WALL').
takeDecision('North') :- sensorLine('Sensor 1,2', 'EMPTY').
takeDecision('North-East') :- sensorLine('Sensor 1,3','EMPTY').
takeDecision('North-West') :- sensorLine('Sensor 1,1','EMPTY').
takeDecision('Rotate-Back') :- \+sensorLine( 'EMPTY').

takeDecision('North') :- sensorLine('Sensor 1,1', 'EMPTY'), \+sensorLine('Sensor 3,1','WALL'), \+sensorLine('Sensor 3,3','WALL'), \+sensorLine('Sensor 3,3','WALL').
takeDecision('Rotate-Left'):- sensorLine('Sensor 1,3','EMPTY').
takeDecision('Rotate-Back'):- sensorLine('Sensor 1,3','EMPTY').
takeDecision('North') :- sensorLine('Sensor 1,2','EMPTY'), sensorLine('Goal','False').
takeDecision('North-East') :- sensorLine('Sensor 1,3','EMPTY').
takeDecision('North-West') :- sensorLine('Sensor 1,1','EMPTY').

