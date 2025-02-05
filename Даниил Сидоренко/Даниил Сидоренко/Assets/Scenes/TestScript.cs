using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TestScript : MonoBehaviour
{ 
    void Start()// start вызывается перед первым кадром
    {
        Debug.Log("start вызывается перед первым кадром"); 
    } 
    void Update()// Update вызывается каждый каждый кадр
    {
        Debug.Log("Update вызывается каждый каждый кадр");
    }
    private void OnCollisionEnter(Collision collision) //OnCollisionEnter при столкновении
    {
        Debug.Log("OnCollisionEnter при столкновении");
    }
    private void OnCollisionExit(Collision collision) //OnCollisionExit вызывается при выходе из колизии 
    {
        Debug.Log("OnCollisionExit вызывается при выходе из колизии");
    }
}
