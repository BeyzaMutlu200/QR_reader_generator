## QR Reader & Generator

Bu proje, QR kodları oluşturma, okuma ve çözümleme işlemlerini gerçekleştiren Python tabanlı bir uygulamadır. Proje, hem kameradan canlı QR kod okuma hem de mevcut QR görsellerini çözümleme özelliklerini içerir.

---

## İçerik

- `qr_generator.py`  
  QR kodu oluşturmak için kullanılır. Metni Base64 formatında encode eder ve `.png` dosyası olarak kaydeder.

- `qr_reader.py` / `qr.py`  
  Kameradan QR kodları okur ve çözümler. Kodun üzerine bounding box çizer ve QR kod içeriğini ekranda gösterir.  

- `qr-base-reader.py`  
  Var olan QR kod görsellerini çözümlemek için kullanılır. Çözümlenen metni bounding box ve yazı ile görselleştirir. Base64 veya UTF-8 formatında çözümleme yapar.

- `data-storage.py`  
  QR kodlarından çözülen metni JSON formatında kaydeder. Örnek olarak `"decode"` alanında QR kod sonucu saklanır.

---

## Gereksinimler

- Python 3.x  
- OpenCV (`cv2`)  
- Pillow (`PIL`)  
- pyzbar  
- qrcode  
- base64  

Kurulum için:

```bash
pip install opencv-python pillow pyzbar qrcode
```

## Kullanım
# 1. QR Kod Oluşturma
```bash
python qr_generator.py
``` 
Oluşturulan QR kod qr_kitlenme_basarili_utf8.png olarak kaydedilir.

# 2. QR Kod Görseli Çözümleme
```bash 
python qr-base-reader.py
```

Mevcut .png dosyasını çözümleyerek bounding_box_and_polygon.png olarak kaydeder.

Çözümlenen metin terminalde gösterilir.

# 3. Canlı Kamera ile QR Kod Okuma
``` bash
python qr_reader.py
```

Kameradan QR kod okur ve ekranda gösterir.

Çözülen metin terminalde görünür.

q tuşuna basarak çıkış yapabilirsiniz.

# 4. QR Kod Sonucunu JSON Olarak Kaydetme
python data-storage.py


Çözülen QR kod sonucu qr_output.json dosyasına kaydedilir.
 ``` bash 
Örnek JSON Çıktısı (qr_output.json)
{
  "decode": "kitlenme başarılı"
}
```

## Notlar

qr_reader.py ve qr.py dosyaları benzer işlevleri yapar; istersen tek birini kullanabilirsin.

Kamera açılmazsa veya kare alınamazsa, ilgili hata mesajları terminalde gösterilir.

qr-base-reader.py Base64 ile kodlanmış metinleri çözümleyebilir.
