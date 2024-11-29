using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class playercontroler : MonoBehaviour
{
   
    
    void Update()
    {
        transform.position = Vector3.MoveTowards(transform.position,
          new Vector3(transform.position.x + Input.GetAxis("Horizontal"), transform.position.y, transform.position.z + Input.GetAxis("Vertical")), Time.deltaTime+5);
        
    }
}
