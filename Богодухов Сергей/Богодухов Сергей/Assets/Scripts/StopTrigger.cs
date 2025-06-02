using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class StopTrigger : MonoBehaviour
{
    private Bot _bot;
    private void OnTriggerEnter(Collider other)
    {
        var bot = other.GetComponent<Bot>();
        if (bot != null)
        {
            _bot = bot;
            _bot.isLoock = true;   
        }
    }
    private void OnTriggerExit(Collider other)
    {
        var bot = other.GetComponent<Bot>();
        if (bot != null)
        {
            _bot =null;
            _bot.isLoock = false;
        }
    }
    private void OnDisable()
    {
        _bot = null;
        _bot.isLoock = false;
    }
}
