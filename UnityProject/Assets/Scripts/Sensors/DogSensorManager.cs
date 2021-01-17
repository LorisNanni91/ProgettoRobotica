using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DogSensorManager : Sensor
{
    public DogSensor[] viewSensors;


    public string GetStringSensor()
    {
        string sensorsString = "";

        foreach(DogSensor dogSensor in viewSensors)
        {
            sensorsString += dogSensor.myCell.ToString()+MessageHandler.messageVectorSeparetor;
        }

        // to remove last separetor
        sensorsString = sensorsString.Remove(sensorsString.Length-1);

        return sensorsString;
    }

    public void UpdateSensor()
    {
        foreach (DogSensor dogSensor in viewSensors)
        {
            dogSensor.OnMove();
        }

        Debug.Log("NEW SENSOR UPDATE: "+GetStringSensor());
    }

}
