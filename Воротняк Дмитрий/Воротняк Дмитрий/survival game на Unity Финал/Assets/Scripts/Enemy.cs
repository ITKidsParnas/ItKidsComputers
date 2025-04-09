using System.Collections;
using UnityEngine;
using UnityEngine.AI;

public class Enemy : MonoBehaviour
{
    private FirstPersonController _player;
    public Transform[] points;
    private int destPoint = 0;
    private NavMeshAgent _agent;
    [SerializeField] private float _damage;
    void Start()
    {
        _agent = GetComponent<NavMeshAgent>();
        _agent.autoBraking = false;
        GotoNextPoint();
    }


   private void GotoNextPoint()
    {
        if (points.Length == 0)
            return;
        _agent.destination = points[destPoint].position;
        destPoint = (destPoint + 1) % points.Length;
    }


    void Update()
    {
        if (_player != null)
        {
            _agent.destination = _player.transform.position;
        }
        else
        {
            if (!_agent.pathPending && _agent.remainingDistance < 0.5f)
                GotoNextPoint();
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.GetComponent<FirstPersonController>() != null)
        {
            _player = other.GetComponent<FirstPersonController>();
        }
    }
   
    private void OnTriggerExit(Collider other)
    {
        if (other.GetComponent<FirstPersonController>() != null)
        {
            _player = null;
        }
    }
    private void OnCollisionEnter(Collision collision)
    {
        var player = collision.gameObject.GetComponent<HealhSystem>();
        if (player != null)
        {
            StartCoroutine(Damage(player));
        }
    }

    private void OnCollisionExit(Collision collision)
    {
        var player = collision.gameObject.GetComponent<HealhSystem>();
        if (player != null)
        {
            StopAllCoroutines();
        }
    }
    IEnumerator Damage(HealhSystem player)
    {
        yield return new WaitForSeconds(1f);
        player.Health = _damage;
    }
}
