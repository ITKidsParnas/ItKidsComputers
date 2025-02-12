using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;

public class MobSpawn : MonoBehaviour
{
    int objectCount = 0;
    int maxObjects = 5;
    public GameObject mob;
    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine(SpawnRoutine());
    }

    // Update is called once per frame
    void Update()
    {

    }
    void SpawnObject()
    {
        if (objectCount < maxObjects)
        {
            Vector3 randomPosition = new Vector3(
                Random.Range(4f, 11f),
                -1.05f, // или другая высота, если нужно
                Random.Range(4f, 11f)
            );
            Instantiate(mob, randomPosition, Quaternion.identity);
            objectCount++;
        }
    }

    IEnumerator SpawnRoutine() {
       while (objectCount < maxObjects) {
           SpawnObject();
           yield return new WaitForSeconds(1f);
       }
   }
}
