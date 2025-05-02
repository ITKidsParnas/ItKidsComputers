using System;
using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UIElements;

public class earnCube : MonoBehaviour
{
    public CubeFallButton firstCubeFallButton;
    public CubeFallButton secondCubeFallButton;
    private void Update()
    {
        if (firstCubeFallButton.isCube || secondCubeFallButton.isCube)
        {
            transform.position = new Vector3(1000, 1000, 1000);
        }
    }
}
