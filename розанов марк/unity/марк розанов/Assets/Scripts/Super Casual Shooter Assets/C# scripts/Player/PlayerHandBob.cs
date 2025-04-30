/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class PlayerHandBob : MonoBehaviour
{
    private float counter;

    private Vector3 default_hand_position;


    [SerializeField]
    private float amplitude;

    [SerializeField]
    private float frequency;


    [SerializeField]
    private float jump_height;

    private FirstPersonController controller;

    // Start is called before the first frame update
    void Start()
    {
        controller = GetComponentInParent<FirstPersonController>();

        default_hand_position = transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        if(controller.is_player_moving && controller.is_player_grounded)
        {
            bobHand();
        }
    }

    private void bobHand()
    {
        if (counter < (2 * Mathf.PI) / frequency) // this basically simulates repeated sine wave oscilation
        {
            counter += Time.deltaTime;
        }
        else
        {
            counter = 0;
        }

        transform.position += new Vector3(0, amplitude * Mathf.Sin(counter * frequency), 0);
    }
}
