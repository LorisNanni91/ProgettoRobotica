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

        connection.SendMessage(MessageType.PLANE, piano.GetComponent<BoxCollider>().size);
        connection.SendMessage(MessageType.DOG,cane.transform.position);

        //connection.SendData(MessageToSend(MessageType.PLANE,piano.GetComponent<BoxCollider>().size));
        //connection.SendData(MessageToSend(MessageType.DOG,cane.transform.position));
    }

    // Update is called once per frame
    void Update()
    {
        
    }

}
