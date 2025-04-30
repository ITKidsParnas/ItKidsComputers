/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DeathZone : MonoBehaviour
{
   
    private void OnTriggerEnter(Collider other) // any damagable that collides with this object will get the maximum damage
    {
        Damagable damagable = other.GetComponent<Damagable>();

        if(damagable)
        {
            damagable.takeDamage(damagable.getMaxHealth());
        }
    }
}
