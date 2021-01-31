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
    [SerializeField]
    private MessageHandler connection;
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

        StartCoroutine(SendInitialData());

        // Initial turn is for the dog
        _turn = turnManagement[CounterType];
    }

    IEnumerator SendInitialData()
    {
        yield return new WaitForSeconds(1f);

        Debug.Log("PLANE SIZE: " + plane.size);
        connection.SendMessage(MessageType.PLANE_SIZE, plane.size);
        yield return new WaitForSeconds(1f);

        connection.SendMessage(MessageType.DOG_POSITION, dog.transform.position);
        Debug.Log("DOG POSITION: " + plane.size);

        yield return null;
    }

    public void PassTurn(OBJECTSTYPE type)
    {
        if(Turn == type)
        {
            CounterType++;
            _turn = turnManagement[CounterType];
           // Debug.Log("TURNO DI: " + Turn);
        }
    }

    public void SendSensorMessage(MessageType messageType, string message)
    {
        connection.SendMessage(messageType, message);
    }

    public void SendPositionMessage(MessageType messageType, Vector3 position)
    {
        connection.SendMessage(messageType, position);
    }

    public string GetDogIstructionMessage()
    {
        return this.connection.GetLastArrivedMessage();
    }

    public bool NewMessageToRead(int messagesReaded)
    {
        return connection.NewMessageToRead(messagesReaded);
    }




}
