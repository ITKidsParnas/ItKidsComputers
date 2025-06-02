using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.UIElements;


public class gun : MonoBehaviour
{
    public bool isbot;
    public GameObject winPanel;
    public GameObject pauseMenu;
    public GameObject loosePanel;
    public gun enemy;
    public Text text;
    public bool isdeath;
    public GameObject effect;
    public AudioSource audioSource;
    public Rigidbody[] rigidbodies;
    public Animator animator;
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
        pauseMenu.SetActive(false);
        if (isdeath) { return; }
        if(isShoted) { return; }
        isShoted = true;
        enemy.isdeath = true;
        effect.SetActive(true);
        animator.SetTrigger("shoot");
        winPanel.SetActive(!isbot);
        loosePanel.SetActive(isbot);
        text.text = isbot ? "You loose" : "You win";
        if (!isbot)
        {
           PlayerPrefs.SetInt("money", PlayerPrefs.GetInt("money", 0) + 10);               
        }
        audioSource.Play();
        rigidbodies[0].GetComponentInParent<Animator>().enabled = false;   
        foreach (var rigidbody in rigidbodies)
        {
            rigidbody.isKinematic = false;
        }
    }
}
