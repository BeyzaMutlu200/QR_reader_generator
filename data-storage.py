import json
from qr_reader import  qr_decoder
import cv2

text =qr_decoder(cv2.VideoCapture(0))

# a Python object (dict):
x = {
  "decode": text
  #"sunucu": 

}
# Save as JSON
with open("qr_output.json", "w", encoding="utf-8") as f:
    json.dump(x, f, ensure_ascii=False, indent=4)

print("QR code result saved to qr_output.json")
