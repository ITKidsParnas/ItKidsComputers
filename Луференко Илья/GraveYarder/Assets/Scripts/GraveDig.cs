using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GraveDig : MonoBehaviour
{
    public Image fadeImage; // Ссылка на изображение для затемнения
    private bool isFading = false;

    void OnTriggerEnter(Collider other)
    {
        // Проверяем, что объект, вошедший в триггер, - это игрок
        if (other.CompareTag("Player") && !isFading)
        {
            StartCoroutine(FadeToBlack());
        }
    }

    private IEnumerator FadeToBlack()
    {
        isFading = true;
        float time = 0f;

        // Затемняем экран
        while (time < 1f)
        {
            time += Time.deltaTime / 5f; // 5 секунд
            fadeImage.color = new Color(0, 0, 0, time); // Изменяем альфа-канал
            yield return null;
        }

        yield return new WaitForSeconds(1f); // Ждем 5 секунд с черным экраном

        // Возвращаем исходный вид
        time = 1f;
        while (time > 0f)
        {
            time -= Time.deltaTime / 5f; // 5 секунд
            fadeImage.color = new Color(0, 0, 0, time); // Изменяем альфа-канал
            yield return null;
        }

        isFading = false;
    }
}
