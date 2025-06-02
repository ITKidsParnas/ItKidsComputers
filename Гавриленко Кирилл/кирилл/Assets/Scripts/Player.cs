
using UnityEngine;

public class Player : MonoBehaviour
{
    public Ball _ball;
    public Transform _point;
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
            _ball.GetComponent<Rigidbody>().AddForce(transform.TransformDirection(Vector3.forward) * 1000f);
            _ball = null;
        }
        if(_ball == null && Input.GetKey(KeyCode.F))
        {
            RaycastHit hit;
            // Does the ray intersect any objects excluding the player layer
            if (Physics.Raycast(Camera.main.transform.position, Camera.main.transform.TransformDirection(Vector3.forward), out hit, 10))
            {
                var bot = hit.transform.gameObject.GetComponent<Bot>();
                if (bot != null)
                {
                    if (bot._ball != null)
                    {
                        bot._ball.GetComponent<Rigidbody>().isKinematic = true;
                        bot._ball.GetComponent<MeshCollider>().enabled = false;
                        bot._ball.transform.SetParent(transform);
                        bot._ball.transform.rotation = new Quaternion(0, 0, 0, 0);
                        _ball = bot._ball;
                        _ball.transform.position = _point.position;
                        if (_ball.bot != null) _ball.bot.StillBall();
                    }
                }

            }
            else
            {
                Debug.DrawRay(transform.position, transform.TransformDirection(Vector3.forward) * 1000, Color.white);
                Debug.Log("Did not Hit");
            }
        }
    }
}
