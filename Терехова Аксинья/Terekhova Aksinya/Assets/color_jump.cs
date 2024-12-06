using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class color_jump : MonoBehaviour
{

    public bool isRepoint;

    public Color color;
    private void OnCollisionEnter(Collision collision)
    { if (isRepoint)
        {
            GetComponent<MeshRenderer>().materials[0].color = color;
        }
    }
    //private void OnCollisionExit(Collision collision)
    //{
    //    GetComponent<MeshRenderer>().materials[0].color = Color.blue;
    //}
}