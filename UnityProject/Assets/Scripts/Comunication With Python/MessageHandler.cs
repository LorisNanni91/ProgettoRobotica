﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MessageHandler : UdpSocket
{
    public const string messageTypeSeparetor = "|";
    public const string messagePositionSeparetor = ",";
    public const string messageVectorSeparetor = ":";
    List<string> messagesArrived = new List<string>();
    List<string> messagesSended = new List<string>();

    public void SendMessage(MessageType type, Vector3 coordinates)
    {
        string message = MessageFormattation(type, coordinates);
        Send(message);
    }

    public void SendMessage(MessageType type, string text)
    {
        string message = MessageFormattation(type, text);
        Send(message);
    }

    private void Send(string message)
    {
        messagesSended.Add(message);
        SendData(message);
    }

    //protected override void ReceiveData()
    //{
    //    base.ReceiveData();
    //    messagesArrived.Add(this.textReceived);

    //    Debug.Log("Message arrived " + this.textReceived);

    //}

    protected override void SaveLastMessage(string message)
    {
        messagesArrived.Add(this.textReceived);
        //Debug.Log("Message arrived " + this.textReceived);
    }

    public string GetLastArrivedMessage()
    {
        return messagesArrived[messagesArrived.Count-1];
    }

    private string MessageFormattation(MessageType type, string text)
    {
        string textToSend;
        textToSend = type+MessageHandler.messageTypeSeparetor+text;

        return textToSend;
    }

    private string MessageFormattation(MessageType type, Vector3 coordinates)
    {
        string textToSend;
        int[] intCordinate = CoordinateSplit(coordinates);

        textToSend = type.ToString() + "|" + intCordinate[0] + "," + intCordinate[1];

        return textToSend;

    }

    private int[] CoordinateSplit(Vector3 coordinate)
    {
        int x = (int)coordinate.x;
        int z = (int)coordinate.z;
        int[] intcoord = { x, z };

        return intcoord;
    }

    public bool NewMessageToRead(int messagesReaded)
    {
        return messagesReaded < this.messagesArrived.Count;
    }


}

public enum MessageType
{
    PLANE_SIZE,
    DOG_POSITION,
    DOG_SENSOR,
    GOAL_FOUND,
    GOAL_REACHED
}
