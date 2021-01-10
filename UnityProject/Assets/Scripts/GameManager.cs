using System;
using System.Collections;
using System.Collections.Generic;
using System.Reflection;
using UnityEngine;

public class GameManager : MonoBehaviour
{

    [HideInInspector]
    public static GameManager GameManagerInstance;

    [SerializeField]
    BoxCollider plane;
    [SerializeField]
    Dog dog;

    public MessageHandler connection;
    public static OBJECTSTYPE Turn
    {
        get
        {
            return _turn;
        }

    }

    private static OBJECTSTYPE _turn;
    private OBJECTSTYPE[] turnManagement = { OBJECTSTYPE.DOG, OBJECTSTYPE.SHEEP };
    private int CounterType
    {
        get
        {
            return _counterType;
        }
        set
        {
            _counterType = (this._counterType + value) % (this.turnManagement.Length+1);
        }
    }

    private int _counterType = 0;

    void Awake()
    {
        GameManagerInstance = this;


        connection.SendMessage(MessageType.PLANE_SIZE, plane.size);
        connection.SendMessage(MessageType.DOG_POSITION, dog.transform.position);

        // Initial turn is for the dog
        _turn = turnManagement[CounterType];
    }

    private void Start()
    {


    }

    public void PassTurn(OBJECTSTYPE type)
    {
        if(Turn == type)
        {
            CounterType++;
            _turn = turnManagement[CounterType];
            Debug.Log("TURNO DI: " + Turn);
        }
    }

    public void SendSensorMessage(MessageType messageType, string message)
    {
        connection.SendMessage(messageType, message);
    }




}
