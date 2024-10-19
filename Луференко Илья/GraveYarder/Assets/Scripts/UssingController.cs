using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UssingController : MonoBehaviour
{
    public Material newMaterial; // Новый материал, который будет применен
    private Material originalMaterial; // Оригинальный материал объекта
    private Renderer objectRenderer; // Рендерер объекта
    private bool isPlayerInside = false; // Флаг для отслеживания, находится ли игрок в триггере

    void Start()
    {
        // Получаем рендерер и оригинальный материал
        objectRenderer = GetComponent<Renderer>();
        originalMaterial = objectRenderer.material;
    }

    void OnTriggerEnter(Collider other)
    {
        // Проверяем, что триггер активирован игроком (или другим объектом)
        if (other.CompareTag("Player"))
        {
            isPlayerInside = true;
        }
    }

    void OnTriggerExit(Collider other)
    {
        // Проверяем, что игрок вышел из триггера
        if (other.CompareTag("Player"))
        {
            isPlayerInside = false;
        }
    }

    void Update()
    {
        if (isPlayerInside && Input.GetKeyDown(KeyCode.E))
        {
            // Проверяем, если текущий материал оригинальный, меняем на новый
            if (objectRenderer.material == originalMaterial)
            {
                objectRenderer.material = newMaterial;
            }
            else
            {
                // Если подняли новый материал, возвращаем оригинальный
                objectRenderer.material = originalMaterial;
            }
        }
    }
}
