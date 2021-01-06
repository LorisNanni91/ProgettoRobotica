using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Sensor : MonoBehaviour
{
    public const string AGENT = "A";
    public const string OSTACLE = "W";
    public const string EMPTY = "0";
    public const string GOAL = "G";
    public const string SHEEP = "S";



}

public enum OBJECTSTYPE
{
    EMPTY,
    SHEEP,
    OBSTACLE,
    GOAL,
    DOG
}
