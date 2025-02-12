using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class arrayTest : MonoBehaviour
{
    public Transform[] transforms;
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log(transforms[0].name);
    }
    private void OnCollisionEnter(Collision collision)
    {
        foreach (var item1 in transforms)
        {
     item.psi       
        }
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
