using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerManagment : MonoBehaviour
{
 
    public float speed = 0.5f;
    public static float vertical, horizontal;
    void Start()
    {
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }


    void Update()
    {
        horizontal = Input.GetAxis("Horizontal")*speed*Time.deltaTime;
        vertical = Input.GetAxis("Vertical")*speed* Time.deltaTime;
        transform.Translate(horizontal, 0, 0);
        transform.Translate(0, 0, vertical);
    }
}
