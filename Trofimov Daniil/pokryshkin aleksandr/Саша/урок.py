import qrcode

data = "https://www..com/"
qr = qrcode.make(data)
qr.save("qr.png")