using System.Collections;
using System.Collections.Generic;
using Unity.Mathematics;
using UnityEngine;

public class CartRotate : MonoBehaviour
{
    public GameObject cart;
    public Vector3 rotateAngle =new (0, 180, 0);
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("Cart"))
        {
         
        }
    }
}
