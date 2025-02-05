using UnityEngine;
using UnityEngine.AI;
using UnityEngine.SceneManagement;
public class Bot : MonoBehaviour
{
    public Transform[] points;
    private NavMeshAgent agent;
    private Transform target;
    private int currentPoint;
    private void Start()
    {
        agent = GetComponent<NavMeshAgent>();
    }
    private void OnCollisionEnter(Collision collision)
    {
      //  if (collision.gameObject.GetComponent<Target>() != null) { SceneManager.LoadScene(SceneManager.GetActiveScene().name);}
    }
    private void OnTriggerEnter(Collider other)
    {
        var player = other.gameObject.GetComponent<FirstPersonController>();
        if (player != null)
        {
            target = player.transform;
        }
    }
    private void OnTriggerExit(Collider other)
    {
        var player = other.gameObject.GetComponent<FirstPersonController>();
        if (player != null)
        {
            target  = null;
        }
    }
    private void Update()
    {
        if (target != null)
        {
            agent.destination = target.position;
            transform.LookAt(new Vector3(agent.destination.x, transform.position.y, agent.destination.z));
            var distance = Vector3.Distance(agent.destination, transform.position);
            if (distance < 0.6f)
            {
                SceneManager.LoadScene(SceneManager.GetActiveScene().name);
            }
        }
        else
        {
            agent.destination = points[currentPoint].position;
            transform.LookAt(new Vector3(agent.destination.x, transform.position.y, agent.destination.z));
            var distance = Vector3.Distance(agent.destination, transform.position);
            if (distance < 0.6f )
            {
                currentPoint++;
                if (currentPoint >= points.Length)
                {
                    currentPoint = 0;
                }
            }
        }
    }
}
