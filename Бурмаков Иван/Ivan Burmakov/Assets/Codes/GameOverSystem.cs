using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class GameOverSystem : MonoBehaviour
{
    public float _timeToLoose;
    public float fadeSpeed;
    public Text _text;
    public Image image;
    private float _timer;
    private bool _isGameOver;
    public void Win()
    {
        if ( _isGameOver == false)
        {
            _isGameOver = true;
            StartCoroutine(FadeAndLoadSceneRoutine(new Color(1f, 1f, 1f, 0)));
        }
    }
    public void Loose()
    {
        if (_isGameOver == false)
        {
            _isGameOver = true;
            StartCoroutine(FadeAndLoadSceneRoutine(Color.clear));
        }
    }
    void Update()
    {
        _timer += Time.deltaTime;
        if (_timer >= _timeToLoose && _isGameOver == false)
        {
            _isGameOver = true;
            StartCoroutine(FadeAndLoadSceneRoutine(Color.clear));
        }
        else 
        {
            int minutes =(int)(_timeToLoose- _timer )/ 60; // Получаем целое количество минут
            int seconds = (int)(_timeToLoose-_timer) % 60;
            _text.text = minutes+":"+seconds;
        }
    }
    IEnumerator FadeAndLoadSceneRoutine(Color color)
    {
        image.color=color;  
        float alpha = 0f;
        while (alpha < 1f)
        {
            alpha += fadeSpeed * Time.deltaTime;
            image.color = new Color(image.color.r, image.color.g, image.color.b,alpha);
            yield return null;
        }
        yield return new WaitForSeconds(0.5f);
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
}
