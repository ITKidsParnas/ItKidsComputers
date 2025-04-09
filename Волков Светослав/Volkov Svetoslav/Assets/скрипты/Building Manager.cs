using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using static UnityEngine.UIElements.UxmlAttributeDescription;

public class BuildingManager : MonoBehaviour
{
    public houses[] housesPrefabs;
    private houses CurentHouses;
    public static BuildingManager instance;
    public void SetHouse(int houseNum)
    {
        CurentHouses = housesPrefabs[houseNum];
    }
    public void BuildHouse(GameObject housePlase)
    { 
        if (CurentHouses == null) return;
        if (GAmecontroler.instans.money >= CurentHouses.cost)
        {
            GAmecontroler.instans.money -= CurentHouses.cost;
            var obj = Instantiate(CurentHouses.gameObject, housePlase.transform.position, Quaternion.identity);
            obj.transform.rotation = housePlase.transform.rotation;
            Destroy(housePlase);
        }
    }    
    void Start()
    {
        instance = this;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
