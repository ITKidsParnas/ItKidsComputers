using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NightDayControll : MonoBehaviour
{
    // Start is called before the first frame update
    public Light sun; // Ссылка на Directional Light
    public float dayLength = 1440f; // Длина дня в секундах

    private float rotationSpeed;

    void Start()
    {
        rotationSpeed = 360f / dayLength; // Угол вращения за секунду
    }

    void Update()
    {
        // Поворачиваем солнце
        sun.transform.Rotate(rotationSpeed * Time.deltaTime, 0, 0);
    }
}
