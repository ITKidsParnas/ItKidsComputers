using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class color_jump : MonoBehaviour
{
    private void OnCollisionEnter(Collision collision)
    {
        GetComponent<MeshRenderer>().materials[0].color = Color.green;
   
    }
    private void OnCollisionExit(Collision collision)
    {
    }
}
