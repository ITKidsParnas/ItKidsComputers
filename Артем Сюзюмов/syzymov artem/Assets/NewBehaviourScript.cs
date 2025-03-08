using System.Collections;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    public bool isRepaint; 
    public Color color;
    public Rigidbody boby;
    public int[] nums;
    //int целые числа 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84
    //flot дробные числа 
    //string строка 
    // bool tru false
    private void Start()
    {
        //foreach (var item in nums)
        //    Debug.Log(item);
        //}
        //Debug.Log(nums[0]);
        for (int i = 1; i < nums.Length; i++)
        {
            Debug.Log(nums[i - 1] * nums[i]);
        }
    }
    private void OnCollisionEnter(Collision collision)
    {
        if (isRepaint)     
        {          
           GetComponent<MeshRenderer>().materials[0].color = Color.blue;  
        }
        
        
    }
    //private void OnCollisionExit(Collision collision)
    //{
    //     GetComponent<MeshRenderer>().materials[0].color = Color.black;
    //}
}
