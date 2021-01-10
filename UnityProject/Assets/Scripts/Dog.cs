using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Dog : MovableObjects
{
    private DogSensorManager dogSensor;
    private int movesCounter = 0;
    private bool newIstructionArrived = false;
    private bool waitForIstrucition = false;
    List<string> istructions = new List<string>(); // need to be a class ?

    private void Start()
    {
        dogSensor = (DogSensorManager)sensor;


    }

    private void Update()
    {
        if(CanMove && !waitForIstrucition)
        {
            waitForIstrucition = true;
            StartCoroutine(DogTurn());

        }
        
    }

    private IEnumerator DogTurn()
    {
        GameManager.GameManagerInstance.SendPositionMessage(MessageType.DOG_POSITION, transform.position);
        GameManager.GameManagerInstance.SendSensorMessage(MessageType.DOG_SENSOR, this.dogSensor.GetStringSensor());

        //yield return new WaitUntil(() => newIstructionArrived);

        while(!newIstructionArrived)
        {
            newIstructionArrived = GameManager.GameManagerInstance.NewMessageToRead(this.istructions.Count);
            yield return new WaitForSeconds(1f);
        }

        string istruction = GameManager.GameManagerInstance.GetDogIstructionMessage();

        ExecuteIstruction(istruction);

        yield return null;

    }


    private void ExecuteIstruction(string message)
    {
        Vector3 mypostion = transform.position;

        switch(message)
        {
            case Actions.ROTATE_LEFT:
                transform.Rotate(new Vector3(0,-90,0));
                break;
            case Actions.ROTATE_RIGHT:
                transform.Rotate(new Vector3(0, 90, 0));
                break;
            case Actions.ROTATE_BACK:
                transform.Rotate(new Vector3(0, 180, 0));
                break;
            case Actions.NORTH_EAST:
                break;
            case Actions.NORTH_WEST:
                break;
            case Actions.NORTH:
                break;

            default:
                Debug.LogError("DOG RECEIVED INVALID ACTION");
                break;
             
        }

        // reset boolean
        waitForIstrucition = false;
        newIstructionArrived = false;

        this.movesCounter++;
        this.PassMyTurn();

    }

    private void RotateDog(float angle)
    {
        Vector3 rotation = transform.rotation.eulerAngles + Vector3.up * angle;
        transform.Rotate(rotation);
    }

}


public static class Actions
{
    // Rotation
    public const string ROTATE_RIGHT = "Rotate-Right";
    public const string ROTATE_LEFT = "Rotate-Left";
    public const string ROTATE_BACK = "Rotate-Back";

    // Move
    public const string NORTH = "North";
    public const string NORTH_EAST = "North-East";
    public const string NORTH_WEST = "North-West";
}
