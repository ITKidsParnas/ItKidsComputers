/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[RequireComponent(typeof(FirstPersonController))]
public class PlayerInput : MonoBehaviour
{
    public static PlayerInput instance;
    public static PlayerInput Instance
    {
        get
        {
            return instance;
        }
    }

    public PlayerCollectableManager player_collectable_manager;

    // are we controlling player or computer system
   
   
    private float player_look_up_down;
    private float player_look_left_right;



    public Vector3 move_vector
    {
        get;
        private set;
    }
    public Vector3 look_vector
    {
        get;
        private set;
    }
    private FirstPersonController fps;


    // player actions
    public bool jump
    {
        get;
        private set;
    }
   
    public bool mouse_left_click
    {
        get;
        private set;
    }
    public bool mouse_right_click
    {
        get;
        private set;
    }
    public bool interact
    {
        get;
        private set;
    }
    public bool disinteract
    {
        get;
        private set;
    }
    
    private const float max_look_up = 70, min_look_down = -70;
    
    [SerializeField]
    [Range(1, 6)]
    private float scroll_sensitivity = 1; // for the speed of mouse movement


    // Use this for initialization
    void Start ()
    {
        if(instance == null)
        {
            instance = this;
        }


        fps = gameObject.GetComponent<FirstPersonController>();


        Cursor.lockState = CursorLockMode.Locked; // lock Cursor
    }
	
	// Update is called once per frame
	void Update ()
    {
        jump = Input.GetKeyDown(KeyCode.Space);

        mouse_left_click = Input.GetAxis("Fire1") > 0;
        mouse_right_click = Input.GetAxis("Fire2") > 0;

        interact = Input.GetKeyDown(KeyCode.E);
        disinteract = Input.GetKeyDown(KeyCode.T);


        player_look_up_down += -(Input.GetAxis("Mouse Y") * scroll_sensitivity);
        player_look_left_right += (Input.GetAxis("Mouse X") * scroll_sensitivity);

        player_look_up_down = Mathf.Clamp(player_look_up_down, min_look_down, max_look_up);

        look_vector = new Vector3(player_look_up_down, player_look_left_right, 0);



        move_vector = new Vector3(Input.GetAxis("Horizontal"), 0, Input.GetAxis("Vertical"));

        fps.movePlayer(move_vector, Quaternion.Euler(look_vector), jump);

    }


}
