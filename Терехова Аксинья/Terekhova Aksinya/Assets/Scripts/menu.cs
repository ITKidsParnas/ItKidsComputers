using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class menu : MonoBehaviour
{
    public GameObject _menu;

    public void Continue()
    { 
        _menu.SetActive(false);
        Cursor.lockState = CursorLockMode.Locked;
    }
    public void Exit()
    {
            Application.Quit(); 
    }
    public void Restart ()
    {
        string sceneName = SceneManager.GetActiveScene().name ;
        SceneManager.LoadScene(sceneName);
    }
   
    void Start()
    {
            
    }


    void Update()
    {
        if(Input.GetKeyDown(KeyCode.Escape))
        {
            _menu.SetActive(true);
            Cursor.lockState = CursorLockMode.Confined;
        }
    }
}

