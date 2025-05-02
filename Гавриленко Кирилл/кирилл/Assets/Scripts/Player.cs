
using UnityEngine;

public class Player : MonoBehaviour
{
    private Ball _ball;
    // Start is called before the first frame update
    void Start()
    {
        
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
    // Update is called once per frame
    void Update()
    {
        if (_ball != null&&Input.GetKey(KeyCode.E))
        {
            _ball.GetComponent<Rigidbody>().isKinematic = false;
            _ball.GetComponent<MeshCollider>().enabled = true;
            _ball.transform.SetParent(null);
            _ball.GetComponent<Rigidbody>().AddForce(transform.TransformDirection(Vector3.forward) * 777f);
            _ball = null;
        }
    }
}
