using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;


public class Menu : MonoBehaviour
{
    public void ChangeTime(float time )
    { 
        Time.timeScale = time;  
    }
    public void RestartButton()
{
    SceneManager.LoadScene(SceneManager.GetActiveScene().name);
}
    public void mainmenu() { SceneManager.LoadScene(0); }
    // Start is called before the first frame update
    void Start()
    {
        ChangeTime(1);  
    }

}
