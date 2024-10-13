import qrcode

data = "https://gtaprosveshcheniye.ucoz.net/"
qr = qrcode.make(data)
qr.save("qr.png")