using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Avvio : MonoBehaviour
{
    [SerializeField]
    GameObject piano;

    public MessageHandler connection;

    // Start is called before the first frame update
    void Start()
    {
        Vector3 dimensionepiano = new Vector3();
        dimensionepiano = piano.GetComponent<BoxCollider>().size;

        Debug.Log(dimensionepiano);
        string stringa = dimensionepiano.ToString();
        Debug.Log(stringa);
        string stringina = "ciao";
        connection.SendData(stringina);

    }

    // Update is called once per frame
    void Update()
    {
        
    }
}