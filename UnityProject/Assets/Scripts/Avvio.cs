using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Avvio : MonoBehaviour
{
    [SerializeField]
    GameObject piano;
    [SerializeField]
    GameObject cane;

    public MessageHandler connection;

    // Start is called before the first frame update
    void Start()
    {
        Debug.Log((int)MessageType.PLANE);
        

        connection.SendData(MessageToSend(MessageType.PLANE,piano.GetComponent<BoxCollider>().size));
        connection.SendData(MessageToSend(MessageType.DOG,cane.transform.position));
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private int[] coordinateSplit(Vector3 coordinate)
    {
        int x = (int)coordinate.x;
        int z = (int)coordinate.z;
        int[] intcoord = [x, z];
        return intcoord;
    }

    private string MessageToSend(MessageType type, Vector3 coordinates)
    {
        string textToSend;
        const string separetor = ",";
        int[] intCordinate = coordinateSplit(coordinates);

        textToSend = (int)type + separetor + intCordinate[0] + separetor + intCordinate[1];


        return textToSend;

    }
}


public enum MessageType
{
    PLANE,
    DOG,
    SENSOR
}