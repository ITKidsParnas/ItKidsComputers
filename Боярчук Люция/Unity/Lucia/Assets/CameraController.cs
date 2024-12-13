using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject camera;
    public Material cameraMaterial;
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(KeyCode.F)) 
        { 
            
        }
        if (Input.GetKey(KeyCode.E))
        {
            Texture2D screenImage = new Texture2D(Screen.width, Screen.height);
            screenImage.ReadPixels(new Rect(0, 0, Screen.width, Screen.height), 0, 0);
            screenImage.Apply(); 
        }
        if (Input.GetKey(KeyCode.Q))
        {
            camera.SetActive(!camera.activeInHierarchy);
        }
    }
}
