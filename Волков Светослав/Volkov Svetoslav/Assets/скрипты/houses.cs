using System;
using System.Collections;
using System.Collections.Generic;
using System.Data.SqlTypes;
using Unity.VisualScripting;
using UnityEngine;

public class houses : MonoBehaviour
{
    public float moneyInSec;
    public int cost;
    public float HateInSec;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        GAmecontroler.instans.money += moneyInSec * Time.deltaTime;
        GAmecontroler.instans.Hate = Math.Clamp( GAmecontroler.instans.Hate+ HateInSec * Time.deltaTime ,- 15f,100f) ;

    }
}
