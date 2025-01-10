using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gun : MonoBehaviour
{
    public GameObject effect;
    public AudioSource audioSource;
    public Rigidbody[] rigidbodies;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
       if(Input.GetKeyDown(KeyCode.Space)) 
        {
            effect.SetActive(true);
            audioSource.Play();
            foreach (var rigidbody in rigidbodies)
            { 
                rigidbody.isKinematic = false;
            }
        } 
    }
}
