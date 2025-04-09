using UnityEngine;

public class UIMenuBase : MonoBehaviour
{
    [SerializeField] private FirstPersonController firstPersonController;
    private void OnEnable()
    {
       // firstPersonController.lockCursor = false;
        firstPersonController.enabled = false;
        Cursor.lockState = CursorLockMode.Confined;
    }
    private void OnDisable()
    {
        //firstPersonController.lockCursor = true;
        firstPersonController.enabled = true;
        Cursor.lockState = CursorLockMode.Locked;
    }
}
