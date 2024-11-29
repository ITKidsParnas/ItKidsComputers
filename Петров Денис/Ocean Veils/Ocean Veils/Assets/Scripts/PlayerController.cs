using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float speed = 5f; // Скорость перемещения игрока
    public float gravity = -9.81f; // Сила тяжести
    private CharacterController characterController; // Компонент CharacterController
    private Vector3 velocity; // Вектор для хранения движения

    void Start()
    {
        // Получаем ссылку на компонент CharacterController
        characterController = GetComponent<CharacterController>();
    }

    void Update()
    {
        // Обработка пользовательского ввода
        MovePlayer();
        HandleGravity();
    }

    // Метод для перемещения игрока
    private void MovePlayer()
    {
        // Получение ввода от клавиатуры
        float moveX = Input.GetAxis("Horizontal"); // A/D или стрелки влево/вправо
        float moveZ = Input.GetAxis("Vertical"); // W/S или стрелки вверх/вниз

        // Создаем вектор движения
        Vector3 move = transform.right * moveX + transform.forward * moveZ;

        // Перемещение игрока
        characterController.Move(move * speed * Time.deltaTime);
    }

    // Метод для применения силы тяжести
    private void HandleGravity()
    {
        if (characterController.isGrounded)
        {
            velocity.y = 0; // Если игрок находит на дне, сбрасываем y скорость
        }
        else
        {
            velocity.y += gravity * Time.deltaTime; // Применяем силу тяжести
        }

        // Перемещаем игрока вниз
        characterController.Move(velocity * Time.deltaTime);
    }
}