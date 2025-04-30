/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HooverBoardController : Collectable
{

    private HoverBoard hoverboard;

    [SerializeField]
    private Transform left_joystick;

    [SerializeField]
    private Transform right_joystick;

    // Start is called before the first frame update
    private void Start()
    {
        
        hoverboard = FindObjectOfType<HoverBoard>();
    }

    protected override void Update()
    {
        base.Update();

        simulateJoystickPlayerMovement();

        controlHoverboardUpDownMotion();

    }


    private void simulateJoystickPlayerMovement() // simulate left joystick movement based on player movement
    {
        if (hoverboard.is_player_engaged)
        {
            left_joystick.transform.localRotation = Quaternion.Euler(
            PlayerInput.instance.move_vector.z * -20,
            PlayerInput.instance.move_vector.x * -20,
            0

            );
        }
    }

    private void controlHoverboardUpDownMotion()
    {
        if (PlayerInput.instance.mouse_left_click && is_in_players_pocket && gameObject.activeSelf) // if we press down left mouse button while this object is in player hand
        {

            if (hoverboard.is_player_engaged) // if player is on hover board
            {
                right_joystick.transform.localRotation = Quaternion.Euler(-20, 0, 0);

                hoverboard.ascend(); // hoverboard should go up
            }
            else
            {

                hoverboard.isCalled(transform.position); // if player is not engaged, hoverboard should move to player position
            }
        }


        else if (PlayerInput.instance.mouse_right_click && is_in_players_pocket && gameObject.activeSelf) // if we press down right mouse button while this object is in player hand
        {
            if (hoverboard.is_player_engaged) // if player is on hoverboard
            {
                hoverboard.descend(); // hovervoard should go down
                right_joystick.transform.localRotation = Quaternion.Euler(20, 0, 0);

            }

        }
        else
        {
            
            right_joystick.transform.localRotation = Quaternion.Euler(0, 0, 0);

        }

    }
}
