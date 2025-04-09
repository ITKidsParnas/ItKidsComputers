using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class EndOfLevel : MonoBehaviour
{
    private void OnCollisionEnter(Collision collision)
    {
        var _inventory = collision.gameObject.GetComponent<inventory>();
        if (_inventory != null)
        {
            SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        }
    }
}

