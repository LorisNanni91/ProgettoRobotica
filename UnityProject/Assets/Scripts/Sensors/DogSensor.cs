using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Text;
using System;

public class DogSensor : Sensor
{
    public Cell myCell;
    protected static bool goalFound = false;

    private void Awake()
    {
        myCell = new Cell(transform.position, OBJECTSTYPE.EMPTY);
    }

    private void OnTriggerStay(Collider other)
    {
        myCell = new Cell(transform.position, other.GetComponent<Objects>().type);

        if(!goalFound && other.GetComponent<Objects>().type == OBJECTSTYPE.GOAL)
        {
            GameManager.GameManagerInstance.SendPositionMessage(MessageType.GOAL_FOUND, other.transform.position);
            goalFound = true;
        }

    }
    private void OnTriggerExit(Collider other)
    {
        myCell = new Cell(transform.position, OBJECTSTYPE.EMPTY);

    }

    public void OnMove()
    {
        myCell = new Cell(transform.position, OBJECTSTYPE.EMPTY);

    }


}

