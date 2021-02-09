using System.Linq;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SheepSensor : Sensor
{
    private bool mustMove = false;
    private bool nextPositionCalculated = false;
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
            if(!this.obstacles.Contains(obstalce) && obstalce.type != OBJECTSTYPE.GOAL)
            {
                this.obstacles.Add(obstalce);
                // need to recalculate next position
                this.nextPositionCalculated = false;
            }


            if (obstalce.type == OBJECTSTYPE.DOG && !this.nextPositionCalculated)
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
        CheckObstacles(dog.transform.position);
    }

    private void CheckObstacles(Vector3 dogPosition)
    {

        Rect rect = new Rect(0, 0, 2, 2);

        rect.center = new Vector2(transform.position.x, transform.position.z);

        Vector3[] cornerOfRect = new Vector3[4];

        cornerOfRect[0] = new Vector3(rect.xMin, 0, rect.yMin); // top-left corner
        cornerOfRect[1] = new Vector3(rect.xMin, 0, rect.yMax); // top-right corner
        cornerOfRect[2] = new Vector3(rect.xMax, 0, rect.yMin); // bottom-left corner
        cornerOfRect[3] = new Vector3(rect.xMax, 0, rect.yMax); // bottom-right corner


        if (this.NearWall)
        {
            // Make like billiards


            foreach(Vector3 corner in cornerOfRect)
            {
                 bool isInList = this.obstacles.Exists(x => GameManager.IgnoreYofVector(x.transform.position) == corner);

                if(!isInList)
                {
                    SetNextPosition(corner);
                    this.nextPositionCalculated = true;
                    return;
                }

            }

        }

        // all corner are full, check the further empty position from the dog

        Vector3[] rectMiddlePoints = new Vector3[4];

        rectMiddlePoints[0] = new Vector3(rect.xMin+1, 0, rect.yMin); // top-mid corner
        rectMiddlePoints[1] = new Vector3(rect.xMin, 0, rect.yMin+1); // left-mid corner
        rectMiddlePoints[2] = new Vector3(rect.xMax, 0, rect.yMin+1); // right-mid corner
        rectMiddlePoints[3] = new Vector3(rect.xMin+1, 0, rect.yMax); // bottom-mid corner


        Dictionary<Vector3, float> allRectPoints = new Dictionary<Vector3, float>();

        foreach(Vector3 rectValidPosition in cornerOfRect)
        {
            bool isInList = this.obstacles.Exists(x => GameManager.IgnoreYofVector(x.transform.position) == rectValidPosition);

            if (!isInList)
            {
                float distance = Vector3.Distance(GameManager.IgnoreYofVector(dogPosition), rectValidPosition);
                allRectPoints.Add(rectValidPosition,distance);

            }

        }


        foreach (Vector3 rectValidPosition in rectMiddlePoints)
        {
            bool isInList = this.obstacles.Exists(x => GameManager.IgnoreYofVector(x.transform.position) == rectValidPosition);

            if (!isInList)
            {
                float distance = Vector3.Distance(GameManager.IgnoreYofVector(dogPosition), rectValidPosition);
                allRectPoints.Add(rectValidPosition, distance);
            }

        }

        // we take the first further empty position from the dog
        Vector3 nextPositionRecalculated = allRectPoints.OrderByDescending(x => x.Value).First().Key;

        this.SetNextPosition(nextPositionRecalculated);
        this.nextPositionCalculated = true;




    }

    private void SetNextPosition(Vector3 nextPosition)
    {
        if(nextPosition!=null)
        {
            float previousY = transform.parent.position.y;
            this.nextPosition = nextPosition;
            this.nextPosition.y = previousY;
        }
        else
        {
            // don't move
            this.nextPosition = transform.parent.position;
        }
    }


    public void MoveDone()
    {
       this.mustMove = false;
       this.nextPositionCalculated = false;
    }

    public bool MustMove ()
    {
        return this.mustMove;
    }


}
