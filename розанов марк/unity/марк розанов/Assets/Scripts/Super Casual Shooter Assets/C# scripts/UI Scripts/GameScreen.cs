/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;


public class GameScreen : MonoBehaviour
{

    [SerializeField]
    protected Image health_bar;

    [SerializeField] 
    private Text health_percent_text;


    [SerializeField]
    private Damagable player_damagable;

    

    // Update is called once per frame
    private void Update()
    {
        updateHealthUI();

    }



    // Update is called once per frame
    protected void updateHealthUI()
    {
       // fill bar based on health
        health_bar.fillAmount = player_damagable.getCurrentHealth() / player_damagable.getMaxHealth();

        //Green Red color spectrum.  red represents low health, green represents high health
        health_bar.color = Color.Lerp(Color.red, Color.green, (float)player_damagable.getCurrentHealth() / (float)player_damagable.getMaxHealth());

        health_percent_text.text = ((float)player_damagable.getCurrentHealth() / (float)player_damagable.getMaxHealth() * 100).ToString("n0") + " %";
    }



    public void reloadScene()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);

    }
}
