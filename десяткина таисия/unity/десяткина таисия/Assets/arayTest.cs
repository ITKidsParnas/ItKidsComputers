using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class arayTest : MonoBehaviour
{
    public Transform[] Transforms;

    // Start is called before the first frame update
    void Start()
    {
        Debug.Log(Transforms[0].name);
            
    }
    private void OnCollisionEnter(Collision collision)
    {
        foreach (Transform item in Transforms)
            item.position += Vector3.up;
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
