using System.Collections;
using System.Collections.Generic;
using UnityEngine;

    public class Item : MonoBehaviour
    {
    public ItemType type;
        void Start()
        {
            
        }


        void Update()
        {
            
        }
    }
public enum ItemType
{
    Cloth,
    Toys,
    Dishes,
    Wash,
    BathItem
}