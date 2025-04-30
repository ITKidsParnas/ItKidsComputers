/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AutomaticGun : Gun
{

    [SerializeField]
    private GameObject shoot_particle;


    [SerializeField]
    [Range(10,20)]
    private float shot_power=10; // the force that will be applied to rigidbodies shot by this gun


    [SerializeField]
    private float recoil_amplitude = 0.1f;

    [SerializeField]
    private float recoil_frequency = 30;


    protected override void shoot()
    {

        if (current_bullet > 0 && gameObject.activeSelf && is_in_players_pocket && PlayerInput.instance.mouse_left_click )
        {
            shoot_particle.SetActive(true);
            RaycastHit hit;

            
            current_bullet -= 1;

            if (Physics.Raycast(shoot_start_position.position, shoot_start_position.forward, out hit))
            {
                Damagable damagable = hit.collider.GetComponent<Damagable>();
                Rigidbody rbody = hit.collider.GetComponent<Rigidbody>();

                if (damagable) { hit.collider.GetComponent<Damagable>().takeDamage((int)gun_damage); }

                if(rbody) { hit.collider.GetComponent<Rigidbody>().AddForce((hit.point - shoot_start_position.position).normalized * shot_power); }
            }

        }
        else
        {
            shoot_particle.SetActive(false);
        }

    }



    protected override void Start()
    {
        base.Start();
    }

    // Update is called once per frame
    protected override void Update()
    {
        base.Update();

    }

}
