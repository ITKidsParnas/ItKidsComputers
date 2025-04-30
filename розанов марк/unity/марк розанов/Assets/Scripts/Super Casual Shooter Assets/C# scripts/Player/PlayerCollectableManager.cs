/*
    Written By Olusola Olaoye

    To only be used by those who purchased from the Unity asset store

*/


using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerCollectableManager : MonoBehaviour
{

    #region Singleton
    private static PlayerCollectableManager instance;
    public static PlayerCollectableManager Instance
    {
        get
        {
            return instance;
        }
    }

    #endregion


   
    private List<Collectable> current_weapons = new List<Collectable>();

    public int weapon_at_hand_index
    {
        get;
        set;
    }
  
    public Transform hand;

    private PlayerInput player_input;

   
	// Use this for initialization
	void Start ()
    {
        
        if(instance == null)
        {
            instance = this;
        }
        player_input = gameObject.GetComponent<PlayerInput>();

    }

    // Update is called once per frame
    void Update()
    {
        if (player_input.disinteract)
        {
            dropCollectable(current_weapons[weapon_at_hand_index]);

        }

        updateWeaponIndex();

        updateWeaponAtHand();

        // aim texture should only be visible if the weapon currently held is a type of Gun
        AimTexture.Instance.setActive(current_weapons.Count > 0 && current_weapons[weapon_at_hand_index].GetType().BaseType == typeof(Gun));

    }


    private void updateWeaponIndex() // use the mouse scroll wheel to change currect weapon
    {
        if (Input.GetAxis("Mouse ScrollWheel") > 0)
        {
            weapon_at_hand_index += 1;
        }
        else if (Input.GetAxis("Mouse ScrollWheel") < 0)
        {
            weapon_at_hand_index -= 1;
        }
        weapon_at_hand_index = Mathf.Clamp(weapon_at_hand_index, 0, current_weapons.Count - 1);

    }


    public void removeWeaponFromList(Collectable weapon)
    {
        current_weapons.Remove(weapon);
    }

    private void updateWeaponAtHand() // set only the current weapon visible
    {
        for (int i = 0; i < current_weapons.Count; i++)
        {
            if (weapon_at_hand_index == i)
            {
                current_weapons[i].gameObject.SetActive(true);
            }
            else
            {
                current_weapons[i].gameObject.SetActive(false);
            }
        }
    }

    public void assignCollectableToHand(Collectable collectable) // pick up a collectable and set it to hand position
    {
        collectable.pickUpThisObject();

        Vector3 off_Set = collectable.offset;
        off_Set = hand.rotation * off_Set;
        collectable.GetComponent<Rigidbody>().isKinematic = true;
        collectable.transform.SetParent(hand.transform);
        collectable.transform.position = (hand.transform.position + off_Set);
        
        collectable.transform.rotation = hand.rotation;

        current_weapons.Add(collectable);
    }


    public void dropCollectable(Collectable collectable) //drop a collectable
    {

        collectable.dropThisObject();

        collectable.transform.SetParent(null);

        collectable.GetComponent<Rigidbody>().isKinematic = false;
        collectable.GetComponent<Rigidbody>().AddForce(transform.forward * 200); // to give the effect that player threw the weapon foward


        StartCoroutine(changeCollectable()); // a little bit of delay before we switch to the next available collectable in our inventory

        IEnumerator changeCollectable()
        {
            yield return new WaitForSeconds(1);

            current_weapons.Remove(collectable);

            if (weapon_at_hand_index > 0)
            {
                weapon_at_hand_index -= 1;
            }
        }
    }

    
}
