using UnityEngine;
using UnityEngine.AI;
using UnityEngine.SceneManagement;
public class Bot : MonoBehaviour
{
    private NavMeshAgent agent;
    private Transform target;
    public float distoins;
      void  Start()
    {
        agent = GetComponent<NavMeshAgent>();

    }
    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.GetComponent<FirstPersonController>() != null) { SceneManager.LoadScene(SceneManager.GetActiveScene().name);}
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
            if (Vector3.Distance(target.position, transform.position) < distoins)
            {
                SceneManager.LoadScene(SceneManager.GetActiveScene().name);
            }
            else
            {
                agent.destination = target.position;
                transform.LookAt(new Vector3(agent.destination.x, transform.position.y, agent.destination.z));
            }
          
        }
    }
}
