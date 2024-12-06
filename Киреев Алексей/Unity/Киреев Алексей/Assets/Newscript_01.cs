using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Newscript_01 : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        print("hi IDIOT,welcome to durka");
    }
    private void OnCollisionExit(Collision collision)
    {
        
    }
    private void OnCollisionEnter(Collision collision)
    {
        GetComponent<MeshRenderer>().materials[0].color = Color.black;

       
    }
    // Update is called once per frame
    void Update()
    {
        print("hi IDIOT,welcome to durka");
    }
}
