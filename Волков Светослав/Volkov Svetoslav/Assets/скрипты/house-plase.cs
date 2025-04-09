using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.VFX;

public class housePlase : MonoBehaviour
{
    
    // Start is called before the first frame update
    void Start()
    {
        
    }

    private void OnMouseDown()
    {
        BuildingManager.instance.BuildHouse(gameObject);  
    }
}
