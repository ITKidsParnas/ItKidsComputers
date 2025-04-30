/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/



using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[RequireComponent(typeof(Explodable))]
public class TimableBomb : Collectable
{


    private Explodable explodable;
    

    public void nowExplode()
    {
        explodable.nowExplode();
    }

    private void Start()
    {
        
        explodable = GetComponent<Explodable>();
    }

    protected override void Update()
    {
        base.Update();

        if(PlayerInput.instance.mouse_left_click && is_in_players_pocket && gameObject.activeSelf )
        {
            PlayerCollectableManager.Instance.dropCollectable(this);

        }
    }
}
