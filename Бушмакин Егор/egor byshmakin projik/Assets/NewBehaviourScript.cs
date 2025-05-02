using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    public bool canRepaint;
    public int number;
    public Color color;
    // Start is called before the first frame update
    void Start()
    {
        
    }
    
    private void OnCollisionEnter(Collision collision)
    {
        if (canRepaint)
        {
            GetComponent<MeshRenderer>().materials[0].color = color;
        }

        
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
