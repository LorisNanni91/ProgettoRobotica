using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Text;
using System;

public class DogSensor : Sensor
{

    private void OnTriggerStay(Collider other)
    {
        //Debug.Log("tipo di oggetto: "+ other.GetComponent<Objects>().type.ToString());
    }

}

