/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class AimTexture : MonoBehaviour
{

    private static AimTexture instance;

    public static AimTexture Instance
    {
        get
        {
            return instance;
        }
    }

    private RectTransform rect_transform;


    // Start is called before the first frame update
    void Start()
    {
        if(instance == null)
        {
            instance = this;
        }

        rect_transform = GetComponent<RectTransform>();

        setActive(false);
        
    }

    public void setActive(bool active)
    {
        gameObject.SetActive(active);
    }

    public void setPosition(Vector3 position)
    {
        rect_transform.position = position;
    }

}
