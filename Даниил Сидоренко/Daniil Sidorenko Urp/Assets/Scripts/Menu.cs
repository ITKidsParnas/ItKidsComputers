using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Menu : MonoBehaviour
{
    public GameObject menu;
    public FirstPersonController controller;
    // Start is called before the first frame update
    void Start()
    {
        Cursor.lockState = CursorLockMode.Locked;
        Time.timeScale = 1.0f;
    }
    public void Restart()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }   
    public void Exit()
    {
        Application.Quit();
    }
    public void Continue()
    {
        Cursor.lockState = CursorLockMode.Locked;
        menu.SetActive(false);
        Time.timeScale = 1.0f;
        controller.enabled = true;
    }
    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            Cursor.lockState = CursorLockMode.Confined;
            menu.SetActive(true);
            Time.timeScale = 0f;
            controller.enabled = false;
        }
    }
}
