/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;


[RequireComponent(typeof(BoxCollider))]
[RequireComponent(typeof(Rigidbody))]


public abstract class Collectable : MonoBehaviour
{

    public Vector3 offset; // offset position on hand

    public bool is_in_players_pocket // if this item has been picked up by player
    {
        get;
        private set;
    }


    private float collectable_distance = 5; // maximum distance from which player can pick up this item


    protected virtual void Update()
    {
        listenForPlayerInteraction();
    }

    public void pickUpThisObject()
    {
        is_in_players_pocket = true;
    }

    public void dropThisObject()
    {
        is_in_players_pocket = false;
    }


    protected void listenForPlayerInteraction()
    {
        // listen for player pickup interaction, if object is close enough and the object is not yet owned 
        if (PlayerInput.instance.interact)
        {
            if (Vector3.Distance(PlayerInput.instance.gameObject.transform.position, transform.position) < collectable_distance && !is_in_players_pocket)
            {
               
                PlayerInput.instance.player_collectable_manager.assignCollectableToHand(this);

            }
        }
    }
}