using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BlinkingLight : MonoBehaviour
{
    public Light blinkingLight; // Ссылка на компонент Light
    public float blinkInterval = 0.5f; // Интервал мигания в секундах
    public bool startOn = true; // Начинать во включенном состоянии

    private float timer;

    void Start()
    {
        if (blinkingLight == null)
        {
            // Если свет не назначен в инспекторе, попробуем получить его автоматически
            blinkingLight = GetComponent<Light>();
        }

        timer = 0f;
        blinkingLight.enabled = startOn;
    }

    void Update()
    {
        timer += Time.deltaTime;

        if (timer >= blinkInterval)
        {
            timer = 0f;
            blinkingLight.enabled = !blinkingLight.enabled; // Переключаем состояние света
        }
    }
}