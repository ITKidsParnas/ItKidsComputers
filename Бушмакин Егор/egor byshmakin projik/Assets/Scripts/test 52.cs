using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class test52 : MonoBehaviour
{
    public int[] lizard;
    // Start is called before the first frame update
    void Start()
    {
        foreach (var item in lizard)
        {
            Debug.Log(item);
        }
        for (int i = 0; i < 10; i++) {
            Debug.Log("сбер мега маркет... lol");

        }
    }

    public GameObject[] obgs;
    // Update is call,ed once per frame
    private void OnCollisionEnter(Collision collision)
    {
        foreach (var item in obgs)
        {
            item.SetActive(false);
        }
    }
    void Update()
    {

    }
}
