/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(Damagable))]
[RequireComponent(typeof(Explodable))]
public class Grenade : Collectable 
{
    [SerializeField]
    [Range(1, 500)]
    protected int attack_value; // value of attack on damage


    protected bool is_thrown; // if grenade is thrown by player

    [SerializeField]
    protected float wait_before_ignite = 3;// wait in seconds before it blows up

    [SerializeField]
    [Range(1, 1.5f)]
    protected float up_throw_multiplier; // up force when throing grenade


    protected Explodable explodable; // explodable component
   
	// Use this for initialization
	private void Start ()
    {
       
        explodable = GetComponent<Explodable>();
       
	}
	// Update is called once per frame
	protected override void Update ()
    {
        base.Update();

        throwGrenade();
        
        if(gameObject.GetComponent<Damagable>() != null)
        {
            if(gameObject.GetComponent<Damagable>().getCurrentHealth() <= 0)
            {
               explodable.nowExplode();     
            }
        }

    }

    protected virtual void throwGrenade()
    {
        if (PlayerInput.instance.mouse_left_click && is_in_players_pocket && gameObject.activeSelf)
        {
            PlayerCollectableManager.Instance.dropCollectable(this); // player should drop grenade


            int up_force = 500; // add an up force when throwing a grenade

            gameObject.GetComponent<Rigidbody>().AddForce((transform.forward + (transform.up * up_throw_multiplier))
                * up_force);

            StartCoroutine(igniteGrenade());

        }
    }


   
    protected IEnumerator igniteGrenade()
    {
        yield return new WaitForSeconds(wait_before_ignite);

        explodable.nowExplode();
    }


}
