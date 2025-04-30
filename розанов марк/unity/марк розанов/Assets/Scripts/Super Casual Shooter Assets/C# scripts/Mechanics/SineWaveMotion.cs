/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public enum Axis
{
    X, Y, Z
}


public class SineWaveMotion : MonoBehaviour
{
    [SerializeField]
    private Axis axis;

    [SerializeField]
    private float amplitude;

    [SerializeField]
    private float frequency;

    private float counter = 0;

    private float initial_position;

    private float position_value;


    // Start is called before the first frame update
    void Start()
    {
        // set initial position value based on the axis
        switch (axis)
        {
            case Axis.X:
                initial_position = transform.position.x;
                break;

            case Axis.Y:
                initial_position = transform.position.y;
                break;

            case Axis.Z:
                initial_position = transform.position.z;
                break;
        }
    }

    // Update is called once per frame
    void Update()
    {

        if(counter < (2 * Mathf.PI) / frequency) // this basically simulates repeated sine wave oscilation
        {
            counter += Time.deltaTime;
        }
        else
        {
            counter = 0;
        }

        position_value =  amplitude * Mathf.Sin(counter * frequency);


        switch (axis) // apply position based on axis
        {
            case Axis.X:
                transform.position = new Vector3(initial_position + position_value, transform.position.y, transform.position.z);
                break;


            case Axis.Y:
                transform.position = new Vector3(transform.position.x, initial_position + position_value, transform.position.z);
                break;


            case Axis.Z:
                transform.position = new Vector3(transform.position.x, transform.position.y, initial_position + position_value);
                break;

        }
    }
}
