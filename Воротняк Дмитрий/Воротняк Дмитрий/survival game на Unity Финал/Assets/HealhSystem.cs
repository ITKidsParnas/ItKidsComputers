using UnityEngine;
using UnityEngine.UI;

public class HealhSystem : MonoBehaviour
{
    [SerializeField] private GameObject _canavas;
    [SerializeField] private Slider _healthBar;
    [SerializeField] private float _health;
    private void Awake()
    {
        _healthBar.maxValue = _health;
    }
    public float Health
    {
        get
        {
            return _health;
        }
        set
        {
            _health -= value;
            _healthBar.value = _health;
            if (_health < 0)
            {
                _canavas.SetActive(true);
            }
        }
    }
}
