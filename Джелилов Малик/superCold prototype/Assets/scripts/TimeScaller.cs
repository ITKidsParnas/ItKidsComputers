using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TimeScaller : MonoBehaviour
{
private Rigidbody rb;
    // Start is called before the first frame update
    void Start()
    {
        Time.timeScale = 0.5f; 
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        Debug.Log("rb.velocity" + rb.velocity);
        if (rb.velocity==Vector3.zero)
        {
            Debug.Log("Time.timeScale" + Time.timeScale);
            Time.timeScale = Mathf.Clamp(Time.timeScale + 0.002f, 0.5f, 2f);
        }
    }
}
