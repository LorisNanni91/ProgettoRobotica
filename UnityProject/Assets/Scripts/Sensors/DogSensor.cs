using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Text;
using System;

public class DogSensor : Sensor
{
    public Cell myCell;
    //private bool collision = false;

    private void Awake()
    {
        myCell = new Cell(transform.position, OBJECTSTYPE.EMPTY);
    }

    private void OnTriggerStay(Collider other)
    {
        myCell = new Cell(transform.position, other.GetComponent<Objects>().type);

        if(other.GetComponent<Objects>().type == OBJECTSTYPE.GOAL)
        {
            GameManager.GameManagerInstance.SendPositionMessage(MessageType.GOAL_FOUND, other.transform.position);
        }

        //collision = true;

    }
    private void OnTriggerExit(Collider other)
    {
        myCell = new Cell(transform.position, OBJECTSTYPE.EMPTY);
        //collision = false;

    }

    public void OnMove()
    {
        myCell = new Cell(transform.position, OBJECTSTYPE.EMPTY);

    }


}

