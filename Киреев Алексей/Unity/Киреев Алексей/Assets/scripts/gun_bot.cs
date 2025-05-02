using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gun_bot : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject effect;
    public AudioSource audioSource;
    void Start()
    {
        Invoke("Shoot", Random.Range(0.1f,5f));
    }
    private void Shoot()
    {
        effect.SetActive(true);
        audioSource.Play();
    }
}
