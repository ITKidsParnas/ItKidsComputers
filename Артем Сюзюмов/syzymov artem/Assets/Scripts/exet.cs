using CharacterScript;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class exet : MonoBehaviour
{
    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.GetComponent<FPSController>() != null) { SceneManager.LoadScene(SceneManager.GetActiveScene().name); }
    }
    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.GetComponent<FPSController>() != null) { SceneManager.LoadScene(SceneManager.GetActiveScene().name); }
    }
}
