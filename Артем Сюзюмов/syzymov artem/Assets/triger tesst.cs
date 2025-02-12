using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class trigertesst : MonoBehaviour
{
    public Color color;

    private void OnTriggerEnter(Collider other)
    {

        other.GetComponent<MeshRenderer>().materials[0].color = color;
    }
    private void OnTriggerExit(Collider other)
    {
        other.GetComponent<MeshRenderer>().materials[0].color = Color.white;

    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
