using UnityEngine;

public class MouseLook : MonoBehaviour
{
    public float sensitivity = 2f; // Чувствительность мыши
    public float rotationX = 0f; // Угол вращения по оси X
    public float rotationY = 0f; // Угол вращения по оси Y
    public float minX = -60f; // Минимальный угол по оси X
    public float maxX = 60f; // Максимальный угол по оси X

    private void Start()
    {
        Cursor.lockState = CursorLockMode.Locked; // Скрываем курсор и блокируем его в центре экрана
    }

    private void Update()
    {
        RotateCamera(); // Вращение камеры
    }

    // Метод для обработки вращения камеры
    private void RotateCamera()
    {
        float mouseX = Input.GetAxis("Mouse X") * sensitivity; // Получаем данные о движении мыши по оси X (горизонталь)
        float mouseY = Input.GetAxis("Mouse Y") * sensitivity; // Получаем данные о движении мыши по оси Y (вертикаль)

        // Обновляем углы вращения
        rotationY += mouseX;
        rotationX -= mouseY;

        // Ограничиваем угол вращения по оси X
        rotationX = Mathf.Clamp(rotationX, minX, maxX);

        // Применяем вращение к камере
        transform.localRotation = Quaternion.Euler(rotationX, rotationY, 0f);
    }
}