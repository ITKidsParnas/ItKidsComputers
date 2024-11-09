using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NightDayControll : MonoBehaviour
{
    
    public Light sun; 
    public float dayLength = 1440f; 

    private float rotationSpeed;

    void Start()
    {
        rotationSpeed = 360f / dayLength; 
    }

    void Update()
    {
        sun.transform.Rotate(rotationSpeed * Time.deltaTime, 0, 0);
    }
}
