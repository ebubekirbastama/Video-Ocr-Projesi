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
    video_path = "analiz.mp4"  # Analiz edilecek video dosyası
    output_folder = "frames"  # Karelerin kaydedileceği dizin

    # Videoyu karelere bölme
    video_to_frames(video_path, output_folder)

    # Karelerdeki metni OCR kullanarak analiz etme
    analyze_frames_with_ocr(output_folder)
