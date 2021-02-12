using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Goal : Objects
{
    private void OnTriggerEnter(Collider other)
    {
        Objects sheep = other.GetComponent<Objects>();

        if (sheep != null && sheep.type == OBJECTSTYPE.SHEEP)
        {
            GameManager.GameManagerInstance.SendSensorMessage(MessageType.GOAL_REACHED, "una pecora in meno");

            // disable sheep
            sheep.gameObject.SetActive(false);
        }

    }
}
