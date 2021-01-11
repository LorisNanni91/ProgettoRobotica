using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SheepSensor : Sensor
{
    private bool mustMove = false;
    public Vector3 nextPosition;
    private List<GameObject> obstacles = new List<GameObject>();
    private void OnTriggerEnter(Collider other)
    {

        Objects Object = other.GetComponent<Objects>();

        if(Object != null)
        {

            if (Object.type == OBJECTSTYPE.OBSTACLE)
            {
                this.obstacles.Add(other.gameObject);
            }

            if (Object.type == OBJECTSTYPE.DOG)
            {
                mustMove = true;
                float previousY = transform.position.y;
                Vector3 delta = transform.position - other.transform.position;
                this.nextPosition = transform.position + delta;
                this.nextPosition.y = previousY;
                CheckObstacles(other.transform.position,delta);
            }

        }


    }

    private void CheckObstacles(Vector3 dogPosition,Vector3 delta)
    {

        Debug.Log("Delta " + delta);

        foreach(GameObject obstacle in this.obstacles)
        {
            if(IgnoreYofVector(obstacle.transform.position) == IgnoreYofVector(this.nextPosition))
            {
                Vector3 obstacleDelta = obstacle.transform.position - transform.position;

                Debug.Log("Obstacle at " + obstacle.transform.position+" Name: "+obstacle.name+ "Obstacle delta " + obstacleDelta + "current next position "+this.nextPosition);

                // calculate alternative position



            }
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

    private Vector3 IgnoreYofVector(Vector3 a)
    {
        return Vector3.Scale(a,new Vector3(1,0,1));
    }


}
