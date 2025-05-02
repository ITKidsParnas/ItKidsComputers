using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MassiveTEST : MonoBehaviour
{
    public Transform[] Transforms;
    // Start is called before the first frame update

    void Start()
    {
        Debug.Log(Transforms[0].name);
    }

    private void OnCollisionEnter(Collision collision)
    {
        foreach (var item in Transforms)
        {
       //   item.posittion += Vector3.up;
        }
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
