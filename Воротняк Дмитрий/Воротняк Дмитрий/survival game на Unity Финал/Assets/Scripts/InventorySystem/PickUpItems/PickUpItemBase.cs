using UnityEngine;

public abstract class  PickUpItemBase :MonoBehaviour, IInteract
{
    public Sprite sprite;
    public float damage;
    public float mineDamage;
    public float chopDamage;
    public PickUpItemType type;
    public void Interact(Inventory player)
    {
        Pick(player);
    }

    public void Pick(Inventory player)
    {
        gameObject.SetActive(false);
        player.UpdateInventory(this);
    }
}
public enum PickUpItemType
{
    none,
    wood,
    woodPixaxe,
    woodSword,
    iron,
    ironSword,
    ironAxe,
    ironPixaxe,
    diamond,
    diamondSword,
    meet,
    demonAye

}
