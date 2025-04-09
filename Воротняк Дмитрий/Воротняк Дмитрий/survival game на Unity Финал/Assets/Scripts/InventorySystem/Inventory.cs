using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Inventory : MonoBehaviour
{
    public PickUpItemBase pickUpItemCurrent;
    public List <PickUpItemBase>items;

    [SerializeField] private Canvas _inventory;
    [SerializeField] private float _handDamage;
    [SerializeField] private float _hitDistance;
    [SerializeField] private Camera _HitPoint;
    [SerializeField] private ItemUiPrefab _itemPrefab;
    [SerializeField] private GridLayoutGroup inventoryGridLayoutGroup;

    private float _damage;
    private float _mineDamage;
    private float _chopDamage;
    private float _mineHandDamage = 1;
    private float _chopHandDamage = 1;
    public float GetDamage() { return _damage; }
    public float GetMineDamage() { return _mineDamage; }
    public float GetChopDamage() { return _chopDamage; }

    void Update()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            if (pickUpItemCurrent != null)
            {
                _chopDamage = pickUpItemCurrent.chopDamage;
                _mineDamage = pickUpItemCurrent.mineDamage;
                _damage = pickUpItemCurrent.damage;
            }
            else
            {
                _chopDamage = _chopHandDamage;
                _mineDamage = _mineHandDamage;
                _damage = _handDamage;
            }
            RaycastHit hit = new RaycastHit();
            Ray ray = _HitPoint.ScreenPointToRay(Input.mousePosition);
            hit.distance = _hitDistance;
            if (Physics.Raycast(ray, out hit))
            {
                Debug.DrawRay(_HitPoint.transform.position, hit.transform.position, Color.yellow);
                var interact = hit.collider.GetComponent<IInteract>();
                if (interact != null)
                {
                    Debug.Log("Did Hit Interact");
                    interact.Interact(this);
                }
                Debug.Log("Did Hit");
            }   
        }
        if (Input.GetKeyDown(KeyCode.I))
        {
            _inventory.gameObject.SetActive(!_inventory.gameObject.activeInHierarchy);
        }
    }
    public void UpdateInventory(PickUpItemBase pickUpItemBase)
    {
        items.Add(pickUpItemBase);
        var item = Instantiate(_itemPrefab, inventoryGridLayoutGroup.transform);
        item.SetData(pickUpItemBase, _inventory, inventoryGridLayoutGroup);
    }
    public void RemooveFromInventory( ItemUiPrefab uiPrefab)
    {
        if (uiPrefab == null)
        {
            return;
        }
        items.Remove(uiPrefab.GetItem());
        Destroy(uiPrefab.gameObject);
    }
}
