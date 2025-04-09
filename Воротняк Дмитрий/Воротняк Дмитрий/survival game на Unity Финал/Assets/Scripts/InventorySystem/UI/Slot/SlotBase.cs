using UnityEngine;
using UnityEngine.EventSystems;

public class SlotBase : MonoBehaviour,IDropHandler
{
    protected ItemUiPrefab _item;
  //  [SerializeField] protected RectTransform _center;
      public ItemUiPrefab GetItem ()
    {
        return _item;
    }
    public void OnDrop(PointerEventData eventData)
    {
        var item = eventData.pointerDrag.GetComponent<ItemUiPrefab>();
        if (item != null)
        {
            if (_item != null)
            {
                _item.DropHandler();
            }
            eventData.pointerDrag.GetComponent<RectTransform>().anchoredPosition = GetComponent<RectTransform>().anchoredPosition;
            _item = item;
            UpDataSlot();
        }

    }
    public virtual void UpDataSlot()
    { 

    }
}
