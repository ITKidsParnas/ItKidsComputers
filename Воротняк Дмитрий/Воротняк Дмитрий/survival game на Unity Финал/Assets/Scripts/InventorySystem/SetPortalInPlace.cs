using UnityEngine;

[RequireComponent(typeof(MeshRenderer))]
public class SetPortalInPlace : MonoBehaviour, IInteract
{
    [SerializeField] private Portal _portal;
    [SerializeField] private PickUpItemType _type;
    [SerializeField] private Material _material;
    private bool isInteracted;
    private MeshRenderer renderer;
    private void Awake()
    {
        renderer = GetComponent<MeshRenderer>();
    }
    public void Interact(Inventory player)
    {
        if (isInteracted)
        {
         return; 
        }
        if (player.pickUpItemCurrent.type == _type)
        {
            renderer.materials[1].color = _material.color;
            _portal.ActivatePortal();
        }
    }
}
