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

    protected void MoveTodirection(Vector3 newPosition)
    {
        transform.position = newPosition;
    }

 
    protected void PassMyTurn()
    {
        GameManager.GameManagerInstance.PassTurn(this.type);
    }
  
}
