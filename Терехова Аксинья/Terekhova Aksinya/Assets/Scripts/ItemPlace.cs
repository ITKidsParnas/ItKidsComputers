using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ItemPlace : MonoBehaviour
{
    public ItemType Type;
    public Transform[] itemPlaces;
    private int index;
    public void SetItem(Item item)
    {
        if (index < itemPlaces.Length)
        {
            item.transform.SetParent(itemPlaces[index], false);
            index++;
        }
        else {
            item.transform.SetParent(null, false);
            item.gameObject.SetActive(false);
        }
        Destroy(item);
    }
}

