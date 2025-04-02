using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class by : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }
    private void OnCollisionExit(Collision collision)
    {
        GetComponent<MeshRenderer>().materials[0].color = Color.red;
    }
    private void OnCollisionEnter(Collision collision)
    {

        GetComponent<MeshRenderer>().materials[0].color = Color.green;

    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
