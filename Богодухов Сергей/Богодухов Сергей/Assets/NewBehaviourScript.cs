using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class CameraSwitcher : MonoBehaviour
{
    public int number;
    public Color color;
    public bool canRepaint;
    // Start is called before the first frame update
    void Start()
    {

    }
    
    // Update is called once per frame
    void Update()
    {

    }
    private void OnCollisionEnter(Collision collision)
    { if (canRepaint) {
               
        GetComponent<MeshRenderer>().materials[0].color = color;
        }
    }
}