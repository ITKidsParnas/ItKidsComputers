using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class trigerTest : MonoBehaviour
{
    public int[] nums;
    public Color color;
      private void Start()
    {
        Debug.Log(nums[0]);
    }
    private void OnTriggerExit(Collider other)
    {
        other.GetComponent<MeshRenderer>().materials[0].color = Color.white;
    }
    private void OnTriggerEnter(Collider other)
    {
        other.GetComponent<MeshRenderer>().materials[0].color = color;

    }
    // Start is called before the first frame update


    // Update is called once per frame
    void Update()
    {
        
    }
}
