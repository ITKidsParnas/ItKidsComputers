using System.Collections;
using System.Collections.Generic;
using Unity.Services.Analytics.Internal;
using UnityEngine;
using UnityEngine.AI;

public class Bot : MonoBehaviour
{
    private NavMeshAgent agent;
    public Transform destination;
    public Transform gates;
    private Ball _ball;
    private void Start()
    {
        agent = GetComponent<NavMeshAgent>();
    }
    private void OnCollisionEnter(Collision collision)
    {
        var ball = collision.gameObject.GetComponent<Ball>();
        if (ball != null)
        {
            ball.GetComponent<Rigidbody>().isKinematic = true;
            ball.GetComponent<MeshCollider>().enabled = false;
            ball.transform.SetParent(transform);
            ball.transform.rotation = new Quaternion(0, 0, 0, 0);
            _ball = ball;
        }
    }
    private void Update()
    {
        if (_ball == null)
        {
            agent.speed = 3.5f;
            agent.destination = destination.position;
        }
        else
        {
            agent.speed = 1000f;
            agent.destination = gates.position;
        }

    }
}
