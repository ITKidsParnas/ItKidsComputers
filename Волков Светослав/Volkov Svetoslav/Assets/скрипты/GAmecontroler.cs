using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class GAmecontroler : MonoBehaviour
{ 
    public float  money;
    
    public float cost; 
    public Text moneyText;
    public static GAmecontroler instans;
    public Scrollbar HateScrollbar;

    public float Hate;

    private void Start()
    {
        instans = this;
    }
    void Update()
    {
        moneyText.text = "money:" + money;
        if (Hate >= 100)
        {
            SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        }

    }
}
