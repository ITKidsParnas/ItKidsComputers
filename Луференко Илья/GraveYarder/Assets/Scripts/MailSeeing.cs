using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.UI;
public class MailSeeing : MonoBehaviour
{
    public TextMeshProUGUI textMeshProUGUI;
    private bool isRead = false;
    private bool playerInTrigger = false; 
    public Image image;

    // Start is called before the first frame update
    void Start()
    {
        textMeshProUGUI.enabled = false; 
        image.enabled = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (playerInTrigger && Input.GetKeyDown(KeyCode.E) && !isRead)
        {
            textMeshProUGUI.enabled = true;
            image.enabled = true;
            isRead = true;
        }
        if (isRead && Input.GetKeyDown(KeyCode.Escape))
        {
            isRead = false;
            textMeshProUGUI.enabled = false;
            image.enabled = false;
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            playerInTrigger = true; 
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            playerInTrigger = false;
        }
    }
}
