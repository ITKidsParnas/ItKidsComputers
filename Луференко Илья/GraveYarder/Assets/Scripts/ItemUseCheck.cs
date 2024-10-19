using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ItemUseCheck : MonoBehaviour
{

    public BoxCollider cubeCollider; // Флаг для отслеживания, находится ли игрок в триггере

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
