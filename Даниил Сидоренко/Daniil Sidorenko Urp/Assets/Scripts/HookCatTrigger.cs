using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HookCatTrigger : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        if (other.GetComponent<FirstPersonController>() != null)
        {
            other.GetComponent<HookCat>().enabled = true;
        }
    }
}
