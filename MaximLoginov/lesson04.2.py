import qrcode

url = 0
text = input("Введите URL сайта, пример (www.example.com): ")
url = text
qr = qrcode.make(text)
qr.save("qr.png")