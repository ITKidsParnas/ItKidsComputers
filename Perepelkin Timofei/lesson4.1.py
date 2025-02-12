import qrcode

data = "https://print.com/"
qr = qrcode.make(data)
qr.save("qr.png")