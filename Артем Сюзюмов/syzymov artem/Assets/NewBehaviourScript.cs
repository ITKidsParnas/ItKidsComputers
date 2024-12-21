using System.Collections;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    public bool isRepaint; 
    public Color color;
    public Rigidbody boby;

    private void OnCollisionEnter(Collision collision)
    {
        if (isRepaint)     
        {          
           GetComponent<MeshRenderer>().materials[0].color = Color.blue;  
        }
        
        
    }
    //private void OnCollisionExit(Collision collision)
    //{
    //     GetComponent<MeshRenderer>().materials[0].color = Color.black;
    //}
}
