using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;



namespace DesignPatterns
{
    public class TriggerTest : MonoBehaviour
    {
        public int[] nums;
      
        private void OnTriggerExit(Collider other)
        {
            other.GetComponent<MeshRenderer>().materials[0].color = Color.white;

        }
        private void OnTriggerEnter(Collider other)
        {
            other.GetComponent<MeshRenderer>().materials[0].color = color;
        }
           public Color color;
        void Start()
        {
            Debug.Log(nums[252]);
        }


        void Update()
        {
            
        }
    }
}
