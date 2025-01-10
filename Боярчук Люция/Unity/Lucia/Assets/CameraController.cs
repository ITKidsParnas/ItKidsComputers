using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject camera;
    public GameObject cameraScreen;
    public GameObject shot;
    public GameObject scope;
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.F)) // scope
        {
            scope.SetActive(!scope.activeInHierarchy);
            camera.SetActive(!scope.activeInHierarchy);
        }
        if (Input.GetKeyDown(KeyCode.E))  // take shot
        {
            //Texture2D screenImage = new Texture2D(Screen.width, Screen.height);
            //screenImage.ReadPixels(new Rect(0, 0, Screen.width, Screen.height), 0, 0);
            //screenImage.Apply();
            //cameraScreen.materials[0].mainTexture = screenImage;
            //cameraScreen.materials[0].color = Color.white;
            cameraScreen.gameObject.SetActive(!cameraScreen.activeInHierarchy);// todo rework
        }
        if (Input.GetKeyDown(KeyCode.Q))   // hide or show camera
        {
            camera.SetActive(!camera.activeInHierarchy);
        }
        if (Input.GetKeyDown(KeyCode.Z))   // look at shot
        {
            shot.SetActive(!shot.activeInHierarchy);

        }
    }
}
