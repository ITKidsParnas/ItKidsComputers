using UnityEngine;

public class ZRotationLimiter : MonoBehaviour
{
    [SerializeField] private float minZAngle = -45f;
    [SerializeField] private float maxZAngle = 45f;

    void Update()
    {
        // Получаем текущие углы Эйлера
        Vector3 currentRotation = transform.eulerAngles;

        // Приводим угол Z к диапазону -180..180
        if (currentRotation.z > 180f)
            currentRotation.z -= 360f;

        // Ограничиваем угол Z
        currentRotation.z = Mathf.Clamp(currentRotation.z, minZAngle, maxZAngle);

        // Применяем обратно
        transform.eulerAngles = currentRotation;
    }
}