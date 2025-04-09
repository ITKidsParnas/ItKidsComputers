using System;
using System.Collections;
using System.Collections.Generic;
using System.Data.SqlTypes;
using UnityEngine;

public class houses : MonoBehaviour
{
    public float moneyInSec;
    public int cost;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        GAmecontroler.instans.money += moneyInSec * Time.deltaTime;
            
    }
}
