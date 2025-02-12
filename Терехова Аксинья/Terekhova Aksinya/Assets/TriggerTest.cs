using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;



namespace DesignPatterns
{
   
    public class TriggerTest : MonoBehaviour
    {
        public GameObject[] Objects ;
            
        public int[] nums;
        
        void Start()
        {
            foreach (int num in nums)
            {
                Debug.Log(num);
            }
        }
       
        private void OnTriggerExit(Collider other)
        {
            other.GetComponent<MeshRenderer>().materials[0].color = Color.white;
        foreach (GameObject obj in Objects) 
        {
                obj.SetActive(false);
        }
    }
        private void OnTriggerEnter(Collider other)
        {
            other.GetComponent<MeshRenderer>().materials[0].color = color;
        foreach (GameObject obj in Objects) 
        {
                obj.SetActive(true);
        }
    }
           public Color color;



        void Update()
        {
            
        }
    }
}
