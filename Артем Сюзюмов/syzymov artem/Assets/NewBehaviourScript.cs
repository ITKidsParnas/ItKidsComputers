using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    private void OnCollisionEnter(Collision collision)
    {
        GetComponent<MeshRenderer>().materials[0].color = Color.blue;
        
    }
    private void OnCollisionExit(Collision collision)
    {
         GetComponent<MeshRenderer>().materials[0].color = Color.black;
    }
}
