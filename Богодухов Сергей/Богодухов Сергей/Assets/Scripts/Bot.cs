using UnityEngine;
using UnityEngine.AI;
using UnityEngine.SceneManagement;
public class Bot : MonoBehaviour
{
    public Transform[] points;
    public Transform player;
    public Camera Ncamera;
    private NavMeshAgent agent;
    private Transform target;
    public int currentPoint;
    public bool isLoock;
    private float distanceToKill = 6f;
    private void Start()
    {
        agent = GetComponent<NavMeshAgent>();

    }
    private void Update()
    {
        if (isLoock) { agent.destination = transform.position; }
        agent.destination = points[currentPoint].position;
        transform.LookAt(new Vector3(agent.destination.x, transform.position.y, agent.destination.z));
        var distance = Vector3.Distance(agent.destination, transform.position);
        if (distance < 2f)
        {
            currentPoint++;
            if (currentPoint > 5)
            {
                transform.position = points[currentPoint].position;
            }
        }

        if (Vector3.Distance(transform.position, player.position) < distanceToKill)
        {
            SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        }
        if (currentPoint >= points.Length)
        {
            currentPoint= 0;
        }
    }

}
