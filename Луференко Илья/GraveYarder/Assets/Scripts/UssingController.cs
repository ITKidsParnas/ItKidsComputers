using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UssingController : MonoBehaviour
{
    public Material newMaterial;    
    private Material originalMaterial;
    private Renderer objectRenderer;
    private bool isPlayerInside = false;

    void Start()
    {

        objectRenderer = GetComponent<Renderer>();
        originalMaterial = objectRenderer.material;
    }

    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            isPlayerInside = true;
        }
    }

    void OnTriggerExit(Collider other)
    {

        if (other.CompareTag("Player"))
        {
            isPlayerInside = false;
        }
    }

    void Update()
    {
        if (isPlayerInside && Input.GetKeyDown(KeyCode.E))
        {
            if (objectRenderer.material == originalMaterial)
            {
                objectRenderer.material = newMaterial;
            }
            else
            {
                objectRenderer.material = originalMaterial;
            }
        }
    }
}
