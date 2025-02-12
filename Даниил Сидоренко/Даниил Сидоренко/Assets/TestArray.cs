using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TestArray : MonoBehaviour
{
    public Transform[] array;
    // Start is called before the first frame update
    void Start()
    {
        
    }
    private void OnCollisionEnter(Collision collision)
    {
        foreach(Transform item in array)
        {
            item.position += Vector3.up;
        }
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
