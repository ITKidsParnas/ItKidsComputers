/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class HoverBoard : MonoBehaviour
{

    private GameObject player;

   

    [SerializeField]
    [Range(1, 5)]
    private float ride_with_player_speed = 3;

    [SerializeField]
    [Range(0.1f, 2)]
    private float move_todards_player_speed = 1f;


    [SerializeField]
    [Range(1, 50)]
    private float ascend_speed = 1f;


    [SerializeField]
    [Range(1, 20)]
    private float descend_speed = 1f;


    [SerializeField]
    [Range(1, 500)]
    private float maximum_fly_height = 30; // will not ascend beyond this point in the y axis


  
    public bool is_player_engaged
    {
        get;
        set;
    }


    private bool is_called;

    private Vector3 call_position;

    private void Start()
    {
        is_called = false;

        player = FindObjectOfType<PlayerInput>().gameObject;
    }

    public void isCalled(Vector3 call_position)
    {
        is_called = true;

        this.call_position = call_position;
    }

    // Update is called once per frame
    void Update()
    {
        if (is_player_engaged)
        {
            followPlayerOnFlatAxis();

        }
        else
        {
            if (is_called)
            {
                callHooverBoard();
            }
           
        }
    }

    public void callHooverBoard()
    {
        // move to player
        transform.position = Vector3.Lerp(transform.position, player.transform.position , move_todards_player_speed * Time.deltaTime);


        // if we get too close to player then stop moving towards player
        if(Vector3.Distance(transform.position, call_position) < 8)
        {
            is_called = false;
        }
    }

    // follow player on x and z axis
    private void followPlayerOnFlatAxis()
    {
        transform.position = Vector3.Lerp(transform.position,
            new Vector3(player.transform.position.x, transform.position.y, player.transform.position.z),
            ride_with_player_speed * Time.deltaTime);
    }

   

    public void ascend()
    {
        if(transform.position.y < maximum_fly_height)
        {
            transform.Translate(0, ascend_speed * Time.deltaTime, 0);
        }

    }


    public void descend()
    {
        transform.Translate(0, -descend_speed * Time.deltaTime, 0);

    }

  

    private void OnTriggerEnter(Collider other)
    {
        if(other.GetComponent<FirstPersonController>() )
        {
            is_player_engaged = true;

        }
       
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.GetComponent<FirstPersonController>())
        {
            is_player_engaged = false;

            is_called = false;
        }
    }

    

}
