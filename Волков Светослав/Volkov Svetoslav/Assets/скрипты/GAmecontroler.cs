using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GAmecontroler : MonoBehaviour
{ 
    public float  money;
    public float cost; 
    public Text moneyText;
    public static GAmecontroler instans;
    private void Start()
    {
        instans = this;
    }
    void Update()
    {
        moneyText.text = "money:" + money;
    }
}
