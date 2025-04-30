/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public abstract class Gun : Collectable
{

    [SerializeField]
    protected TMPro.TMP_Text bullet_display;
    
    [SerializeField]
    [Range(5, 5000)]
    protected int max_bullet; // maximim bullet in the gun
    
    [SerializeField]
    protected Transform shoot_start_position; // this is where the shoot raycast will start fromS


    
    [SerializeField]
    [Range(10, 1000)] 
    protected float gun_damage = 20; // the amount of damage the gun can do to a damagable

 

    public int current_bullet // the current number of bullets in the gun
    {
        get;
        protected set;
    }
    

    protected virtual void Start()
    {
        
        current_bullet = max_bullet; // initialliy, current bullet should be maximum
        
    }

    protected override void Update()
    {
        base.Update();

        shoot();
       
        if (is_in_players_pocket && gameObject.activeSelf)
        {
            showAimEffect();
        }

        displayBullet();
    }

    

    protected abstract void shoot(); // will have specific implementation depending on the type of gun


    protected virtual void displayBullet()
    {
        bullet_display.text = current_bullet + " / " + max_bullet;
    }


    // to accurately show where gun is aiming using the Aim texture
    private void showAimEffect()
    {
        
        RaycastHit hit;

        if(Physics.Raycast(shoot_start_position.position, shoot_start_position.forward, out hit))
        {
            AimTexture.Instance.setPosition( Camera.main.WorldToScreenPoint(hit.point));

        }
    }
}