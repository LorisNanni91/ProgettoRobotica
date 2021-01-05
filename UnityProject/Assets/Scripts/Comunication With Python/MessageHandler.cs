using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MessageHandler : UdpSocket
{
    List<string> messagesArrived = new List<string>();

    protected override void ReceiveData()
    {
        base.ReceiveData();
        messagesArrived.Add(this.textReceived);
       
    }

    public string GetLastArrivedMessage()
    {
        return messagesArrived[messagesArrived.Count-1];
    }


}
