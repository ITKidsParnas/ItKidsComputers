public class ChopTest : TakeDamageBase
{
    public override void Damage(Inventory player)
    {
        _hp -= player.GetChopDamage();
        print("_hp " + _hp);
        print("damage " + player.GetChopDamage());

        if (_hp <= 0)
        {
            if (player.GetChopDamage() > 1)
            {
                Death();
            }
            else { Destroy(gameObject); }
        }
    }
}