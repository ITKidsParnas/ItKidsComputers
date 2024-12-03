using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ColorJump : MonoBehaviour
{
    public bool isRepaint;

    public Color color;
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
