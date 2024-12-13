using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class CameraFollow : MonoBehaviour
{
    public float smoothSpeed = 0.125f;  // Скорость сглаживания
    private void Update()
    {
        var target = transform.position + new Vector3(Input.GetAxis("Horizontal"), 0, Input.GetAxis("Vertical"));
        transform.position = Vector3.MoveTowards(transform.position, target, Time.deltaTime * smoothSpeed);
    }

}

