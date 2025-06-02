using System.Collections;
using System.Collections.Generic;
using UnityEngine;



namespace DesignPatterns
{
    public class stear : MonoBehaviour
    {
        public Transform spawnPoint;
        public float speed;

        private bool isMooving;
        private Transform _playerTransform;
       
        private void OnTriggerEnter(Collider other)
        {
            var player = other.GetComponent<FirstPersonController>();
            if (player != null) { isMooving = false;
                player.enabled = true;
                player.transform.position = spawnPoint.position;
                player.GetComponent<Rigidbody>().isKinematic = false;

            }
        }
        private void OnCollisionEnter(Collision collision)
        {
            var player = collision.gameObject.GetComponent <FirstPersonController>();
            if (player != null) {
                isMooving = true;
                _playerTransform = player.transform;
                player.enabled = false;
                player.GetComponent<Rigidbody>().isKinematic = true;
            }

        }
       


        void Update()
        {
            if (isMooving) 
            {
                var destination = _playerTransform.position + new Vector3(0,Input.GetAxis("Vertical"),0);
                _playerTransform.position = Vector3.MoveTowards(_playerTransform.position, destination, Time.deltaTime*speed);
            }
        }
    }
}
