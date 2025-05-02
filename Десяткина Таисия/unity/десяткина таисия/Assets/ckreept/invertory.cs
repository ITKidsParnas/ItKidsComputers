using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class invertory : MonoBehaviour
{
    public Transform point;
    private duck _duck;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (_duck != null &&Input.GetKeyDown(KeyCode.Q))
        {
            RaycastHit hit;
            // Does the ray intersect any objects excluding the player layer
            if (Physics.Raycast(Camera.main.transform.position, Camera.main.transform.TransformDirection(Vector3.forward), out hit, Mathf.Infinity))
            {
                Debug.DrawRay(transform.position, transform.TransformDirection(Vector3.forward) * hit.distance, Color.yellow);
                var duckPlace =hit.transform.gameObject.GetComponent<duckPlace>();
                if (duckPlace != null) 
                {
                    duckPlace.SetDuck(_duck.transform);
                    _duck = null;
                }
                Debug.Log("Did Hit");
            }
            else
            {
                Debug.DrawRay(transform.position, transform.TransformDirection(Vector3.forward) * 1000, Color.white);
                Debug.Log("Did not Hit");
            }

        }
    }
    private void OnCollisionEnter(Collision collision)
    {
        var dack = collision.gameObject.GetComponent<duck>();
        if (dack != null)
        {
            dack.gameObject.SetActive( false);
            _duck = dack;
        }
    }
}
