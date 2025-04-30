/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/



using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


[RequireComponent(typeof(Damagable))]
public class PlayerBleed : MonoBehaviour
{
    private Damagable damagale; // referece to damagable


    [SerializeField]
    private Image bleed_image; // the bleed image



    [SerializeField]
    private Color bleed_color; // the bleed color


    [SerializeField]
    [Range(0,1)]
    private float maximum_bleed_alpha; // maximum alpha for the bleed color image

    private float current_image_alpha; 

    private void Start()
    {
        damagale = GetComponent<Damagable>();
    }


    private void Update()
    {

        // set bleed alpha based on the damage effect counter
        current_image_alpha = (damagale.getCurrentDamageEffectCounter() / damagale.getMaxDamageEffectCounter()) * maximum_bleed_alpha;

        
        bleed_image.color = getTransparentOfColor(bleed_color, current_image_alpha);
    }

    private Color getTransparentOfColor (Color color, float alpha)
    {
        return new Color(color.r, color.g, color.b, alpha);
    }
}
