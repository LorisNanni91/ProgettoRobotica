using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovableObjects : Objects
{
    public Sensor sensor;

    protected void MoveTodirection(float x, float z)
    {
        float y = transform.position.y;
        transform.position = new Vector3(x, y, z);
    }
  
}
