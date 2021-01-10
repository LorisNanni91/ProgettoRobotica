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

public class Cell
{
    public Vector3 myPosition;
    public OBJECTSTYPE objectOnMyPosition;

    public Cell(Vector3 position, OBJECTSTYPE objType)
    {
        this.myPosition = position;
        this.objectOnMyPosition = objType;
    }

    public override string ToString()
    {
        string toString = this.myPosition.x + MessageHandler.messagePositionSeparetor 
            + this.myPosition.z + MessageHandler.messagePositionSeparetor 
            + this.objectOnMyPosition;

        return toString;
    }
}
