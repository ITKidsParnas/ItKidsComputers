using UnityEngine;

public class TakeDamageBase : MonoBehaviour, IInteract
{
    [SerializeField] protected float _hp;
    [SerializeField] protected PickUpItemBase loot;
    public void Interact(Inventory player)
    {
        Damage(player);
    }
    public virtual void Damage(Inventory player)
    {
        _hp -= player.GetDamage();
        print("_hp " + _hp);
        print("damage " + player.GetDamage());

        if (_hp <= 0)
        {
            Death();
        }
    }
    public virtual void Death()
    {
        var lootItem = Instantiate(loot, transform.position, Quaternion.identity);
        lootItem.gameObject.SetActive(true);
        Destroy(gameObject);
    }
}
