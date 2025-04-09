public class MineTest : TakeDamageBase
{
    public override void Damage(Inventory player)
    {
        _hp -= player.GetMineDamage();
        print("_hp " + _hp);
        print("damage " + player.GetMineDamage());

        if (_hp <= 0)
        {
            if (player.GetMineDamage() > 1)
            {
                Death();
            }
            else { Destroy(gameObject); }
        }
    }
}
