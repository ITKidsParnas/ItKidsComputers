/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

[RequireComponent(typeof(LineRenderer))]
public class LaserGun : Gun
{
    private float count_shooting = 0;
    

    [SerializeField]
    private Image shoot_load_prefab;

    private Image shoot_load;

    [SerializeField]
    public int count_additive = 10;

  
    protected LineRenderer shoot_line
    {
        get
        {
            return gameObject.GetComponent<LineRenderer>();
        }
    }


    protected override void Start()
    {
        base.Start();

        shoot_load = Instantiate(shoot_load_prefab); // instantiate a shoot load. shoot load object is a UI image that shows the damage progress of a laser gun

    }

    // Update is called once per frame
    protected override void Update()
    {
        base.Update();

        if(is_in_players_pocket)
        {
            shoot_start_position.rotation = transform.parent.rotation;
            shoot_load.transform.SetParent(FindObjectOfType<GameScreen>().transform, false);
        }

       
    }

    protected override void shoot()
    {
        if (gameObject.activeSelf && is_in_players_pocket && PlayerInput.instance.mouse_left_click && current_bullet >0)
        {

           

            current_bullet -= 1;

            RaycastHit hit;

            
            if (Physics.Raycast(shoot_start_position.position, shoot_start_position.forward, out hit))
            {
                if (hit.collider.gameObject.GetComponent<Damagable>() != null)
                {
                    count_shooting += count_additive * Time.deltaTime; // if we hit a damagable, keep adding to count shooting
                    if (count_shooting > hit.collider.gameObject.GetComponent<Damagable>().getMaxHealth())
                    {
                        // only when count shooting has reached the maximum damage the damagable can take
                        // that is when we can inflict full damage on the damagable
                        hit.collider.gameObject.GetComponent<Damagable>().takeDamage((int)count_shooting); 
                    }


                    shoot_load.gameObject.SetActive(true);

                    shoot_load.GetComponent<Image>().fillAmount = count_shooting / hit.collider.gameObject.GetComponent<Damagable>().getMaxHealth();

                }
                else
                {
                    count_shooting = 0;
                    
                    shoot_load.gameObject.SetActive(false);
                }

                 // used for line render to show line from shoot start position to hit point
                shoot_line.enabled = true;
                Vector3[] shoot_poses = new Vector3[] 
                {
                    shoot_start_position.position, hit.point
                };

                shoot_line.SetPositions(shoot_poses);

                
            }
        }
        else
        {
            shoot_line.enabled = false;

            shoot_load.gameObject.SetActive(false);
        }
    }




}