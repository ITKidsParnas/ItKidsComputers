using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bomb : MonoBehaviour
{
    public GameObject _destroyTrigger;
    private void OnCollisionEnter(Collision collision)
    {
        Instantiate(_destroyTrigger, collision.contacts[0].point, Quaternion.identity);
        Destroy(gameObject);
    }
}
