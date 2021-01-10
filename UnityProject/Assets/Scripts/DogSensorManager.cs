using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DogSensorManager : Sensor
{
    public DogSensor[] viewSensors;

    private void Start()
    {
        Invoke("Test", 2f);
    }

    private string ComposeStringSensor()
    {
        string sensorsString = MessageType.DOG_SENSOR+MessageHandler.messageTypeSeparetor;

        foreach(DogSensor dogSensor in viewSensors)
        {
            sensorsString += dogSensor.myCell.ToString()+MessageHandler.messageVectorSeparetor;
        }

        sensorsString = sensorsString.Remove(sensorsString.Length-1);

        return sensorsString;
    }

    private void Test()
    {
        string test = ComposeStringSensor();

        Debug.Log("TEST: " + test);
    }
}
