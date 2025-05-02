using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class mainmenu : MonoBehaviour
{
    private int _levelid = 1;
    public void Exit()
    {
        Application.Quit();
    }
    public void startgame()
    {
        SceneManager.LoadScene(_levelid);
    }
    public void LoadLevel( int levelId)
    {
        _levelid = levelId;
     //   SceneManager.LoadScene(levelId);
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
