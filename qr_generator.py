import qrcode
import base64

text = "kitlenme başarılı"
encoded = base64.b64encode(text.encode("utf-8")).decode("ascii")

img = qrcode.make(encoded)
img.save("qr_kitlenme_basarili_utf8.png")
