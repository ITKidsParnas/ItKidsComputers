
using UnityEngine;

public class arrayTest : MonoBehaviour
{
    public GameObject[] array ;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
for (int i = 0; i <10; i++)
        {
            
        } 
    }
    private void OnCollisionEnter(Collision collision)
    {
        foreach (var item in array)
        {
            item.SetActive(false);
        } 
    }
    // Update is called once per frame
    void Update()
    {
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   `                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    }
}
