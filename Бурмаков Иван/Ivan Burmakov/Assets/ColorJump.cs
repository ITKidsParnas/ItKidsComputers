using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ColorJump : MonoBehaviour
{
    public Color color;
    public bool isRepaint;

    private void OnCollisionEnter(Collision collision)
    {
        if (isRepaint)
        {
            GetComponent<MeshRenderer>().materials[0].color = color;
        }
    }

    //private void OnCollisionExit(Collision collision)
    //{
    //    GetComponent<MeshRenderer>().materials[0].color = Color.cyan;
    //}

}
