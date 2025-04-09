using UnityEngine;

public class PortalTrigger : MonoBehaviour
{
    [SerializeField] private Canvas _winCanvas;
    private void OnTriggerEnter(Collider other)
    {
        var player = other.GetComponent<FirstPersonController>();
        if (player != null)
        {
            _winCanvas.gameObject.SetActive(true);
        }

    }
}
