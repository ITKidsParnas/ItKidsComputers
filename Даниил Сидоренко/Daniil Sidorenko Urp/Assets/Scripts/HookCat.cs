using System.Runtime.InteropServices;
using UnityEngine;

public class HookCat : MonoBehaviour
{
    public float speed;
    public float distance;
    private FirstPersonController controller;
    private Rigidbody controllerRb;
    private Vector3 hookedPossition;
    private bool isHooked;// Start is called before the first frame update
    private LineRenderer lineRenderer;
    void Start()
    {
        lineRenderer = GetComponent<LineRenderer>();
        controller = GetComponent<FirstPersonController>();
        controllerRb = GetComponent<Rigidbody>();   
    }

    // Update is called once per frame
    void Update()
    {
        if (isHooked)
        {
            if (Vector3.Distance(transform.position, hookedPossition) < distance)
            {
                isHooked = false;
                controllerRb.isKinematic = false;
                controller.playerCanMove = true;
                lineRenderer.enabled = false;
            }
            else 
            {
                lineRenderer.SetPosition(0, Camera.main.transform.position+Vector3.down);
                lineRenderer.SetPosition(1, hookedPossition);
                transform.position = Vector3.MoveTowards(transform.position, hookedPossition,Time.deltaTime*speed);
            }
        }
        else
        {
            if (Input.GetMouseButtonDown(0))
            {
                RaycastHit hit;
                // Does the ray intersect any objects excluding the player layer
                if (Physics.Raycast(Camera.main.transform.position, Camera.main.transform.TransformDirection(Vector3.forward), out hit, Mathf.Infinity))
                {
                    Debug.DrawRay(transform.position, transform.TransformDirection(Vector3.forward) * hit.distance, Color.yellow);
                    Debug.Log("Did Hit");
                    isHooked = true;
                    hookedPossition = hit.point;
                    controllerRb.isKinematic = true;
                    controller.playerCanMove = false;
                    lineRenderer.enabled = true;
                }
                else
                {
                    Debug.DrawRay(transform.position, transform.TransformDirection(Vector3.forward) * 1000, Color.white);
                    Debug.Log("Did not Hit");
                }
            }
        }
    }
}
