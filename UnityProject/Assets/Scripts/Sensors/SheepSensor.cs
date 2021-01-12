using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SheepSensor : Sensor
{
    private bool mustMove = false;
    private bool nextPositionEmpty = false;
    public Vector3 nextPosition;
    private Vector3 lastDogPosition;
    private void OnTriggerEnter(Collider other)
    {

        Objects Object = other.GetComponent<Objects>();

        if(Object != null)
        {

            //if (Object.type == OBJECTSTYPE.OBSTACLE)
            //{
            //    this.obstacles.Add(other.gameObject);
            //}

            if (Object.type == OBJECTSTYPE.DOG)
            {
                this.lastDogPosition = other.transform.position;
                mustMove = true;
                float previousY = transform.position.y;
                Vector3 delta = transform.position - other.transform.position;
                this.nextPosition = transform.position + delta;
                this.nextPosition.y = previousY;
                CheckObstacles();
            }

        }


    }

    private void CheckObstacles()
    {
        bool checkObstacle = Physics.CheckBox(this.nextPosition, this.nextPosition / 2);

        if(checkObstacle)
        {
            RecalculatePosition();
            return;
        }

        if(checkObstacle)
        {
            // swap direction
        }

    }

    private void RecalculatePosition()
    {

        Rect rect = new Rect(0,0, 2, 2);

        rect.center = new Vector2(transform.position.x, transform.position.z);

        Vector3[] anglesOfRect = new Vector3[4];

        anglesOfRect[0] = new Vector3(rect.xMin,0,rect.yMin);
        anglesOfRect[1] = new Vector3(rect.xMin,0,rect.yMax);
        anglesOfRect[2] = new Vector3(rect.xMax,0,rect.yMin);
        anglesOfRect[3] = new Vector3(rect.xMax,0,rect.yMax);

       for(int i=0; i< anglesOfRect.Length && !this.nextPositionEmpty;i++)
        {
            // dont work correctly, needs another method to check object at position
            bool testObstacle = Physics.CheckBox(anglesOfRect[i], anglesOfRect[i] / 2,Quaternion.identity,LayerMask.NameToLayer("Plane"));

            if(!testObstacle)
            {
                this.nextPosition = new Vector3(anglesOfRect[i].x,transform.position.y,anglesOfRect[i].z);
                //this.nextPositionEmpty = true;
            }

        }



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
