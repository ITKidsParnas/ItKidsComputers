/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(Rigidbody))]
[RequireComponent(typeof(Damagable))]
[RequireComponent(typeof(LineRenderer))]


public class EnemyDrone : MonoBehaviour
{

    [SerializeField]
    [Range(1, 6)]
    private int attack_time; // time in secoonds the drone spends attacking player before cooling down


    [SerializeField]
    [Range(1, 4)]
    private int cool_down_time; // time it takes in seconds for drone to cool down


    private Rigidbody rigid_body; // rigidbody reference
    private LineRenderer shoot_line; // line renderer reference



    public Transform player { get; set; } // access to player

   
    [SerializeField]
    [Range(0,1)]
    private float attack_value = 0.1f; // damage to inflict on player


    private float action_counter; // track time in seconds to switch between drone actions. attacking or cooling dowwn

    private bool is_dead; // if drone is dead



    private void Start()
    {
        shoot_line = GetComponent<LineRenderer>();

        rigid_body = GetComponent<Rigidbody>();
    }



    // Update is called once per frame
    private void Update()
    {
        transform.LookAt(player);

        if (!is_dead)
        {
            // basically, what is happening here is that while drone is attacking player, there is a force added to the drone to move towards the player
            // when drone is not attacking player, it simply cools down by moving on a random vector, after cool down, attack continues, and so on.
            if (action_counter >= attack_time) 
            {

                
                rigid_body.AddForce(Vector3.one * UnityEngine.Random.Range(0, 1));

                shoot_line.enabled = false;

                StartCoroutine(coolDown());


            }
            else
            {
                action_counter += Time.deltaTime;

                rigid_body.AddForce((player.transform.position - transform.position).normalized);

                attack();

            }
        }
    }

    private IEnumerator coolDown()
    {

        yield return new WaitForSeconds(cool_down_time);

        action_counter = 0;
    }


    private void attack()
    {
        
        RaycastHit hit;
        Damagable damagable;

        // attack the player and cause damage
        if (Physics.Raycast(transform.position, transform.forward, out hit, 200))
        {
            damagable = hit.collider.gameObject.GetComponent<Damagable>();
            if (damagable != null)
            {
                damagable.takeDamage(attack_value);

                Vector3[] shoot_line_points = new Vector3[] 
                {
                    transform.position, hit.point // draw line from this object to the hit point
                };

                shoot_line.enabled = true;
                shoot_line.SetPositions(shoot_line_points);

            }
        }
    }

    public void onDeath() // when drone runs out of health, this function basically simulates the destruction of the drone when dead
    {
        shoot_line.enabled = false; // disable the shoot line


        Destroy(gameObject, 3); // destroy game object in 3 seconds

        // before we destroy the object, let us add convex mesh colliders and rigid bodies to the child transforms to simulate destruction like the drone broke to pieces
        foreach (Transform children_transforms in gameObject.GetComponentsInChildren<Transform>())
        {
            children_transforms.transform.SetParent(null);
            children_transforms.gameObject.AddComponent<MeshCollider>().convex=true;

            if (!children_transforms.GetComponent<Rigidbody>())
            {
                children_transforms.gameObject.AddComponent<Rigidbody>();
            }

            Destroy(children_transforms.gameObject, 2);

        }
    }

    
}