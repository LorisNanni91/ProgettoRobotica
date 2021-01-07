using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Sheep : MovableObjects
{
   private SheepSensor sheepSensor;

    private void Start()
    {
        sheepSensor = (SheepSensor)this.sensor;

    }

    private void Update()
    {
        if (sheepSensor.MustMove())
        {
            MoveTodirection(sheepSensor.nextPosition.x,sheepSensor.nextPosition.z);
        }
    }
}
