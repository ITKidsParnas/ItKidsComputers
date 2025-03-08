using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HouseTeleport : MonoBehaviour
{
    public GameObject house;
    public GameObject player;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private void OnTriggerStay(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            if (Input.GetKey(KeyCode.E)) 
                {
                    var housePosition = house.transform.position;
                    player.transform.localPosition = housePosition;
                }
        }
        
    }
}
