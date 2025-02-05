using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class item : MonoBehaviour
{
    public CharController_Motor target;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (target != null)
        {
            var distance = Vector3.Distance(target.transform.position, transform.position);
            if (distance <50f)
            {
                target.ItemPick(gameObject);
            }
        }

        
    }
}
