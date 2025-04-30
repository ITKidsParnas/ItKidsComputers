/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[RequireComponent(typeof(SphereCollider))]
public class EnemyDroneMaker : MonoBehaviour
{

    [SerializeField]
    private Transform player;


    [SerializeField]
    private Transform drone_position; // position to launch drone from



    [SerializeField]
    [Range(1, 6)] private int number_of_enemy_drones = 1; // number of drones to launch at once



    [SerializeField]
    protected EnemyDrone[] villain_drone_prefabs; // prefabs for enemy drones




    private void OnTriggerEnter(Collider other) // when player comes near this drone maker, spawn a random drone
    {
        if(other.gameObject == player.gameObject)
        {
            for(int i=0; i < number_of_enemy_drones; i++)
            {
                spawnRandomDrone();
            }
        }
    }

    private void spawnRandomDrone()
    {
        int rand = UnityEngine.Random.Range(0, villain_drone_prefabs.Length - 1);

        EnemyDrone drone =  Instantiate(villain_drone_prefabs[rand], drone_position.position, Quaternion.identity);

        drone.player = player;

    }

}
