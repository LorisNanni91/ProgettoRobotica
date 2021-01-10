using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Dog : MovableObjects
{
    private DogSensorManager dogSensor;
    private int movesCounter = 0;

    private void Start()
    {
        dogSensor = (DogSensorManager)sensor;
        Debug.Log("DOG POSITION " + transform.position);
    }

    private void ReceiveIstruction(string message)
    {
        switch(message)
        {
            case Actions.ROTATE:
                break;
            case Actions.NORTH:
                break;
            case Actions.SOUTH:
                break;
            case Actions.EAST:
                break;
            case Actions.WEST:
                break;
            case Actions.NORTH_EAST:
                break;
            case Actions.NORTH_WEST:
                break;
            case Actions.SOUTH_EAST:
                break;
            case Actions.SOUTH_WEST:
                break;

            default:
                Debug.LogError("DOG RECEIVED INVALID ACTION");

                break;
             
        }

    }
}

public static class Actions
{
    public const string ROTATE = "Rotate";
    public const string NORTH = "North";
    public const string SOUTH = "South";
    public const string EAST = "East";
    public const string WEST = "West";

    public const string NORTH_EAST = "North-East";
    public const string NORTH_WEST = "North-West";
    public const string SOUTH_EAST = "South-East";
    public const string SOUTH_WEST = "South-West";


    //takeDecision("Rotate") :-
    //takeDecision("North") :-
    //takeDecision("South") :-
    //takeDecision("East") :-
    //takeDecision("West") :-
    //takeDecision("North-East") :-
    //takeDecision("North-West") :-
    //takeDecision("South-East") :-
    //takeDecision("South-West") :-
}
