using System;
using System.Collections;
using System.Collections.Generic;
using System.Drawing;
using UnityEngine;

public class BuildingManager : MonoBehaviour
{
    public houses[] housesPrefabs;
    public MeshFilter ghost;
    private houses CurentHouses;
    public static BuildingManager instance;
    private GameObject priviosGhost;
    public void SetHouse(int houseNum)
    {
        var newHouse = housesPrefabs[houseNum];
        ghost.gameObject.SetActive(CurentHouses != newHouse);
        if (CurentHouses == newHouse)
        {
            CurentHouses = null;
            return;
        }
        CurentHouses = newHouse;
        if (priviosGhost != null)
        {
            Destroy(priviosGhost.gameObject);
        }

        var d = CurentHouses.GetComponentInChildren<MeshFilter>();
        priviosGhost = Instantiate(CurentHouses.gameObject, Vector3.zero, Quaternion.identity);
        priviosGhost.GetComponent<houses>().enabled = false;
        priviosGhost.transform.SetParent(ghost.transform, false);
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
        if (CurentHouses == null) return;
        Vector3 mouse = Input.mousePosition;
        Ray castPoint = Camera.main.ScreenPointToRay(mouse);
        RaycastHit hit;
        if (Physics.Raycast(castPoint, out hit, Mathf.Infinity))
        {
            ghost.transform.position = hit.point;
        }
      //  ghost.transform.position = new Vector3(point.x,10.5f, point.z);
    }
}
