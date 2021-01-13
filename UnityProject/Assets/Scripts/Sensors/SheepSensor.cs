using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SheepSensor : Sensor
{
    private bool mustMove = false;
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
    /*
    private void OnTriggerEnter(Collider other)
    {

        Objects obstalce = other.GetComponent<Objects>();

        if (obstalce != null)
        {
            this.obstacles.Add(obstalce);

            if (obstalce.type == OBJECTSTYPE.DOG)
            {
                RunAwayFromDog(obstalce);
            }

        }


    }
    */

    private void OnTriggerStay(Collider other)
    {

        Objects obstalce = other.GetComponent<Objects>();

        if (obstalce != null)
        {
            if(!this.obstacles.Contains(obstalce))
            {
                this.obstacles.Add(obstalce);
            }


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
        Vector3 delta = transform.position - dog.transform.position;

        SetNextPosition(transform.position + delta);
        CheckObstacles();
    }

    private void CheckObstacles()
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

            for (int i = 0; i < anglesOfRect.Length; i++)
            {
                 bool isInList = this.obstacles.Exists(x => this.IgnoreYofVector(x.transform.position) == anglesOfRect[i]);

                if(!isInList)
                {
                    SetNextPosition(anglesOfRect[i]);
                    return;
                }

            }

            // all points are full, do something else

        }
        else
        {
            bool isInList = this.obstacles.Exists(x => this.IgnoreYofVector(x.transform.position) == this.IgnoreYofVector(this.nextPosition));

            if(isInList)
            {

            }

        }


    }

    private void SetNextPosition(Vector3 nextPosition)
    {
        float previousY = transform.parent.position.y;
        this.nextPosition = nextPosition;
        this.nextPosition.y = previousY;
    }


    public void MoveDone()
    {
       this.mustMove = false;
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
