using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class kaftame2 : MonoBehaviour
{
    public int number;
    public Color color;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private void OnCollisionEnter(Collision collision)
    {
        if (true)
        {

        }
        GetComponent<MeshRenderer>().materials[0].color=color;
    }
}
