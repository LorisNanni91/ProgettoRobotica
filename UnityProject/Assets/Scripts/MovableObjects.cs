using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovableObjects : Objects
{

    public Sensor sensor;
    protected bool CanMove
    {
        get
        {
            return GameManager.Turn == this.type;
        }
    } 


    [ContextMenu("Pass")]
    protected void PassMyTurn()
    {
        GameManager.GameManagerInstance.PassTurn(this.type);
    }
  
}
