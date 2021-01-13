using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SheepSensor : Sensor
{
    private bool mustMove = false;
    private bool nextPositionEmpty = false;
    public Vector3 nextPosition;

    private List<Objects> obstacles = new List<Objects>();
    private bool NearWall
    {
        get
        {
            return this.obstacles.Exists(x=>x.type==OBJECTSTYPE.WALL);
        }
    }

    #region UnityMethod
    private void OnTriggerEnter(Collider other)
    {

        Objects obstalce = other.GetComponent<Objects>();

        if(obstalce != null)
        {
            this.obstacles.Add(obstalce);

            if (obstalce.type == OBJECTSTYPE.DOG)
            {
                RunAwayFromDog(obstalce);
            }

        }


    }

    private void OnTriggerExit(Collider other)
    {
        Objects obstacle = other.GetComponent<Objects>();
        this.obstacles.Remove(obstacle);
    }

    #endregion

    private void RunAwayFromDog(Objects dog)
    {
        mustMove = true;
        float previousY = transform.position.y;
        Vector3 delta = transform.position - dog.transform.position;
        this.nextPosition = transform.position + delta;
        this.nextPosition.y = previousY;
        RecalculatePosition();
    }

    private void RecalculatePosition()
    {
        if(this.NearWall)
        {
            // Make like billiards
            Rect rect = new Rect(0, 0, 2, 2);

            rect.center = new Vector2(transform.position.x, transform.position.z);

            Vector3[] anglesOfRect = new Vector3[4];

            anglesOfRect[0] = new Vector3(rect.xMin, 0, rect.yMin);
            anglesOfRect[1] = new Vector3(rect.xMin, 0, rect.yMax);
            anglesOfRect[2] = new Vector3(rect.xMax, 0, rect.yMin);
            anglesOfRect[3] = new Vector3(rect.xMax, 0, rect.yMax);

            for (int i = 0; i < anglesOfRect.Length && !this.nextPositionEmpty; i++)
            {
                 bool isInList = this.obstacles.Exists(x => this.IgnoreYofVector(x.transform.position) == anglesOfRect[i]);

                if(!isInList)
                {
                    float previousY = transform.position.y;
                    this.nextPosition = anglesOfRect[i];
                    this.nextPosition.y = previousY;
                    return;
                }

            }

        }
        else
        {

        }


    }

    private void CalculateNextPosition()
    {

    }


    public void MoveDone()
    {
       this.mustMove = false;
        this.nextPositionEmpty = false;
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
