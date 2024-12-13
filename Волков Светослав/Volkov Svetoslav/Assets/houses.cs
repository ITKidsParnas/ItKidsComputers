using System;
using System.Collections;
using System.Collections.Generic;
using System.Data.SqlTypes;
using UnityEngine;

public class houses : MonoBehaviour
{
    public GAmecontroler gc;
    public float moneyInSec;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        gc.money += moneyInSec * Time.deltaTime; 
            
    }
}
