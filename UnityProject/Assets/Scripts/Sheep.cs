using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Sheep : MovableObjects
{
   private SheepSensor sheepSensor;

    public bool IsSheepsTurn
    {
        get
        {
            return this.CanMove;
        }
    }


    private void Start()
    {
        sheepSensor = (SheepSensor)this.sensor;

    }

    public void DoSomething()
    {
        if (this.sheepSensor.MustMove() && this.CanMove)
        {
            MoveTodirection(sheepSensor.nextPosition);
            this.sheepSensor.MoveDone();
        }
  
    }

    public void PassSheepsTurn()
    {
        this.PassMyTurn();
    }

    private void MoveTodirection(Vector3 newPosition)
    {
        transform.position = newPosition;
    }
}
