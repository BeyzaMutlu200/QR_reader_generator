## QR Reader & Generator

This project is a Python-based application for creating, reading, and decoding QR codes. It supports both live QR code scanning from a camera and decoding existing QR code images.

---

## Contents

- `qr_generator.py`  
  Used to generate QR codes. Encodes the text in Base64 format and saves it as a `.png` file.

- `qr_reader.py` / `qr.py`  
  Reads and decodes QR codes from a camera. Draws a bounding box around the code and displays the content on the screen.

- `qr-base-reader.py`  
  Used to decode existing QR code images. Visualizes the decoded text with bounding boxes and labels. Can decode Base64 or UTF-8 encoded text.

- `data-storage.py`  
  Saves decoded QR code data in JSON format. For example, the QR code result is stored under the `"decode"` key.

---

## Requirements

- Python 3.x  
- OpenCV (`cv2`)  
- Pillow (`PIL`)  
- pyzbar  
- qrcode  
- base64  

Install dependencies with:

```bash
pip install opencv-python pillow pyzbar qrcode

```

## Usage
# 1. Generate a QR Code
```bash
python qr_generator.py
``` 

The generated QR code will be saved as:

qr_kitlenme_basarili_utf8.png


# 2. Decode a QR Code Image
```bash 
python qr-base-reader.py
```

# Decodes the image and saves:
bounding_box_and_polygon.png

# Example output in terminal:
Çözümlenen QR Metni: kitlenme başarılı

# 3. Read QR Codes from a Live Camera
``` bash
python qr_reader.py
```
Live camera window opens.
Detected QR code output example:
Tespit edilen QR kodu: kitlenme başarılı

Press 'q' to exit the live camera.

# 4.Save QR Code Result as JSON
``` bash
python data-storage.py
```

 ``` bash 
# Output saved to:

qr_output.json

# Example JSON content:
{
  "decode": "kitlenme başarılı"
}

```

## Notes

qr_reader.py and qr.py have similar functionality; you can use either one.

If the camera does not open or frames cannot be captured, relevant error messages will appear in the terminal.

qr-base-reader.py can decode Base64-encoded text.
