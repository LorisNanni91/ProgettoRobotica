using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MessageHandler : UdpSocket
{
    List<string> messagesArrived = new List<string>();
    List<string> messagesSended = new List<string>();

    public void SendMessage(MessageType type, Vector3 coordinates)
    {
        string message = MessageToSend(type, coordinates);
        messagesSended.Add(message);
        SendData(message);
    }

    protected override void ReceiveData()
    {
        base.ReceiveData();
        messagesArrived.Add(this.textReceived);
       
    }

    public string GetLastArrivedMessage()
    {
        return messagesArrived[messagesArrived.Count-1];
    }

    private string MessageToSend(MessageType type, Vector3 coordinates)
    {
        string textToSend;
        int[] intCordinate = CoordinateSplit(coordinates);

        textToSend = (int)type + "|" + intCordinate[0] + "," + intCordinate[1];

        return textToSend;

    }

    private int[] CoordinateSplit(Vector3 coordinate)
    {
        int x = (int)coordinate.x;
        int z = (int)coordinate.z;
        int[] intcoord = { x, z };

        return intcoord;
    }


}

public enum MessageType
{
    PLANE,
    DOG,
    SENSOR
}
