/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[RequireComponent(typeof(BoxCollider))]
public class Jumper : MonoBehaviour
{
   
    [SerializeField]
    [Range(0,1)]
    private float lift;

    private void OnTriggerEnter(Collider other) // set the player to jump on collision
    {
        FirstPersonController controller = other.GetComponent<FirstPersonController>();

        if (controller)
        {
            controller.setJump(lift);
            
        }
    }
}
