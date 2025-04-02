using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    public GameObject[] objs;    
    // Start is called before the first frame update
    void Start()
    {
        
        {
            
        }
    }

    private void OnCollisionEnter(Collision collision)
    {
        foreach (var item in objs)
        {
            item.SetActive(false);
        }






    }
    // Update is called once per frame
    void Update()
    {
       
    }
}
