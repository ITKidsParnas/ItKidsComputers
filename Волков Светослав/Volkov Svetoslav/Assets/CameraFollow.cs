using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class CameraFollow : MonoBehaviour
{
    public float maxHorizontal;
    public float minHorizontal;
    public float maxVertical;
    public float minVertical;
    public float smoothSpeed = 0.125f;  // Скорость сглаживания
    private void Update()
    {
        var target = transform.position + new Vector3(Mathf.Clamp(Input.GetAxis("Horizontal"), minHorizontal,  maxHorizontal),
       0, Mathf.Clamp(Input.GetAxis("Vertical"), minVertical, maxVertical));    
        transform.position = Vector3.MoveTowards(transform.position, target, Time.deltaTime * smoothSpeed);
    }

}

