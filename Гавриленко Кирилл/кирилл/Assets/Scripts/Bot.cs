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
    public float StrikeDistance;
    public Ball _ball;
    private void Start()
    {
        agent = GetComponent<NavMeshAgent>();
    }
    private void OnCollisionEnter(Collision collision)
    {
        var ball = collision.gameObject.GetComponent<Ball>();
        if (ball != null)
        {
            ball.bot =this;
            ball.GetComponent<Rigidbody>().isKinematic = true;
            ball.GetComponent<MeshCollider>().enabled = false;
            ball.transform.SetParent(transform);
            ball.transform.rotation = new Quaternion(0, 0, 0, 0);
            _ball = ball;
        }
        if (collision.gameObject.GetComponent<Player>())
        {
            if (collision.gameObject.GetComponent<Player>()._ball!=null)
            {
                _ball = collision.gameObject.GetComponent<Player>()._ball;
                _ball.bot = this;
                _ball.GetComponent<Rigidbody>().isKinematic = true;
                _ball.GetComponent<MeshCollider>().enabled = false;
                _ball.transform.SetParent(transform);
                _ball.transform.rotation = new Quaternion(0, 0, 0, 0);
                collision.gameObject.GetComponent<Player>()._ball=null;
            }
        }
    }
    public void StillBall()
    {
        agent.destination = transform.position;
        _ball = null;
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
            agent.speed = 10f;
            agent.destination = gates.position;
            if (Vector3.Distance(transform.position, gates.position) < StrikeDistance)
            {
                agent.destination = transform.position;
                _ball.GetComponent<Rigidbody>().isKinematic = false;
                _ball.GetComponent<MeshCollider>().enabled = true;
                _ball.transform.SetParent(null);
                _ball.GetComponent<Rigidbody>().AddForce(transform.TransformDirection(Vector3.forward) * 1000f);
                //_ball = null;
            }
            else { agent.destination = gates.position; }
        }

    }
}
