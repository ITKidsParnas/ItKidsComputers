/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HoverBoardPropeller : MonoBehaviour
{

    [SerializeField]
    private Axis axis;

    [SerializeField]
    [Range(1, 1000)]
    private int speed;


   
    // Update is called once per frame
    void Update()
    {
        // sinumate fan blade spinning on an axis
        if(axis == Axis.X)
        {
            transform.Rotate(speed * Time.deltaTime, 0, 0);
        }

        if (axis == Axis.Y)
        {
            transform.Rotate(0, speed * Time.deltaTime, 0);
        }

        if (axis == Axis.Z)
        {
            transform.Rotate(0, 0 ,speed * Time.deltaTime);
        }
    }


}
