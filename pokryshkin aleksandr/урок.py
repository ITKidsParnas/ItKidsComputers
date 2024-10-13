import qrcode

data = "https://www.mellstroi.com/"
qr = qrcode.make(data)
qr.save("qr.png")