import qrcode

data = "https://www.roblox.com/games/10722150271/Roblox-obby"
qr = qrcode.make(data)
qr.save("qr.png")