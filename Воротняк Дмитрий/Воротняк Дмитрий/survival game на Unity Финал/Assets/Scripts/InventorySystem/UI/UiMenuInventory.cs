using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using static UnityEngine.ParticleSystem;

public class UiMenuInventory : UIMenuBase
{
    [SerializeField] private Inventory _inventory;
    [SerializeField] private CraftSlot[] craftSlots;
    [SerializeField] private Recept[] recepts;
    public void Craft()
    {
        var items = new PickUpItemType [9];
        var i = 0;
        foreach (var slot in craftSlots)
        {
            if (slot.GetItem() != null)
            {
                items[i] = slot.GetItem().GetItem().type;
            }
            else 
            {
                items[i] = PickUpItemType.none;
            }
            i++;
        }
        foreach (var recept in recepts)
        {
            if (Enumerable.SequenceEqual(recept.recept, items))
             {
                foreach (var slot in craftSlots)
                {
                    _inventory.RemooveFromInventory(slot.GetItem());
                }
                _inventory.UpdateInventory(recept.result);
                return;
            }
        }
    }
}
[Serializable]
public class Recept
{
    public PickUpItemType[] recept = new PickUpItemType[9];
    public PickUpItemBase result;
}
