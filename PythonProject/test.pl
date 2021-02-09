 lineSensor('Sensor 1,1',S1) :- perception(S1,_,_,_,_,_,_,_,_,_,_).
 lineSensor('Sensor 1,2',S2) :- perception(_,S2,_,_,_,_,_,_,_,_,_).
 lineSensor('Sensor 1,3',S3) :- perception(_,_,S3,_,_,_,_,_,_,_,_).
 lineSensor('Sensor 2,1',S4) :- perception(_,_,_,S4,_,_,_,_,_,_,_).
 lineSensor('Sensor 2,2',S5) :- perception(_,_,_,_,S5,_,_,_,_,_,_).
 lineSensor('Sensor 2,3',S6) :- perception(_,_,_,_,_,S6,_,_,_,_,_).
 lineSensor('Sensor 3,1',S7) :- perception(_,_,_,_,_,_,S7,_,_,_,_).
 lineSensor('Sensor 3,2',S8) :- perception(_,_,_,_,_,_,_,S8,_,_,_).
 lineSensor('Sensor 3,3',S9) :- perception(_,_,_,_,_,_,_,_,S9,_,_).

lateralSensor('Sensor Left', S10) :- perception(_,_,_,_,_,_,_,_,_,S10,_).
lateralSensor('Sensor Right', S11) :- perception(_,_,_,_,_,_,_,_,_,_,S11).

%V1 = ['Sensor 1,1', 'Sensor 2,1', 'Sensor 3,1'].
%V2 = ['Sensor 1,2', 'Sensor 2,2', 'Sensor 3,2'].
%V3 = ['Sensor 1,3', 'Sensor 2,3', 'Sensor 3,3'].
%
%H1 = 'Sensor 1,1', 'Sensor 1,2', 'Sensor 1,3'.
%H2 = 'Sensor 2,1', 'Sensor 2,2', 'Sensor 2,3'.
%H3 = 'Sensor 3,1', 'Sensor 3,2', 'Sensor 3,3'.


takeDecision('Forward-Left') :-  lineSensor('Sensor 1,1', 'EMPTY'),  lineSensor('Sensor 3,1', 'SHEEP'), goal('True'),!;
                                 lineSensor('Sensor 1,1', 'TARGET'),!;
                                 lineSensor('Sensor 1,1', 'EMPTY'),  lineSensor('Sensor 2,2', 'TARGET'),  lineSensor('Sensor 2,3', 'SHEEP'),!;
                                 lineSensor('Sensor 1,1', 'EMPTY'),  lineSensor('Sensor 3,2', 'TARGET'),  lineSensor('Sensor 2,3', 'SHEEP'),!.

takeDecision('Forward') :-  lineSensor('Sensor 1,2', 'EMPTY'),  lineSensor('Sensor 3,2', 'SHEEP'), goal('True'),!;
                            lineSensor('Sensor 1,2', 'TARGET'),!;
                            lineSensor('Sensor 1,2', 'EMPTY'),  lineSensor('Sensor 2,3', 'TARGET'),!;
                            lineSensor('Sensor 1,2', 'EMPTY'),  lineSensor('Sensor 2,1', 'TARGET'),!.

takeDecision('Forward-Right') :-  lineSensor('Sensor 1,3', 'EMPTY'),  lineSensor('Sensor 3,3', 'SHEEP'), goal('True'),!;
                                  lineSensor('Sensor 1,3', 'TARGET'),!;
                                  lineSensor('Sensor 1,3', 'EMPTY'),  lineSensor('Sensor 2,2', 'TARGET'),  lineSensor('Sensor 2,1', 'SHEEP'),!;
                                  lineSensor('Sensor 1,3', 'EMPTY'),  lineSensor('Sensor 3,2', 'TARGET'),  lineSensor('Sensor 2,1', 'SHEEP'),!.

takeDecision('Left') :- lateralSensor('Sensor Left', 'EMPTY'),  lineSensor('Sensor 2,1', 'SHEEP'), goal('True'),\+  lineSensor('Sensor 2,2', 'SHEEP'), \+  lineSensor(_, 'TARGET'),!;
                        lateralSensor('Sensor Left', 'EMPTY'),  lineSensor('Sensor 2,2', 'SHEEP'),  lineSensor('Sensor 2,1', 'TARGET'),!;
                        lateralSensor('Sensor Left', 'EMPTY'),  lineSensor('Sensor 2,2', 'SHEEP'),  lineSensor('Sensor 3,1', 'TARGET'), \+ lineSensor('Sensor 2,1','SHEEP'),!.

takeDecision('Right') :- lateralSensor('Sensor Right', 'EMPTY'),  lineSensor('Sensor 2,3', 'SHEEP'), goal('True'),\+  lineSensor('Sensor 2,2', 'SHEEP'), \+  lineSensor(_, 'TARGET'),!;
                         lateralSensor('Sensor Right', 'EMPTY'),  lineSensor('Sensor 2,2', 'SHEEP'),  lineSensor('Sensor 2,3', 'TARGET'),!;
                         lateralSensor('Sensor Right', 'EMPTY'),  lineSensor('Sensor 2,2', 'SHEEP'),  lineSensor('Sensor 3,3', 'TARGET'), \+ lineSensor('Sensor 2,3','SHEEP'),!.


takeDecision('Rotate-Back') :-  lineSensor('Sensor 1,1','WALL'), lineSensor('Sensor 1,2','WALL'), lineSensor('Sensor 1,3','WALL'),!.
takeDecision('Rotate-Left') :-  lineSensor(_V3, 'WALL'), \+  lineSensor(_, 'SHEEP'), \+  lineSensor(_, 'SHEEP'),!;
                               lateralSensor('Sensor Left', 'TARGET'),!;
                                lineSensor('Sensor 2,1', 'TARGET'), \+  lineSensor('Sensor 2,2', 'SHEEP'),!;
                                lineSensor('Sensor 1,1', 'TARGET'), \+  lineSensor('Sensor 2,2', 'SHEEP'),!.
takeDecision('Rotate-Right') :-  lineSensor(_V1, 'WALL'), \+  lineSensor(_, 'SHEEP'), \+  lineSensor(_, 'SHEEP'),!;
                                lateralSensor('Sensor Right', 'TARGET'),!;
                                 lineSensor('Sensor 2,3', 'TARGET'), \+  lineSensor('Sensor 2,2', 'SHEEP'),!;
                                 lineSensor('Sensor 1,3', 'TARGET'), \+  lineSensor('Sensor 2,2', 'SHEEP'),!.



takeDecision('Rotate-Left') :- \+  lineSensor(_, 'WALL').
takeDecision('Rotate-Right') :- \+  lineSensor(_, 'WALL').

takeDecision('Forward') :-  lineSensor('Sensor 1,2', 'EMPTY'),  lineSensor('Sensor 3,2', 'TARGET');
                            lineSensor('Sensor 1,2', 'EMPTY'), \+  lineSensor(_, 'TARGET'), \+  lineSensor(_, 'TARGET'), \+  lineSensor(_, 'TARGET').

takeDecision('Left') :- lateralSensor('Sensor Left', 'EMPTY'),  lineSensor('Sensor 3,2', 'TARGET');
                        lateralSensor('Sensor Left', 'EMPTY'), \+  lineSensor(_, 'TARGET'), \+  lineSensor(_, 'TARGET'), \+  lineSensor(_, 'TARGET').

takeDecision('Right') :- lateralSensor('Sensor Right', 'EMPTY'),  lineSensor('Sensor 3,2', 'TARGET');
                         lateralSensor('Sensor Right', 'EMPTY'), \+  lineSensor(_, 'TARGET'), \+  lineSensor(_, 'TARGET'), \+  lineSensor(_, 'TARGET').

takeDecision('Forward-Left') :-  lineSensor('Sensor 1,1', 'EMPTY'), \+  lineSensor(_,'TARGET'), \+  lineSensor(_, 'TARGET'), \+  lineSensor(_, 'TARGET').

takeDecision('Forward-Right') :-  lineSensor('Sensor 1,3', 'EMPTY'), \+  lineSensor(_,'TARGET'), \+  lineSensor(_, 'TARGET'), \+  lineSensor(_, 'TARGET').