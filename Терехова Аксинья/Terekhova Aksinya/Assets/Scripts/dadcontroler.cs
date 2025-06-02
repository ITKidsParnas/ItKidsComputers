using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;



namespace DesignPatterns
{
    public class dadcontroler : MonoBehaviour
    {
        private void OnCollisionEnter(Collision collision)
        {
            if (collision.gameObject.GetComponent<FirstPersonController>() != null) { 
                SceneManager.LoadScene(SceneManager.GetActiveScene().name);
            }
        }
    }
}
