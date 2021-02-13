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

%V1 = 'Sensor 1,1', 'Sensor 2,1', 'Sensor 3,1'.
%V2 = 'Sensor 1,2', 'Sensor 2,2', 'Sensor 3,2'.
%V3 = 'Sensor 1,3', 'Sensor 2,3', 'Sensor 3,3'.
%
%H1 = 'Sensor 1,1', 'Sensor 1,2', 'Sensor 1,3'.
%H2 = 'Sensor 2,1', 'Sensor 2,2', 'Sensor 2,3'.
%H3 = 'Sensor 3,1', 'Sensor 3,2', 'Sensor 3,3'.


takeDecision('Forward-Left') :- lineSensorH1('Sensor 1,1', 'EMPTY'), lineSensorH3('Sensor 3,1', 'SHEEP'), goal('True'),!;
                                lineSensorH1('Sensor 1,1', 'TARGET'),!;
                                lineSensorH1('Sensor 1,1', 'EMPTY'), lineSensorH2('Sensor 2,2', 'TARGET'), lineSensorH2('Sensor 2,3', 'SHEEP'),!;
                                lineSensorH1('Sensor 1,1', 'EMPTY'), lineSensorH3('Sensor 3,2', 'TARGET'), lineSensorH2('Sensor 2,3', 'SHEEP'),!.

takeDecision('Forward') :- lineSensorH1('Sensor 1,2', 'EMPTY'), lineSensorH3('Sensor 3,2', 'SHEEP'), goal('True'),!;
                           lineSensorH1('Sensor 1,2', 'TARGET'),!;
                           lineSensorH1('Sensor 1,2', 'EMPTY'), lineSensorH2('Sensor 2,3', 'TARGET'),!;
                           lineSensorH1('Sensor 1,2', 'EMPTY'), lineSensorH2('Sensor 2,1', 'TARGET'),!.

takeDecision('Forward-Right') :- lineSensorH1('Sensor 1,3', 'EMPTY'), lineSensorH3('Sensor 3,3', 'SHEEP'), goal('True'),!;
                                 lineSensorH1('Sensor 1,3', 'TARGET'),!;
                                 lineSensorH1('Sensor 1,3', 'EMPTY'), lineSensorH2('Sensor 2,2', 'TARGET'), lineSensorH2('Sensor 2,1', 'SHEEP'),!;
                                 lineSensorH1('Sensor 1,3', 'EMPTY'), lineSensorH3('Sensor 3,2', 'TARGET'), lineSensorH2('Sensor 2,1', 'SHEEP'),!.

takeDecision('Left') :- lateralSensor('Sensor Left', 'EMPTY'), lineSensorH2('Sensor 2,1', 'SHEEP'), goal('True'),\+ lineSensorH2('Sensor 2,2', 'SHEEP'), \+ lineSensorV2(_, 'TARGET'),!;
                        lateralSensor('Sensor Left', 'EMPTY'), lineSensorH2('Sensor 2,2', 'SHEEP'), lineSensorH2('Sensor 2,1', 'TARGET'),!;
                        lateralSensor('Sensor Left', 'EMPTY'), lineSensorH2('Sensor 2,2', 'SHEEP'), lineSensorH3('Sensor 3,1', 'TARGET'),!.

takeDecision('Right') :- lateralSensor('Sensor Right', 'EMPTY'), lineSensorH2('Sensor 2,3', 'SHEEP'), goal('True'),\+ lineSensorH2('Sensor 2,2', 'SHEEP'), \+ lineSensorV1(_, 'TARGET'),!;
                         lateralSensor('Sensor Right', 'EMPTY'), lineSensorH2('Sensor 2,2', 'SHEEP'), lineSensorH2('Sensor 2,3', 'TARGET'),!;
                         lateralSensor('Sensor Right', 'EMPTY'), lineSensorH2('Sensor 2,2', 'SHEEP'), lineSensorH3('Sensor 3,3', 'TARGET'),!.


takeDecision('Rotate-Back') :- lineSensorH1('Sensor 1,1','WALL'),lineSensorH1('Sensor 1,2','WALL'),lineSensorH1('Sensor 1,3','WALL'),!.
takeDecision('Rotate-Left') :- lateralSensor('Sensor Left', 'TARGET'),!;
                               lineSensorH2('Sensor 2,1', 'TARGET'), \+ lineSensorH2('Sensor 2,2', 'SHEEP'),!;
                               lineSensorH1('Sensor 1,1', 'TARGET'), \+ lineSensorH2('Sensor 2,2', 'SHEEP'),!.

takeDecision('Rotate-Right') :- lateralSensor('Sensor Right', 'TARGET'),!;
                                lineSensorH2('Sensor 2,3', 'TARGET'), \+ lineSensorH2('Sensor 2,2', 'SHEEP'),!;
                                lineSensorH1('Sensor 1,3', 'TARGET'), \+ lineSensorH2('Sensor 2,2', 'SHEEP'),!.



takeDecision('Rotate-Left') :- \+ lineSensorV1(_, 'WALL').
takeDecision('Rotate-Right') :- \+ lineSensorV3(_, 'WALL').

takeDecision('Forward') :- lineSensorH1('Sensor 1,2', 'EMPTY'), lineSensorH3('Sensor 3,2', 'TARGET');
                           lineSensorH1('Sensor 1,2', 'EMPTY'), \+ lineSensorH1(_, 'TARGET'), \+ lineSensorH2(_, 'TARGET'), \+ lineSensorH1(_, 'TARGET').

takeDecision('Left') :- lateralSensor('Sensor Left', 'EMPTY'), lineSensorH3('Sensor 3,2', 'TARGET');
                        lateralSensor('Sensor Left', 'EMPTY'), \+ lineSensorH1(_, 'TARGET'), \+ lineSensorH2(_, 'TARGET'), \+ lineSensorH1(_, 'TARGET').

takeDecision('Right') :- lateralSensor('Sensor Right', 'EMPTY'), lineSensorH3('Sensor 3,2', 'TARGET');
                         lateralSensor('Sensor Right', 'EMPTY'), \+ lineSensorH1(_, 'TARGET'), \+ lineSensorH2(_, 'TARGET'), \+ lineSensorH1(_, 'TARGET').

takeDecision('Forward-Left') :- lineSensorH1('Sensor 1,1', 'EMPTY'), \+ lineSensorH1(_, 'TARGET'), \+ lineSensorH2(_, 'TARGET'), \+ lineSensorH1(_, 'TARGET').

takeDecision('Forward-Right') :- lineSensorH1('Sensor 1,3', 'EMPTY'), \+ lineSensorH1(_, 'TARGET'), \+ lineSensorH2(_, 'TARGET'), \+ lineSensorH1(_, 'TARGET').





