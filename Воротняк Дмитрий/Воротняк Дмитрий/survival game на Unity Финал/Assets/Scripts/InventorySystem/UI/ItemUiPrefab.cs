using System.Security.Cryptography.X509Certificates;
using UnityEditorInternal.Profiling.Memory.Experimental;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;

public class ItemUiPrefab : MonoBehaviour ,IEndDragHandler
{
    [SerializeField] private Image image;
    private Canvas _canvas;
    private RectTransform _parent;
    private PickUpItemBase _item;

    public PickUpItemBase GetItem()
    { 
        return _item;
    }
    public void SetData(PickUpItemBase item, Canvas canvas,GridLayoutGroup grid)
    {
        image.sprite = item.sprite;
        _canvas = canvas;
        _parent = grid.GetComponent<RectTransform>();
        _item = item;
    }

    public void DragHandler(BaseEventData data)
    {
        transform.parent = _canvas.transform;
        PointerEventData pointerData = (PointerEventData)data;
        Vector2 position;
        RectTransformUtility.ScreenPointToLocalPointInRectangle((RectTransform)_canvas.transform, pointerData.position, _canvas.worldCamera, out position);
        transform.position = _canvas.transform.TransformPoint(position);
        image.raycastTarget = false;
    }

    public void DropHandler()
    {
        transform.parent = _parent;
    }

    public void OnEndDrag(PointerEventData eventData)
    {
        image.raycastTarget = true;
    }
}