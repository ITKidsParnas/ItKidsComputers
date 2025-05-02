using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gun : MonoBehaviour
{
    public bool isbot;
    public gun enemy;
    public bool isdeath;
    public GameObject effect;
    public AudioSource audioSource;
    public Rigidbody[] rigidbodies;
    private bool isShoted;
    // Start is called before the first frame update
    void Start()
    {

        if (isbot)
        {
            Invoke("Shoot",Random.Range(0.5f,3f));    
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (isbot) { return; }
       if(Input.GetKeyDown(KeyCode.Space))
        {
            Shoot();
        }
    }

    private void Shoot()
    {
        if(isdeath) { return; }
        if(isShoted) { return; }
        isShoted = true;
        enemy.isdeath = true;
        effect.SetActive(true);
        if (!isbot)
        {
           PlayerPrefs.SetInt("money", PlayerPrefs.GetInt("money", 0) + 10);               
        }
        audioSource.Play();
        foreach (var rigidbody in rigidbodies)
        {
            rigidbody.isKinematic = false;
        }
    }
}
