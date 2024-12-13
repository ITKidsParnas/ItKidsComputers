using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GAmecontroler : MonoBehaviour
{ 
        public float  money;
    public Text moneyText;
    void Update()
    {
        moneyText.text = "money:" + money;
    }
}
