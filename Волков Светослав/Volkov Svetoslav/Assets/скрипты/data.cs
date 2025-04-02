using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class NumberChanger : MonoBehaviour
{
    public Text numberText; // —сылка на UI Text
    private int currentNumber = 0;
    private DateTime curentDate= new DateTime(2017,2,1);
    private float timer = 0f;
    private void Awake()
    {
        UpdateText();
    }
    // Update is called once per frame
    void Update()
    {
        timer += Time.deltaTime;

        if (timer >= 30f)
        {
            curentDate= curentDate.AddDays(1);
            UpdateText();
            timer = 0f;
        }
    }
    void UpdateText()
    {
        numberText.text = curentDate.ToString("d"); // ќбновл€ем текст
    }
}






