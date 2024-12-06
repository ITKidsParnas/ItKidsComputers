using System.Collections;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using UnityEngine;

public class JumpScript : MonoBehaviour
{
    public bool isRepaint;


    public Color color;
    public Rigidbody body;
    private void OnCollisionEnter(Collision collision)
    {
        if (isRepaint)
        {
            GetComponent<MeshRenderer>().materials[0].color = color;
        }
    }
    //private void OnCollisionExit(Collision collision)
    //{
    //    GetComponent<MeshRenderer>().materials[0].color = Color.white;

    //}
}
