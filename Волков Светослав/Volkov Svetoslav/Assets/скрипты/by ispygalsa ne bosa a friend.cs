using System.Collections;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;
using UnityEngine;

public class byispygalsanebosaafriend : MonoBehaviour

    
{
    public bool canRepaint;
    public int number;
    public Color color;
    public Color new_color;
    public int im;
    // Start is called before the first frame update
    void Start()                
    {
        
    }
    private void OnCollisionEnter(Collision collision)
    {
        if (canRepaint) 
        {

            GetComponent<MeshRenderer>().materials[0].color = color;
        }
        

    }
    private void OnCollisionExit(Collision collision)
    {
        GetComponent<MeshRenderer>().materials[0].color = new_color;
    }
    // Update is called once per frame
    void Update()
    {

    
        
    }
}
