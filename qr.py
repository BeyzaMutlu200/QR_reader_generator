import cv2
from pyzbar.pyzbar import decode

def qr_decoder(input_source):
    cap = input_source

    if not cap.isOpened():
        print("Kamera açılmadı.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kare alınamadı.")
            break

        barcodes = decode(frame)

        for bar_code in barcodes:
            text = bar_code.data.decode("utf-8", errors="replace")
            x, y, w, h = bar_code.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            print("Tespit edilen QR kodu:", text)

        cv2.imshow("HayTurk_QR_Decode", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Kullanım:
qr_decoder(cv2.VideoCapture(0))
