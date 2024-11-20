using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ColorJump : MonoBehaviour
{
    public Color color;
    private void OnCollisionEnter(Collision collision)
    {
        GetComponent<MeshRenderer>().materials[0].color = color;
    }
    
    private void OnCollisionExit(Collision collision)
    {
        GetComponent<MeshRenderer>().materials[0].color = Color.cyan;
    }

}
