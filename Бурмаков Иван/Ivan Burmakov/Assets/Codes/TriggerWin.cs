using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TriggerWin : MonoBehaviour
{

        private void OnTriggerEnter(Collider other)
        {
            var player = other.GetComponent<GameOverSystem>();
            if (player != null)
            {
                player.Win();
            }
        }
    }
