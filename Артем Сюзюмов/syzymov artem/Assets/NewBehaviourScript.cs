using System.Collections;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    public Color color;
    public Rigidbody boby;
    private void OnCollisionEnter(Collision collision)
    {
        GetComponent<MeshRenderer>().materials[0].color = Color.blue;
        
    }
    private void OnCollisionExit(Collision collision)
    {
         GetComponent<MeshRenderer>().materials[0].color = Color.black;
    }
}
