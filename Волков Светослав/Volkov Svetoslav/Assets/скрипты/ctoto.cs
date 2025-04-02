using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ctotoN : MonoBehaviour
{
    public int[] masiv;
// Start is called before the first frame update
void Start()
{
    Debug.Log(masiv); 
        foreach (var item in masiv)
        {
            Debug.Log(-item);   
        }
    }

// Update is called once per frame
void Update()
{

}
}
