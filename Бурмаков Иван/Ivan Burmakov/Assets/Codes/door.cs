using System;
using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UIElements;

public class door : MonoBehaviour
{
    public Button firstButton;
    public Button secondButton;
    private void Update()
    {
        if (firstButton.isCube && secondButton.isCube)
        {
            transform.position = new Vector3 (1000, 1000, 1000);
        }
    }
}
