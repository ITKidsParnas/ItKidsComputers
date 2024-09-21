using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraRotate : MonoBehaviour
{
    public GameObject PlayerCamera;
    
    private float MouseX;
    private float MouseY;
    private float MouseZ;
    public float mouseSpeed;



    void Start()
    {
        Cursor.lockState = CursorLockMode.Locked;
        mouseSpeed = 500;
    }

    void Update()
    {
        MouseX = Input.GetAxis("Mouse X") * mouseSpeed * Time.deltaTime;
        MouseY = -Input.GetAxis("Mouse Y") * mouseSpeed * Time.deltaTime;

        transform.rotation *= Quaternion.Euler(MouseY, MouseX, MouseZ);

    }
}
