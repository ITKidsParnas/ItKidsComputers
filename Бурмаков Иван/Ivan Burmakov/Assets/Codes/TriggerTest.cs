using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class TriggerTest : MonoBehaviour
{
    public Color color;
    public int[] nums;
    public GameObject[] objects;

    private void OnTriggerEnter(Collider other)
    {
        other.GetComponent<MeshRenderer>().materials[0].color = color;
        foreach (GameObject obj in objects) { obj.SetActive(true); }
    }

    private void OnTriggerExit(Collider other)
    {
        other.GetComponent<MeshRenderer>().materials[0].color = Color.white;
        foreach (GameObject obj in objects) { obj.SetActive(false); }
    }

    // Start is called before the first frame update
    private void Start()
    {
        //Debug.Log(nums[0]);
        //foreach (int num in nums) { Debug.Log(num); }
        for (int i = 1; i < nums.Length; i++)
        {
            Debug.Log(nums[i - 1] * nums[i]);
        }

    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
