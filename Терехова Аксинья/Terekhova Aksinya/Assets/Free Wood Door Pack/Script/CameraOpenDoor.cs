using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace CameraDoorScript
{
	public class CameraOpenDoor : MonoBehaviour
	{
		public float DistanceOpen = 3;
		public GameObject text;
		private inventory _inventory;
		// Use this for initialization
		void Start()
		{
			_inventory = GetComponent<inventory>();

		}

		// Update is called once per frame
		void Update()
		{
			RaycastHit hit;
			if (Physics.Raycast(transform.position, transform.forward, out hit, DistanceOpen))
			{
				Debug.DrawRay(transform.position, transform.forward* DistanceOpen);
				if (hit.transform.GetComponent<DoorScript.Door>())
				{
					text.SetActive(true);
					if (Input.GetKeyDown(KeyCode.E))
					{
						hit.transform.GetComponent<DoorScript.Door>().OpenDoor();
					}
				}
				else if (hit.transform.GetComponent<Item>())
				{
					text.SetActive(true);
					if (Input.GetKeyDown(KeyCode.E))
					{
						_inventory.PickItem(hit.transform.GetComponent<Item>());
					}
				}
				else if (hit.transform.GetComponent<ItemPlace>())
				{
					text.SetActive(true);
					if (Input.GetKeyDown(KeyCode.E))
					{
						_inventory.PutItem(hit.transform.GetComponent<ItemPlace>());
					}
                }  else { text.SetActive(false); }
            }
			else{text.SetActive(false);
                Debug.DrawRay(transform.position, transform.forward);
            }
		}
	}
}