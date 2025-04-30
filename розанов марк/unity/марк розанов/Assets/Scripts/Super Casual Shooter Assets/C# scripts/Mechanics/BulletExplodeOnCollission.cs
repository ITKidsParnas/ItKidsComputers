/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(Explodable))]
public class BulletExplodeOnCollission : MonoBehaviour
{
    private Explodable explodable;

    [SerializeField]
    [Range(1,5)]
    private float expiry_time = 3;

    private float expiry_counter;

    private void Start()
    {
        explodable = gameObject.GetComponent<Explodable>();

    }

    private void Update()
    {
        expiry_counter += Time.deltaTime;

        if(expiry_counter >= expiry_time)
        {
            explodable.nowExplode();
        }
    }

    private void OnTriggerEnter(Collider other) // explode if this collides with a non trigger collider
    {
        if(!other.isTrigger) 
        {
            explodable.nowExplode();

        }

    }
}
