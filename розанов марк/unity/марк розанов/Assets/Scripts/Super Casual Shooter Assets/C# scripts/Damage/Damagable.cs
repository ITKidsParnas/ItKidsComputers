/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;



[RequireComponent(typeof(BoxCollider))]


 // this script can be attached to the player or anything that can take damage
public class Damagable : MonoBehaviour
{
    [SerializeField] 
    private int max_health; // the maximum health

    private float current_health; // the current health of the damagable


    [SerializeField]
    private UnityEvent OnDeath; // what happens when health finishes


    [SerializeField]
    [Range(0, 5)]
    private float still_show_damage_effect_for = 0; // even when damage is no longer received. how long should we wait before the damage effect stops. 
                                                // an example of this is how long should the player bleed, even after it has stopped taking damage.

    private float show_damage_effect_counter; // this would help us know when to stop showing damage

    // Use this for initialization
    void Start ()
    {
        current_health = max_health;	
	}


	// Update is called once per frame
	void Update ()
    {
        if (current_health < 1)
        {
            OnDeath.Invoke();
        }

        handleDamageEffect();
    }

    private void handleDamageEffect()
    {
        if(show_damage_effect_counter > 0)
        {
            show_damage_effect_counter -= Time.deltaTime;
        }

    }

    public void takeDamage(float damage) // take a damage
    {
        current_health -= damage;

       
        show_damage_effect_counter = still_show_damage_effect_for;
    }


    public void reverseDamage(int health) // when we get some health
    {
        current_health += health;

        current_health = Mathf.Clamp(current_health, 0, max_health);
    }

   

    public void destroyMesh() // you can use this function to destroy gameobject when health finishes, currently no object uses it
    {
        Destroy(gameObject);
    }

    

    public int getMaxHealth() 
    { 
        return max_health; 
    }

    public float getCurrentHealth()
    {
        return current_health;
    }


    public float getCurrentDamageEffectCounter()
    {
        return show_damage_effect_counter;
    }

    public float getMaxDamageEffectCounter()
    {
        return still_show_damage_effect_for;
    }


}
