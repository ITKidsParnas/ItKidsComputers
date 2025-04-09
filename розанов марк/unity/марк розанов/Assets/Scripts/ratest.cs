using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ratest : MonoBehaviour
{
    public Transform[] transforms;
    // Start is called before the first frame update
    void Start()
    {foreach (Transform transforms in transforms) {
        }
     //   Debug.Log(transforms[0].name);
    }
    private void OnCollisionEnter(Collision collision)
    {
        
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
