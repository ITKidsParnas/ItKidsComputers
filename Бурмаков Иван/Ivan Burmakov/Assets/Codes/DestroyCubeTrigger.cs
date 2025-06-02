using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyCubeTrigger : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        var player = other.GetComponent<PickItem>();
        if (player != null)
        {
            player.DestroyItem();
        }
    }
}
