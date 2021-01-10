using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DogSensorManager : Sensor
{
    public DogSensor[] viewSensors;


    public string GetStringSensor()
    {
        string sensorsString = MessageType.DOG_SENSOR+MessageHandler.messageTypeSeparetor;

        foreach(DogSensor dogSensor in viewSensors)
        {
            sensorsString += dogSensor.myCell.ToString()+MessageHandler.messageVectorSeparetor;
        }

        sensorsString = sensorsString.Remove(sensorsString.Length-1);

        return sensorsString;
    }

}
