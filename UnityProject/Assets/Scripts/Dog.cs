﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Dog : MovableObjects
{
   

    private DogSensorManager dogSensorManager;
    private int movesCounter = 0;
    private bool newIstructionArrived = false;
    private bool waitForIstrucition = false;
    List<string> istructions = new List<string>(); // need to be a class ?

    private void Start()
    {
        dogSensorManager = (DogSensorManager)sensor;

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

        //Debug.Log("Start coroutine dog, waiting " + waitForIstrucition);

        this.dogSensorManager.UpdateSensor();

        // wait for unity updating sensors
        yield return new WaitForSeconds(1f);

        Debug.Log("DOG SENSOR: prima invio " + this.dogSensorManager.GetStringSensor());

        GameManager.GameManagerInstance.SendPositionMessage(MessageType.DOG_POSITION, transform.position);
        yield return new WaitForSeconds(1f);
        GameManager.GameManagerInstance.SendSensorMessage(MessageType.DOG_SENSOR, this.dogSensorManager.GetStringSensor());

        Debug.Log("DOG SENSOR: dopo invio " + this.dogSensorManager.GetStringSensor());

        //yield return new WaitUntil(() => newIstructionArrived);

        while(!newIstructionArrived)
        {
            //Debug.Log("dog waiting " + newIstructionArrived);

            newIstructionArrived = GameManager.GameManagerInstance.NewMessageToRead(this.istructions.Count);
            yield return new WaitForSeconds(1f);
        }

        string istruction = GameManager.GameManagerInstance.GetDogIstructionMessage();
        this.istructions.Add(istruction);

        ExecuteIstruction(istruction);

        yield return null;

    }


    private void ExecuteIstruction(string message)
    {

        //Debug.Log("Execute: " + message);

        Debug.Log("MOVE N# " + this.movesCounter + ": " + message + " current position:" + this.transform.position);


        switch (message)
        {
            case Actions.ROTATE_LEFT:
                transform.Rotate(new Vector3(0,-90,0),Space.Self);
                break;
            case Actions.ROTATE_RIGHT:
                transform.Rotate(new Vector3(0, 90, 0), Space.Self);
                break;
            case Actions.ROTATE_BACK:
                transform.Rotate(new Vector3(0, 180, 0), Space.Self);
                break;
            case Actions.FORWARD_LEFT:
                transform.Translate(new Vector3(-1,0,1), Space.Self);
                break;
            case Actions.FORWARD_RIGHT:
                transform.Translate(new Vector3(1,0,1), Space.Self);
                break;
            case Actions.FORWARD:
                transform.Translate(Vector3.forward,Space.Self);
                break;
            case Actions.LEFT:
                transform.Translate(Vector3.left, Space.Self);
                break;
            case Actions.RIGHT:
                transform.Translate(Vector3.right, Space.Self);
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

        StopAllCoroutines();

    }

    // ONLY TO TEST
    [ContextMenu("TestRotation")]
    private void TestRotation()
    {
        transform.Rotate(new Vector3(0, 90, 0), Space.Self);
    }

    [ContextMenu("TestMove")]
    private void TestMove()
    {
        transform.Translate(Vector3.forward, Space.Self);
    }



}


public static class Actions
{
    // Rotation
    public const string ROTATE_RIGHT = "Rotate-Right";
    public const string ROTATE_LEFT = "Rotate-Left";
    public const string ROTATE_BACK = "Rotate-Back";

    // Move
    public const string FORWARD = "Forward";
    public const string FORWARD_LEFT = "Forward-Left";
    public const string FORWARD_RIGHT = "Forward-Right";
    public const string LEFT = "Left";
    public const string RIGHT = "Right";
}
