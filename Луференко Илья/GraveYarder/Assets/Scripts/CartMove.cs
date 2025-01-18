using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CartMove : MonoBehaviour
{

    private float speed = 0.1f; // Скорость движения
    private bool isMoving = true; // Переменная для управления движением
    public GameObject cart;
    public Vector3 currentPos;
    void Start()
    {
        StartCoroutine(MoveCart()); // Запускаем корутину для движения
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Finish"))
        {
            StopMovement(); // Останавливаем движение
        }
    }
    private void Update()
    {
        currentPos = cart.transform.position;
        if (currentPos.x == -23)
        {
            isMoving = false;
        }
    }
    private IEnumerator MoveCart()
    {
        while (true)
        {
            yield return new WaitForSeconds(0.01f); // Ждем немного перед следующим движением

            if (isMoving) // Проверяем, движется ли объект
            {
                transform.position += new Vector3(speed, 0, 0); // Двигаем объект
            }
        }
    }
    

    public void StopMovement()
    {
        isMoving = false; // Устанавливаем флаг остановки
        Debug.Log("Cart stopped.");
    }

    


}
