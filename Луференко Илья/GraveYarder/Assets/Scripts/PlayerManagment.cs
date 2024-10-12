using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class PlayerManagment : MonoBehaviour
{
 
    public float speed = 0.5f;
    public static float vertical, horizontal;
    public bool isSprint;
    public float pickUpRange = 2;
    public Transform itemHoldPosition;
    private GameObject currentItem;
    public GameObject player;
    private Vector3 playerTransform;
    public bool isItemPickUp = false;
    void Start()
    {
        isSprint = false;
    }
    void PickUpItem()
    {
        // Поиск предмета в области поднятия
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit hit;

        if (Physics.Raycast(ray, out hit, pickUpRange))
        {
            GameObject item = hit.collider.gameObject;

            // Убедитесь, что это именно предмет (добавьте нужные теги или идентификаторы)
            if (item.CompareTag("Item")) // Предполагаем, что у предметов есть тег "Item"
            {
                isItemPickUp = true;
                currentItem = item;
                item.transform.SetParent(itemHoldPosition); // Поднятие предмета
                item.transform.localPosition = player.transform.position; // Установка положения
                item.GetComponent<Rigidbody>().isKinematic = true; // Отключение физики
                
            }
        }
    }

    void ThrowItem()
    {
        isItemPickUp = false;
        currentItem.transform.SetParent(null); // Убираем предмет из родителя
        Rigidbody rb = currentItem.GetComponent<Rigidbody>();
        if (rb != null)
        {
            rb.isKinematic = false; // Включаем физику для выбрасываемого предмета
            rb.AddForce(Camera.main.transform.forward * 2); // Выбрасываем предмет вперед
        }

        currentItem = null; // Сбрасываем текущий элемент

    }
    void Update()
    {
        var playerPos = player.transform.position;
        horizontal = Input.GetAxis("Horizontal") * speed * Time.deltaTime;
        vertical = Input.GetAxis("Vertical") * speed * Time.deltaTime;
        transform.Translate(horizontal, 0, 0);
        transform.Translate(0, 0, vertical);
        playerPos = playerTransform;
        if (Input.GetKeyDown(KeyCode.LeftShift))
        {
            if (!isSprint)
            {
                speed = 10;
                isSprint = true;
            }
            else
            {
                speed = 5;
                isSprint = false;
            }
        }
        if (Input.GetKeyDown(KeyCode.E))
        {
            if (currentItem == null)
            {
                PickUpItem();
            }
            else
            {
                ThrowItem();
            }
        }

        if (isItemPickUp)
        {
            currentItem.transform.localPosition = playerPos;
        }
       
    }
}

