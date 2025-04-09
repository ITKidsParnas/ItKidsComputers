using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Portal : MonoBehaviour
{
    [SerializeField] private int _portalCount=12;
    [SerializeField] private Collider _collider;
    public void ActivatePortal()
    {
        --_portalCount;
        if (_portalCount <= 0)
        {
            _collider.gameObject.SetActive(true);
        }
    }
}
