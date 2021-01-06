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
        //Debug.Log(piano.GetComponent<BoxCollider>().size);

        connection.SendMessage(MessageType.PLANE_SIZE, piano.GetComponent<BoxCollider>().size);
        connection.SendMessage(MessageType.DOG_POSITION, cane.transform.position);

    }


}
