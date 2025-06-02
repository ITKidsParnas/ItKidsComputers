using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class inventory  : MonoBehaviour
{
    public Text text;
    public Transform ItemTransform;
    private Item _item;
    public void PickItem(Item item) 
    {
        text.text = GetItemMessage(item.type);
        _item = item;
        item.transform.SetParent(ItemTransform, false);
        item.transform.localPosition = Vector3.zero;
        item.GetComponent<Collider>().enabled = false;
    }
    private string GetItemMessage(ItemType type) 
    {
        if (type == ItemType.Cloth) return "положи одежду в шкаф";
        if (type == ItemType.Wash) return "положи предмет в стиральную машину";
        if (type == ItemType.Toys) return "положи игрушки на стол ";
        if (type == ItemType.Dishes) return "положи тарелку на обеденый стол ";
        return "";
    }    
    public void PutItem(ItemPlace itemPlace) 
    {
        if (_item == null) return;
        if (_item.type == itemPlace.Type)
        { 
            text.text = "";
            itemPlace.SetItem(_item);
            _item = null;
        }
    }
        }

