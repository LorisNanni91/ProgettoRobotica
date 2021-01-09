using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovableObjects : Objects
{
    [ContextMenuItem("Pass", "PassMyTurn")]

    public Sensor sensor;
    protected bool CanMove
    {
        get
        {
            return GameManager.Turn == this.type;
        }
    } 

    protected void MoveTodirection(float x, float z)
    {
        float y = transform.position.y;
        transform.position = new Vector3(x, y, z);
    }

 
    protected void PassMyTurn()
    {
        GameManager.GameManagerInstance.PassTurn(this.type);
    }
  
}
