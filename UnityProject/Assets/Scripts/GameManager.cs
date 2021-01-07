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

    private Sheep sheep;

    public MessageHandler connection;
    public static Type Turn
    {
        get
        {
            return _turn.GetType();
        }

    }

    private static MovableObjects _turn;
    private MovableObjects[] turnManagement;
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

        if(this.sheep == null)
        {
            sheep = FindObjectOfType<Sheep>();
        }

        turnManagement = new MovableObjects[2] { dog, sheep };

        connection.SendMessage(MessageType.PLANE_SIZE, plane.size);
        connection.SendMessage(MessageType.DOG_POSITION, dog.transform.position);

        // Initial turn is for the dog
        _turn = turnManagement[CounterType];
    }

    private void Start()
    {
        //Debug.Log("TURNO DI: " + Turn);
        Debug.Log(turnManagement.ToString());

    }

    public void PassTurn(MovableObjects movableObject)
    {
        if(Turn == movableObject.GetType())
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
