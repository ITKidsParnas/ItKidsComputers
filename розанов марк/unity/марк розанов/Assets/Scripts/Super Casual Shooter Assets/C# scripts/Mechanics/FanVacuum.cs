/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[RequireComponent(typeof(BoxCollider))]


public class FanVacuum : MonoBehaviour
{


    [SerializeField]
    private Axis suck_axis; // axis at which this vacuum will be pulling the player

    [SerializeField]
    private GameObject fan_blade; // rotating fan blade


    [SerializeField]
    private float fan_rotate_speed; // speed at which fan rotates

    [SerializeField]
    [Range(0, 1)]
    private float vacuum_suck_speed; // speed at which vacuum is pulling the player

    [SerializeField]
    [Range(0, 1)]
    private float harm_value = 0.1f; // the damage we will cause to player if player is too close to vacuum

    

    [SerializeField]
    [Range(1, 10)]
    private int start_harming_player_at_distance = 2; // distance at which vacuum will start harming player
   


    // Update is called once per frame
    void Update()
    {
        rotateFanBlade();
    }

    private void rotateFanBlade()
    {
        switch (suck_axis)
        {
            case Axis.X:

                fan_blade.transform.Rotate(fan_rotate_speed * Time.deltaTime, 0, 0);
                break;

            case Axis.Y:
                fan_blade.transform.Rotate(0, fan_rotate_speed * Time.deltaTime, 0);

                break;

            case Axis.Z:

                fan_blade.transform.Rotate(0, 0, fan_rotate_speed * Time.deltaTime);
                break;

        }
    }


    private void OnTriggerStay(Collider other) // if player is around vacuum, suck the player in
    {
        CharacterController character_controller = other.gameObject.GetComponent<CharacterController>();

        Damagable player_damage = other.gameObject.GetComponent<Damagable>();

        if (character_controller)
        {
            Vector3 direction_to_player = transform.position - character_controller.gameObject.transform.position;
            direction_to_player.Normalize() ;

            other.gameObject.GetComponent<CharacterController>().Move(direction_to_player * vacuum_suck_speed); // suck player towards this object

            
            if ( player_damage
                &&
                Vector3.Distance(transform.position, character_controller.transform.position) < start_harming_player_at_distance) // if player is close enough, then harm player
            {
                player_damage.takeDamage(harm_value);
            }
        }
    }
}
