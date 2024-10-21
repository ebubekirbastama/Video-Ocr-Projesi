# Video OCR Analizi Projesi

Bu proje, video dosyalarındaki kareleri analiz etmek için Python ve Tesseract OCR kullanır. Videoyu karelere böler ve her bir karede yer alan metni OCR (Optik Karakter Tanıma) kullanarak analiz eder. Bu, özellikle videolardan çalıntı kart bilgileri gibi metinleri tespit etmek için kullanışlı olabilir.

## Gereksinimler

- Python 3.7+
- OpenCV (`cv2`)
- pytesseract
- Tesseract OCR (kurulumu ve PATH'e eklenmesi gereklidir)

### Kurulum

1. Tesseract OCR yazılımını [buradan](https://github.com/UB-Mannheim/tesseract/wiki) indirip kurun.
2. Bu dizini sistem PATH değişkenine ekleyin (örneğin: `C:\Program Files\Tesseract-OCR`).
3. Gerekli Python kütüphanelerini yükleyin:

   ```sh
   pip install opencv-python pytesseract
   ```

## Kullanım

Kodun kullanımı oldukça basittir. `video.mp4` adlı bir video dosyasını analiz eder ve kareleri `frames` adlı bir klasöre kaydeder.

```python
import cv2
import pytesseract
import os

# Tesseract uygulama yolunu belirtin
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Video dosyasının karelerini bir dizine kaydetme
def video_to_frames(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    video_capture = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        success, frame = video_capture.read()
        if not success:
            break

        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    video_capture.release()

# Karelerdeki metni analiz etme
def analyze_frames_with_ocr(frames_folder):
    for frame_file in os.listdir(frames_folder):
        frame_path = os.path.join(frames_folder, frame_file)
        image = cv2.imread(frame_path)

        # OCR işlemi
        text = pytesseract.image_to_string(image)
        print(f"Metin ({frame_file}):\n{text}\n")

if __name__ == "__main__":
    video_path = "video.mp4"  # Analiz edilecek video dosyası
    output_folder = "frames"  # Karelerin kaydedileceği dizin

    # Videoyu karelere bölme
    video_to_frames(video_path, output_folder)

    # Karelerdeki metni OCR kullanarak analiz etme
    analyze_frames_with_ocr(output_folder)
```

## Açıklamalar

- **video_to_frames(video_path, output_folder)**: Bu fonksiyon, belirtilen video dosyasını karelere böler ve her bir kareyi `output_folder` adlı dizine kaydeder.
- **analyze_frames_with_ocr(frames_folder)**: Bu fonksiyon, belirtilen dizindeki kareleri tek tek analiz eder ve OCR kullanarak metinleri çıkarır.

## Lisans

Bu proje MIT lisansı altındadır.

