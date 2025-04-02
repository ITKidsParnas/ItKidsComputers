using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class poplach : MonoBehaviour
{
    public void ReStart()
    {
        string Scenname = SceneManager.GetActiveScene().name;
        SceneManager.LoadScene(Scenname);
    }
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
