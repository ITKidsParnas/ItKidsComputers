using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DoorClosing : MonoBehaviour
{
    public GameObject door;
    public Vector3 rotateDoor;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            DoorOpening.isOpened = false;
            door.transform.localRotation = Quaternion.Euler(rotateDoor);
        }
    }
}
