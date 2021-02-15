lineSensor('Sensor 1,1',S1) :- perception(S1,_,_,_,_,_,_,_,_,_,_).
lineSensor('Sensor 1,2',S2) :- perception(_,S2,_,_,_,_,_,_,_,_,_).
lineSensor('Sensor 1,3',S3) :- perception(_,_,S3,_,_,_,_,_,_,_,_).
lineSensor('Sensor 2,1',S4) :- perception(_,_,_,S4,_,_,_,_,_,_,_).
lineSensor('Sensor 2,2',S5) :- perception(_,_,_,_,S5,_,_,_,_,_,_).
lineSensor('Sensor 2,3',S6) :- perception(_,_,_,_,_,S6,_,_,_,_,_).
lineSensor('Sensor 3,1',S7) :- perception(_,_,_,_,_,_,S7,_,_,_,_).
lineSensor('Sensor 3,2',S8) :- perception(_,_,_,_,_,_,_,S8,_,_,_).
lineSensor('Sensor 3,3',S9) :- perception(_,_,_,_,_,_,_,_,S9,_,_).

lineSensorH1('Sensor 1,1',S1) :- perception(S1,_,_,_,_,_,_,_,_,_,_).
lineSensorH1('Sensor 1,2',S2) :- perception(_,S2,_,_,_,_,_,_,_,_,_).
lineSensorH1('Sensor 1,3',S3) :- perception(_,_,S3,_,_,_,_,_,_,_,_).
lineSensorH2('Sensor 2,1',S4) :- perception(_,_,_,S4,_,_,_,_,_,_,_).
lineSensorH2('Sensor 2,2',S5) :- perception(_,_,_,_,S5,_,_,_,_,_,_).
lineSensorH2('Sensor 2,3',S6) :- perception(_,_,_,_,_,S6,_,_,_,_,_).
lineSensorH3('Sensor 3,1',S7) :- perception(_,_,_,_,_,_,S7,_,_,_,_).
lineSensorH3('Sensor 3,2',S8) :- perception(_,_,_,_,_,_,_,S8,_,_,_).
lineSensorH3('Sensor 3,3',S9) :- perception(_,_,_,_,_,_,_,_,S9,_,_).

lineSensorV1('Sensor 1,1',S1) :- perception(S1,_,_,_,_,_,_,_,_,_,_).
lineSensorV1('Sensor 2,1',S4) :- perception(_,_,_,S4,_,_,_,_,_,_,_).
lineSensorV1('Sensor 3,1',S7) :- perception(_,_,_,_,_,_,S7,_,_,_,_).
lineSensorV2('Sensor 1,2',S2) :- perception(_,S2,_,_,_,_,_,_,_,_,_).
lineSensorV2('Sensor 2,2',S5) :- perception(_,_,_,_,S5,_,_,_,_,_,_).
lineSensorV2('Sensor 3,2',S8) :- perception(_,_,_,_,_,_,_,S8,_,_,_).
lineSensorV3('Sensor 1,3',S3) :- perception(_,_,S3,_,_,_,_,_,_,_,_).
lineSensorV3('Sensor 2,3',S6) :- perception(_,_,_,_,_,S6,_,_,_,_,_).
lineSensorV3('Sensor 3,3',S9) :- perception(_,_,_,_,_,_,_,_,S9,_,_).

lateralSensor('Sensor Left', S10) :- perception(_,_,_,_,_,_,_,_,_,S10,_).
lateralSensor('Sensor Right', S11) :- perception(_,_,_,_,_,_,_,_,_,_,S11).


takeDecision('Rotate-Back') :- lineSensor('Sensor 1,1','WALL'),lineSensor('Sensor 1,2','WALL'),lineSensor('Sensor 1,3','WALL'),!.

takeDecision('Rotate-Left') :- lateralSensor('Sensor Left', 'TARGET'),!.

takeDecision('Rotate-Right') :- lateralSensor('Sensor Right', 'TARGET'),!.

takeDecision('Forward-Left') :- lineSensor('Sensor 1,1', 'EMPTY'), lineSensor('Sensor 3,1', 'SHEEP'), goal('True'),!;
                                lineSensor('Sensor 1,1', 'TARGET'),!;
                                lineSensor('Sensor 1,1', 'EMPTY'), lineSensor('Sensor 2,2', 'TARGET'), lineSensor('Sensor 2,3', 'SHEEP'),!;
                                lineSensor('Sensor 1,1', 'EMPTY'), lineSensor('Sensor 3,2', 'TARGET'), lineSensor('Sensor 2,3', 'SHEEP'),!;
                                \+ lateralSensor('Sensor Left', 'EMPTY'), lineSensor('Sensor 1,1', 'EMPTY'), lineSensor('Sensor 2,2', 'SHEEP'), lineSensor('Sensor 2,1', 'TARGET'),!;
                                \+ lateralSensor('Sensor Left', 'EMPTY'), lineSensor('Sensor 1,1', 'EMPTY'), lineSensor('Sensor 2,2', 'SHEEP'), lineSensor(_, 'TARGET'),!;
                                lineSensor('Sensor 1,1', 'EMPTY'), \+ lineSensor('Sensor 1,2', 'EMPTY'), lineSensor('Sensor 2,2', 'TARGET'), \+ lineSensorH1(_, 'SHEEP'),!;
                                lineSensor('Sensor 1,1', 'EMPTY'), lineSensor('Sensor 2,3', 'SHEEP'), lineSensor('Sensor 3,3', 'TARGET'), !.

takeDecision('Forward') :- lineSensor('Sensor 1,2', 'EMPTY'), lineSensor('Sensor 3,2', 'SHEEP'), goal('True'),!;
                           lineSensor('Sensor 1,2', 'TARGET'),!;
                           lineSensor('Sensor 1,2', 'EMPTY'), lineSensor('Sensor 2,1', 'TARGET'), \+ lineSensor(_, 'SHEEP'),!;
                           lineSensor('Sensor 1,2', 'EMPTY'), lineSensor('Sensor 2,3', 'TARGET'), \+ lineSensor(_, 'SHEEP'),!;
                           lineSensor('Sensor 1,2', 'EMPTY'), lineSensor('Sensor 2,2', 'TARGET'), \+ lineSensorH1(_, 'SHEEP').

takeDecision('Forward-Right') :- lineSensor('Sensor 1,3', 'EMPTY'), lineSensor('Sensor 3,3', 'SHEEP'), goal('True'),!;
                                 lineSensor('Sensor 1,3', 'TARGET'),!;
                                 lineSensor('Sensor 1,3', 'EMPTY'), lineSensor('Sensor 2,2', 'TARGET'), lineSensor('Sensor 2,1', 'SHEEP'),!;
                                 lineSensor('Sensor 1,3', 'EMPTY'), lineSensor('Sensor 3,2', 'TARGET'), lineSensor('Sensor 2,1', 'SHEEP'),!;
                                 \+ lateralSensor('Sensor Right', 'EMPTY'), lineSensor('Sensor 1,3', 'EMPTY'), lineSensor('Sensor 2,2', 'SHEEP'), lineSensor('Sensor 2,1', 'TARGET'),!;
                                \+ lateralSensor('Sensor Right', 'EMPTY'), lineSensor('Sensor 1,3', 'EMPTY'), lineSensor('Sensor 2,2', 'SHEEP'), lineSensor(_, 'TARGET'),!;
                                lineSensor('Sensor 1,3', 'EMPTY'), \+ lineSensor('Sensor 1,2', 'EMPTY'), lineSensor('Sensor 2,2', 'TARGET'), \+ lineSensorH1(_, 'SHEEP'),!;
                                lineSensor('Sensor 1,3', 'EMPTY'), lineSensor('Sensor 2,1', 'SHEEP'), lineSensor('Sensor 3,1', 'TARGET'), !.

takeDecision('Left') :- lateralSensor('Sensor Left', 'EMPTY'), lineSensor('Sensor 2,1', 'SHEEP'), goal('True'),\+ lineSensor('Sensor 2,2', 'SHEEP'), \+ lineSensor(_,'TARGET'),!;
                        lateralSensor('Sensor Left', 'EMPTY'), lineSensor(_, 'SHEEP'), lineSensor('Sensor 2,1', 'TARGET'),!;
                        lateralSensor('Sensor Left', 'EMPTY'), lineSensor(_, 'SHEEP'), lineSensor('Sensor 3,1', 'TARGET'),!.

takeDecision('Right') :- lateralSensor('Sensor Right', 'EMPTY'), lineSensor('Sensor 2,3', 'SHEEP'), goal('True'),\+ lineSensor('Sensor 2,2', 'SHEEP'),  \+ lineSensor(_,'TARGET'), !;
                         lateralSensor('Sensor Right', 'EMPTY'), lineSensor(_, 'SHEEP'), lineSensor('Sensor 2,3', 'TARGET'),!;
                         lateralSensor('Sensor Right', 'EMPTY'), lineSensor(_, 'SHEEP'), lineSensor('Sensor 3,3', 'TARGET'),!.



takeDecision('Rotate-Left') :- \+ lineSensorV1(_, 'WALL'), \+ lineSensor(_, 'TARGET').
takeDecision('Rotate-Right') :- \+ lineSensorV3(_, 'WALL'), \+ lineSensor(_, 'TARGET').
takeDecision('Rotate-Back') :- \+ lineSensor(_, 'SHEEP'), \+ lineSensor(_, 'TARGET').

takeDecision('Forward') :- lineSensor('Sensor 1,2', 'EMPTY'), lineSensor('Sensor 3,2', 'TARGET');
                           lineSensor('Sensor 1,2', 'EMPTY').

takeDecision('Left') :- lateralSensor('Sensor Left', 'EMPTY'), lineSensor('Sensor 3,2', 'TARGET');
                        lateralSensor('Sensor Left', 'EMPTY').

takeDecision('Right') :- lateralSensor('Sensor Right', 'EMPTY'), lineSensor('Sensor 3,2', 'TARGET');
                         lateralSensor('Sensor Right', 'EMPTY').

takeDecision('Forward-Left') :- lineSensor('Sensor 1,1', 'EMPTY').

takeDecision('Forward-Right') :- lineSensor('Sensor 1,3', 'EMPTY').





