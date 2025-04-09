using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class MavrodiMMM : MonoBehaviour
{
    public int [] mavrodiMMM;
    public GameObject [] ODGS;
   [TextArea] public string text;
        // Start is called before the first frame update
    void Start()
    {
        for (int  i=0; i<10; i++)
        {
            Debug.Log(text);
        }
    }
    private void OnCollisionEnter(Collision collision)
    {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        foreach (var item in ODGS)
        {
            item.SetActive(false);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }

}
