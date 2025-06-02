
using UnityEngine;
using UnityEngine.SceneManagement;

public class DestroyTrigger : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        if (other.GetComponent<DontTestractsbleObject>()) return;
        if (other.GetComponent<Bomb>()) return;
        if (other.GetComponent<DestroyTrigger>()) return;
        if (other.GetComponent<FirstPersonController>())
        {
            SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        }
        Destroy(other.gameObject);
        Destroy(gameObject.GetComponent<Collider>());
    }
}
