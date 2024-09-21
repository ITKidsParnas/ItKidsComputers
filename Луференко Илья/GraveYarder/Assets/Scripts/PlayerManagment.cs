using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerManagment : MonoBehaviour
{
    private CharacterController controller;

    public float speed = 5f;
    public float gravity = -9.81f;
    public float jumpHeight = 1.5f;
    public GameObject cam;

    private Vector3 velocity;
    private bool isGrounded;

    void Start()
    {
        controller = GetComponent<CharacterController>();
    }

    void Update()
    {
        var camRotation = cam.transform.rotation;
        isGrounded = controller.isGrounded;

        if (isGrounded && velocity.y < 0)
        {
            velocity.y = 0f;
        }

        float moveX = Input.GetAxis("Horizontal");
        float moveZ = Input.GetAxis("Vertical");

        Vector3 move = transform.right * moveX + transform.forward * moveZ;

        controller.Move(move * speed * Time.deltaTime);

        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            velocity.y += Mathf.Sqrt(jumpHeight * -2f * gravity);
        }

        velocity.y += gravity * Time.deltaTime;

        controller.Move(velocity * Time.deltaTime);

        gameObject.transform.localRotation = camRotation;
    }
}
