using Unity.VisualScripting;
using UnityEngine;

public class PickItem : MonoBehaviour
{
    [Header("Настройки")]
    public Transform holdPoint; // Точка удержания объекта
    public float pickUpDistance = 3f; // Дистанция поднятия объекта
    public float liftSpeed = 5f; // Скорость поднятия/опускания
    public float throwForce = 10f; // Сила броска

    private Rigidbody heldRb;
    private bool isHolding = false;
    private float originalZPosition; // Сохраняем оригинальную Z-позицию

    public void DestroyItem()
    {
        if (heldRb == null) return;
        {
            var objToDestroy = heldRb.gameObject;
            ReleaseObject();
            Destroy(objToDestroy);
        }
    }

    void Update()
    {
        HandlePickUp();
        if (isHolding)
        {
            if (Input.GetKey(KeyCode.Mouse2))
            {
                heldRb.transform.SetParent(null, true);   
                HandleMovement();
            }
            else
            {
                heldRb.transform.SetParent(holdPoint, true);
            }
        }


    }

    private void HandlePickUp()
    {
        if (Input.GetKeyDown(KeyCode.E))
        {
            if (isHolding)
            {
                ReleaseObject();
                return;
            }

            RaycastHit hit;
            if (Physics.Raycast(Camera.main.transform.position, Camera.main.transform.forward, out hit, pickUpDistance))
            {
                if (hit.collider.GetComponent<cube>()!=null) // Добавьте тег "Pickable" к поднимаемым объектам
                {
                    heldRb = hit.collider.GetComponent<Rigidbody>();
                    if (heldRb != null)
                    {
                        originalZPosition = heldRb.position.z; // Сохраняем оригинальную Z-позицию
                        isHolding = true;
                        heldRb.isKinematic = true;
                        heldRb.useGravity = false;

                    }
                }
            }
        }
    }

    private void HandleMovement()
    {
        if (!isHolding || heldRb == null) return;

        // Плавное перемещение к точке удержания
        Vector3 targetPosition = holdPoint.position;

        // Сохраняем оригинальную Z-координату или модифицируем по вашему желанию
        // Вариант 1: Сохраняем оригинальную Z-позицию
        targetPosition.z = originalZPosition;

        // Вариант 2: Поднимаем по Z (если нужно изменить Z-координату)
        // targetPosition.z += liftHeight; // Раскомментируйте если нужно

        heldRb.MovePosition(Vector3.Lerp(
            heldRb.position,
            targetPosition,
            liftSpeed * Time.deltaTime
        ));

        // Вращение объекта (опционально)
        heldRb.MoveRotation(Quaternion.Lerp(
            heldRb.rotation,
            holdPoint.rotation,
            liftSpeed * Time.deltaTime
        ));
    }

    private void ReleaseObject()
    { 
        heldRb.transform.SetParent(null, true);
        if (heldRb != null)
        {
            heldRb.isKinematic = false;
            heldRb.useGravity = true;
            heldRb = null;
        }
        isHolding = false;

    }

    private void ThrowObject()
    {
        if (heldRb == null) return;

        ReleaseObject();
        heldRb.AddForce(Camera.main.transform.forward * throwForce, ForceMode.Impulse);
    }

    // Визуализация луча в редакторе
    private void OnDrawGizmos()
    {
        if (Camera.main != null)
        {
            Gizmos.color = Color.green;
            Gizmos.DrawRay(Camera.main.transform.position, Camera.main.transform.forward * pickUpDistance);
        }
    }
}