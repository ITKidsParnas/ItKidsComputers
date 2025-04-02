using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.VFX;

public class housePlase : MonoBehaviour
{
    public GAmecontroler gc;
    public houses house;
    public int cost;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    private void OnMouseDown()
    {
        if (gc.money >= cost)
        { 
            gc.money -= cost;
            var obj = Instantiate(house.gameObject, transform.position, Quaternion.identity);
                obj.GetComponent<houses>().gc=gc;
            obj.transform.rotation = transform.rotation;
            Destroy(gameObject);
        }
            
    }
}
