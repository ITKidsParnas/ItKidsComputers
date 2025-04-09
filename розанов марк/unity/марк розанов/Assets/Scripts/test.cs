using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class test : MonoBehaviour
{
    public GameObject [] obis;
    private void OnCollisionEnter(Collision collision)
    {
        foreach (var item in obis)
        {
            item.SetActive(true);
        }
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
