using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GraveDig : MonoBehaviour
{
    private bool isPlayerInTrigger = false;
    public Image fadeImage;
    private bool isFading = false;

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            isPlayerInTrigger = false; 
        }
    }
    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            isPlayerInTrigger = true;
        }
    }
    public void Update()
    {
        if (isPlayerInTrigger && Input.GetKeyDown(KeyCode.E) && !isFading)
        {
            StartCoroutine(FadeToBlack()); 
        }
    }

    private IEnumerator FadeToBlack()
    {
        isFading = true;
        float time = 0f;
        while (time < 1f)
        {
            time += Time.deltaTime / 3f;
            fadeImage.color = new Color(0, 0, 0, time);
            yield return null;
        }

        yield return new WaitForSeconds(1f);

        time = 1f;
        while (time > 0f)
        {
            time -= Time.deltaTime / 3f;
            fadeImage.color = new Color(0, 0, 0, time);
            yield return null;
        }

        isFading = false;
    }
}
