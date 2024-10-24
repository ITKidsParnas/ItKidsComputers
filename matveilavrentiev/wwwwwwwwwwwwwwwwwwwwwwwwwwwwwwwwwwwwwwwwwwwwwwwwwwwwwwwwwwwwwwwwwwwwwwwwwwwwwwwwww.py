import  qrcode

data =  "https://i.pinimg.com/736x/82/98/0a/82980aee3ae65bdb11d7c43058aa3da0.jpg"

qr =  qrcode.make(data)

qr.save("qr.png")