using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class PlayerManagment : MonoBehaviour
{
    private float sprintMultiplier = 2f; 
    private float moveSpeed = 20f;
    private Rigidbody rb;
    public float speed = 0.5f;
    public static float vertical, horizontal;
    public bool isSprint;
    public float pickUpRange = 2;
    public Transform itemHoldPosition;
    private GameObject currentItem;
    public GameObject player;
    private Vector3 playerTransform;
    public static bool isItemPickUp = false;
    public Transform cameraTransform;
    void Start()
    {
        isSprint = false;
        rb = GetComponent<Rigidbody>();
    }
    void PickUpItem()
    {
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit hit;

        if (Physics.Raycast(ray, out hit, pickUpRange))
        {
            GameObject item = hit.collider.gameObject;
            if (item.CompareTag("Item")) 
            {
                isItemPickUp = true;
                currentItem = item;
                item.transform.SetParent(itemHoldPosition);
                item.transform.localPosition = player.transform.position;
                item.GetComponent<Rigidbody>().isKinematic = true;
                
            }
        }
    }

    void ThrowItem()
    {
        
        currentItem.transform.SetParent(null);
        Rigidbody rb = currentItem.GetComponent<Rigidbody>();
        if (rb != null)
        {
            rb.isKinematic = false;
            rb.AddForce(Camera.main.transform.forward * 2);
            isItemPickUp = false;
        }

        currentItem = null;

    }

    private void Move()
    {
        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");

        // Создаем вектор движения
        Vector3 movement = new Vector3(moveHorizontal, 0.0f, moveVertical);

        // Нормализуем вектор, чтобы избежать ускорения при движении по диагонали
        if (movement.magnitude > 1)
        {
            movement.Normalize();
        }

        // Определяем текущую скорость
        float currentSpeed = moveSpeed;

        // Увеличиваем скорость при спринте
        if (Input.GetKey(KeyCode.LeftShift))
        {
            currentSpeed *= sprintMultiplier;
        }

        // Поворачиваем игрока в направлении камеры
        Vector3 cameraForward = cameraTransform.forward; // Получаем вектор вперед от камеры
        cameraForward.y = 0; // Убираем вертикальную составляющую
        Vector3 cameraRight = cameraTransform.right; // Получаем вектор вправо от камеры

        // Вычисляем новое направление движения игрока на основе направления камеры
        Vector3 desiredDirection = cameraForward * movement.z + cameraRight * movement.x;

        // Если направление не нулевое, поворачиваем игрока
        if (desiredDirection.magnitude > 0)
        {
            Quaternion targetRotation = Quaternion.LookRotation(desiredDirection);
            transform.rotation = Quaternion.Slerp(transform.rotation, targetRotation, Time.deltaTime * 10f); // Плавный поворот
        }

        // Применяем движение к Rigidbody
        rb.MovePosition(transform.position + desiredDirection.normalized * currentSpeed * Time.deltaTime);
    }
    void Update()
    {
        Move();
        var playerPos = player.transform.position;
        playerPos = playerTransform;
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

