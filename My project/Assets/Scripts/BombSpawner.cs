using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BombSpawner : MonoBehaviour
{
    public float timeToSpawn;
    public GameObject bomb;
    public Transform[] bombPoints;
    private float timer;
    void Update()
    {
        if (timer > timeToSpawn)
        {
            timer = 0;
            Instantiate(bomb, bombPoints[Random.Range(0, bombPoints.Length)].position, Quaternion.identity);

        }
        else 
        {
            timer += Time.deltaTime;
        }
    }
}
