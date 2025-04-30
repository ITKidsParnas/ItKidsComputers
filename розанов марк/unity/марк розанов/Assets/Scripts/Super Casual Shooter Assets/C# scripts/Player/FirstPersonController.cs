/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(CharacterController))]

public class FirstPersonController : MonoBehaviour
{

    [SerializeField]
    [Range(0,30)]
    private float movement_speed = 10; // movement speed of player


    [SerializeField]
    private Camera player_camera; // reference to the player camera


    private CharacterController character_controller; // the character controller
   

    private float vertical_velocity; // will be used to set player jump



    private float jump_height = 0.15f;
    

    private float gravity_scale = 0.03f;


    public bool is_player_moving
    {
        get;
        private set;
    }

    public bool is_player_grounded
    {
        get
        {
            return character_controller.isGrounded;
        }
    }

    // Use this for initialization
    void Start ()
    {
        character_controller = gameObject.GetComponent<CharacterController>();
        
	}
	
    public void movePlayer(Vector3 direction, Quaternion look, bool jump)
    {
        
        Vector3 move_vector = new Vector3(direction.x, 0, direction.z) * movement_speed * Time.deltaTime;

        transform.rotation = Quaternion.Euler(look.eulerAngles.x, look.eulerAngles.y, 0);

        move_vector = transform.rotation * move_vector; // player should adjust movement based on where its looking


        addPlayerGravity();
        


        if (jump && is_player_grounded)
        {
            setJump(jump_height);

        }

        is_player_moving = move_vector.magnitude > 0;

        Vector3 character_move = new Vector3(move_vector.x, vertical_velocity, move_vector.z);

        character_controller.Move(character_move);

    }

    private void addPlayerGravity()
    {
        if (!character_controller.isGrounded)
        {
            vertical_velocity += Physics.gravity[1] * Time.deltaTime * gravity_scale; // add gravity to player
        }
    }

    public void setJump(float lift)
    {
        if(character_controller.isGrounded)
        {
            vertical_velocity = lift;
        }
    }
}