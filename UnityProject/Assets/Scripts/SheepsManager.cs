using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;

public class SheepsManager : MonoBehaviour
{
    private List<Sheep> sheeps = new List<Sheep>();

    private List<Objects> obstacles = new List<Objects>();

    [SerializeField]
    private int numberOfSheeps;

    [SerializeField]
    private GameObject prefabSheep;


    private void Awake()
    {

        List<Objects> objects = FindObjectsOfType<Objects>().ToList();
        this.obstacles = objects.FindAll(x => x.type != OBJECTSTYPE.WALL);

    }

    private void Start()
    {
        SpawnSheep();
    }

    private void SpawnSheep()
    {
        Vector3 planeSize = GameManager.GameManagerInstance.PlaneSize;


        int maxX = (int)planeSize.x;
        int maxY = (int)planeSize.z;

        int i = 0;

        while(i<numberOfSheeps)
        {

            int x = Random.Range(0, maxX);
            int z = Random.Range(0, maxY);

            Vector3 sheepPosition = new Vector3(x, 0.5f, z);

            if(!this.obstacles.Exists(n=> GameManager.IgnoreYofVector(n.transform.position) == GameManager.IgnoreYofVector(sheepPosition) ))
            {
                GameObject sheep = Instantiate(prefabSheep, sheepPosition, Quaternion.identity);

                Objects sheepObject = sheep.GetComponentInChildren<Objects>();
                obstacles.Add(sheepObject);
                sheeps.Add((Sheep)sheepObject);

                i++;

            }
 
            
        }

    }

    private void Update()
    {
        if(sheeps[0].IsSheepsTurn)
        {
            foreach (Sheep sheep in sheeps)
            {
                sheep.DoSomething();
            }

            sheeps[0].PassSheepsTurn();

        }
    }

}
