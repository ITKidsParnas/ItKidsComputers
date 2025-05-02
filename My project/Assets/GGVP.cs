using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class GGVP : MonoBehaviour
{
    public GameObject[] objs;
    private void OnCollisionEnter(Collision collision)
    {
        foreach (var item in objs)
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
