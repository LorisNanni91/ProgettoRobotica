using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Text;
using System;

public class DogSensor : MonoBehaviour
{


    private void OnTriggerStay(Collider other)
    {
        Debug.Log("tipo di oggetto: "+ other.GetComponent<Objects>().type.ToString());
    }

}

public enum OBJECTSTYPE
{
    EMPTY,
    SHEEP,
    OBSTACLE,
    GOAL
}
