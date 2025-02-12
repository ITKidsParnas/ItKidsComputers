using UnityEngine;
using UnityEngine.AI;
using UnityEngine.SceneManagement;
[RequireComponent(typeof(NavMeshAgent))]
public class Bot : MonoBehaviour
{
    public Transform[] points;
    private NavMeshAgent agent;
    public Transform target;
    public float distnceToSee=30f;
    public float distnceToKill=3f;
   // private Transform target;
    private int currentPoint;
    private void Start()
    {
        agent = GetComponent<NavMeshAgent>();
    }
    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.GetComponent<PlayerMovement>() != null) { SceneManager.LoadScene(SceneManager.GetActiveScene().name);}
    }
    //private void OnTriggerEnter(Collider other)
    //{
    //   var player = other.gameObject.GetComponent<PlayerMovement>();
    //    if (player != null)
    //    {
    //        target = player.transform;
    //    }
    //}
    //private void OnTriggerExit(Collider other)
    //{
    //    var player = other.gameObject.GetComponent<PlayerMovement>();
    //    if (player != null)
    //    {
    //        target  = null;
    //    }
    //}
    private void Update()
    {
        if (Vector3.Distance(target.position,transform.position)<distnceToSee)
        {
            agent.destination = target.position;
            transform.LookAt(new Vector3(agent.destination.x, transform.position.y, agent.destination.z));
            if (Vector3.Distance(target.position, transform.position) < distnceToKill)
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
