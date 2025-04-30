/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TimeBombController : Collectable
{
    
    // Update is called once per frame
    protected override void Update()
    {
        base.Update();

        if (PlayerInput.instance.mouse_left_click  &&  is_in_players_pocket)
        {
            triggerAllTimeBombs();
        }
    }


    private void triggerAllTimeBombs() // find all time bombs and explode them
    {
        foreach (TimableBomb t in FindObjectsOfType<TimableBomb>())
        {
            t.nowExplode();
        }
    }

}
