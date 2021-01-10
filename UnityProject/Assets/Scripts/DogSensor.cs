using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Text;
using System;

public class DogSensor : Sensor
{
    public Cell myCell;

    private void Awake()
    {
        myCell = new Cell(transform.position, OBJECTSTYPE.EMPTY);
    }

    private void OnTriggerEnter(Collider other)
    {
        myCell = new Cell(transform.position, other.GetComponent<Objects>().type);
        
    }
    private void OnTriggerExit(Collider other)
    {
        myCell = new Cell(transform.position, OBJECTSTYPE.EMPTY);
    }

}

