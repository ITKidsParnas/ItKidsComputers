using UnityEngine;

public class InventorySlot : SlotBase
{
    [SerializeField] private Inventory _inventory;
    public override void UpDataSlot()
    {
        _inventory.pickUpItemCurrent = _item.GetItem();
    }
}
