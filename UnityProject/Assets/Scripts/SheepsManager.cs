using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SheepsManager : MonoBehaviour
{
    private Sheep[] sheeps;

    private void Awake()
    {
        sheeps = FindObjectsOfType<Sheep>();
    }

    private void Update()
    {
        if(sheeps[0].IsSheepsTurn)
        {
            foreach(Sheep sheep in sheeps)
            {
                sheep.DoSomething();
            }

            sheeps[0].PassSheepsTurn();

        }
    }
}
