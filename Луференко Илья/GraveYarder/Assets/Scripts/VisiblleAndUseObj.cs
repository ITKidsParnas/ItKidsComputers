using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class VisiblleAndUseObj : MonoBehaviour
{
    private Renderer itemRenderer; 
    private Color originalColor; 
    private bool isFading = false;
    public MeshRenderer itemMeshRenderer;
    private void Start()
    {
        itemRenderer = GetComponent<Renderer>();
        originalColor = itemRenderer.material.color;
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            StartFade();
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            StopFade();
        }
    }

    private void Update()
    {
        if (isFading && Input.GetKeyDown(KeyCode.E))
        {
            StartCoroutine(FadeOut());
        }   
    }

    private void StartFade()
    {
        isFading = true;
    }

    private void StopFade()
    {
        isFading = false;
    }

    private IEnumerator FadeOut()
    {
        float duration = 4f;
        float elapsedTime = 0f;
        Color targetColor = Color.black; 

        while (elapsedTime < duration)
        {
            elapsedTime += Time.deltaTime;
            // Темнеем
            itemRenderer.material.color = Color.Lerp(originalColor, targetColor, elapsedTime / duration);
            yield return null;
        }

        Color transparentColor = new Color(originalColor.r, originalColor.g, originalColor.b, 0);

        while (elapsedTime < duration)
        {
            elapsedTime += Time.deltaTime;
            itemRenderer.material.color = Color.Lerp(targetColor, transparentColor, elapsedTime / duration);
            yield return null; 
        }


        itemMeshRenderer.enabled = false;
    }
    
}

