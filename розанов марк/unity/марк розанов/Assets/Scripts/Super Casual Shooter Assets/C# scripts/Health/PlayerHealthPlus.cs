/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[RequireComponent(typeof(BoxCollider))]

public class PlayerHealthPlus : MonoBehaviour 
{
    [SerializeField]
    private int health_plus; // health amout to add to player
    
    private void OnTriggerEnter(Collider other)
    {
        FirstPersonController controller = other.GetComponent<FirstPersonController>();


        if(controller ) // of the other collider has a first person controller and a damagable component
        {
            Damagable player_damage = controller.GetComponent<Damagable>();

            if(player_damage)
            {
                other.gameObject.GetComponent<Damagable>().reverseDamage(health_plus); // add health
                Destroy(gameObject);
            }
               
        }
    }

}
