using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SheepSensor : Sensor
{
    private bool mustMove = false;
    public Vector3 nextPosition;
    private void OnTriggerEnter(Collider other)
    {

        MovableObjects movableObjects = other.GetComponent<MovableObjects>();

        if(movableObjects != null && movableObjects.type == OBJECTSTYPE.DOG)
        {
            mustMove = true;
            float previousY = transform.position.y;
            Vector3 delta = transform.position - other.transform.position;
            nextPosition = transform.position + delta;
            nextPosition.y = previousY;
        }
    }


    public void MoveDone()
    {
        mustMove = false;
    }

    public bool MustMove ()
    {
        return this.mustMove;
    }

}
