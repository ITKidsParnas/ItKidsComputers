import qrcode

data = "https://i.pinimg.com/originals/09/2c/72/092c72db80eae3f31b8420ed8e60bc73.jpg"

qr = qrcode.make(data)

qr.save("qr.png")