using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Menu : MonoBehaviour
{
    public GameObject menu;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {

        if (Input.GetKeyDown(KeyCode.Escape))
        {
            menu.SetActive(true);
            Cursor.lockState = CursorLockMode.Confined;
        }

    }

    public void Restart()
    {

        string SceneName = SceneManager.GetActiveScene().name;
        SceneManager.LoadScene(SceneName);

    }
    public void Exit()
    {

        Application.Quit();

    }
    public void Continue()
    {

        menu.SetActive(false);
        Cursor.lockState = CursorLockMode.Locked;

    }
}
