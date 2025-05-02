using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class duckPlace : MonoBehaviour
{
    public GameObject door;
    public Transform place;
    // Start is called before the first frame update
    void Start()
    {
        
    }
    public void SetDuck(Transform duck)
    {
        duck.gameObject.SetActive(true);
        duck.GetComponent<MeshCollider>().enabled = false;
        door.SetActive(false);
        duck.position = place.position;
    }


    // Update is called once per frame
    void Update()
    {
        
    }
}
