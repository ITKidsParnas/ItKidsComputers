import qrcode
data="https://avatars.mds.yandex.net/i?id=c1c54fbdcf17b81d46fe6295128c9bf0-6559900-images-thumbs&n=13"
qr=qrcode.make(data)
qr.save("qr.png")