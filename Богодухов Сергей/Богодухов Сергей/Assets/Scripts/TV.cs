using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TV : MonoBehaviour
{
    public GameObject[] cameras;
    public Bot[] bots;
    private int index;
    private GameObject last;
    // Update is called once per frame
    private void Start()
    {
        last = cameras[0];
        foreach (Bot bot in bots)
        {
            bot.Ncamera = last.GetComponent<Camera>();
        }
    }
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.RightArrow))
        {
            if (index >= cameras.Length - 1)
            {
                index = 0;
            }
            else 
            {
                index++;
            }
            last.SetActive(false);
            cameras[index].SetActive(true);
            last = cameras[index];
        }
        if (Input.GetKeyDown(KeyCode.LeftArrow))
        {
            if (index <=0)
            {
                index = cameras.Length - 1;
            }
            else
            {
                index--;
            }
            last.SetActive(false);
            cameras[index].SetActive(true);
            last = cameras[index];
        }
        foreach (Bot bot in bots) 
        {
            bot.Ncamera = last.GetComponent < Camera>();
        }
    }
}
