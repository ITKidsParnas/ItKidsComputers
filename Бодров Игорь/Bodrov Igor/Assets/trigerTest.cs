using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class trigerTest : MonoBehaviour
{
    public int[] nums;
    public GameObject[] objects;
    public Color color;
      private void Start()
        
    {
        foreach (int num in nums) { Debug.Log(num); }
    }
    private void OnTriggerExit(Collider other)
    {
        other.GetComponent<MeshRenderer>().materials[0].color = Color.white;
        other.GetComponent<MeshRenderer>().materials[0].color = color;

        foreach (GameObject obj in objects) { obj.SetActive(false); }
    }
    private void OnTriggerEnter(Collider other)
    {
        other.GetComponent<MeshRenderer>().materials[0].color = color;
        foreach (GameObject obj in objects) { obj.SetActive(true); }

    }
    // Start is called before the first frame update


    // Update is called once per frame
    void Update()
    {
        
    }
}
