using System.Collections;
using System.Collections.Generic;
using Unity.Burst.CompilerServices;
using UnityEngine;
using UnityEngine.UI;

public class TransformObjectSystem : MonoBehaviour
{
    public Transform targetPosition; // Точка, куда будет двигаться объект
    public float moveSpeed = 3f;
    public KeyCode interactKey = KeyCode.E;

    private Outline outline;
    private bool isMoving = false;
    private bool playerNearby = false;
    public Material lockIn;
    public GameObject obj;

    private void Start()
    {
        outline = GetComponent<Outline>();
        if (outline != null) outline.enabled = false;
    }

    private void Update()
    {
        if (playerNearby && Input.GetKeyDown(interactKey))
        {
            isMoving = true;
        }

        if (isMoving)
        {
            MoveToTarget();
        }
    }

    private void MoveToTarget()
    {
        transform.position = Vector3.MoveTowards(transform.position, targetPosition.position, moveSpeed * Time.deltaTime);

        if (Vector3.Distance(transform.position, targetPosition.position) < 0.1f)
        {
            isMoving = false;
        }
        
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            playerNearby = true;
            if (outline != null) outline.enabled = true;
            obj.GetComponent<Renderer>().material = lockIn;
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            playerNearby = false;
            if (outline != null) outline.enabled = false;
            obj.GetComponent<Renderer>().material = null;
        }
    }
}
