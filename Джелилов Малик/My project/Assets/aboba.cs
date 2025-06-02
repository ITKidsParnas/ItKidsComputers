using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class aboba : MonoBehaviour
{
    public GameObject[] objs;
    private void OnCollisionEnter(Collision collision)
    {
     foreach (var obj in objs)
        {
            obj.SetActive(true);
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
