using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ItemUseCheck : MonoBehaviour
{

    public BoxCollider cubeCollider; 

    void Start()
    {

    }



    void Update()
    {
        if (PlayerManagment.isItemPickUp == false)
        {
            cubeCollider.isTrigger = false;
        }
        else
        {
            cubeCollider.isTrigger = true;
        }
    }
}
