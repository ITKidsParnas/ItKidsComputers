using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UI;

public class practika : MonoBehaviour
{
    
    public GameObject[] masiv;
    // Start is called before the first frame update
    void Start()
    {
        for (int i = 0; i < 10; i++)
        {
            Debug.Log("проектор");
        }
    }  
    // Update is called once per frame
    void Update()
    {
       
    }
   
    private void OnCollisionEnter(Collision collision)
    {
        foreach (var item in masiv)
        {
            item.SetActive(false);
        }
    }
}
