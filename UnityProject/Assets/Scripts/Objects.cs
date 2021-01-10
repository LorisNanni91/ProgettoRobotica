using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Objects : MonoBehaviour
{
    public OBJECTSTYPE type;
}

public enum OBJECTSTYPE
{
    EMPTY,
    SHEEP,
    OBSTACLE,
    GOAL,
    DOG
}
