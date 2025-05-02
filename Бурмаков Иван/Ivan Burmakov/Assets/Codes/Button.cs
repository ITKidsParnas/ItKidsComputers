
using UnityEngine;


    public class Button : MonoBehaviour
    
{
    public bool isCube;

    private void OnCollisionEnter(Collision collision)
    {
        var cube = collision.gameObject.GetComponent<cube>();
        if (cube!= null)
        {
            isCube = true;
        }
    }
    private void OnCollisionExit(Collision collision)
    {
        var cube = collision.gameObject.GetComponent<cube>();
        if (cube!= null)
        {
            isCube = false;
        }
    }
}
