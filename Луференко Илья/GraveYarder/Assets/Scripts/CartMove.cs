using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CartMove : MonoBehaviour
{

    private float speed = 0.1f; // Скорость движения
    public GameObject cart;
    void Start()
    {
        StartCoroutine(MoveCart()); // Запускаем корутину для движения
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Finish"))
        {
            speed = 0;
        }
    }
    private void Update()
    {
        
    }
    private IEnumerator MoveCart()
    {
        while (true)
        {
            yield return new WaitForSeconds(0.01f); // Ждем немного перед следующим движением
            transform.position += new Vector3(speed, 0, 0); // Двигаем объект
        }
    }
    


    


}
