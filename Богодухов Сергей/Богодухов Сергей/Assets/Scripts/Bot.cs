using UnityEngine;
using UnityEngine.AI;
using UnityEngine.SceneManagement;
public class Bot : MonoBehaviour
{
    public Transform[] points;
    private NavMeshAgent agent;
    private Transform target;
    private int currentPoint;
    private float distanceToKill = 6f;
    private void Start()
    {
        agent = GetComponent<NavMeshAgent>();

    }
    private void OnCollisionEnter(Collision collision)
    {
       if (collision.gameObject.GetComponent<FirstPersonController>() != null) 
        {
            SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        }
    }

    private void Update()
    {
        if (target != null)
        {
            agent.destination = target.position;
            transform.LookAt(new Vector3(agent.destination.x, transform.position.y, agent.destination.z));
            if (Vector3.Distance(transform.position, target.position) < distanceToKill)
            {
                SceneManager.LoadScene(SceneManager.GetActiveScene().name);
            }
        }
        else
        {
            agent.destination = points[currentPoint].position;
            transform.LookAt(new Vector3(agent.destination.x, transform.position.y, agent.destination.z));
            var distance = Vector3.Distance(agent.destination, transform.position);
            if (distance < 5.6f )
            {
                currentPoint++;
            }
        }
    }
}
