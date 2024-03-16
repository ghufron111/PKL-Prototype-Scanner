import requests
import cv2
import numpy as np
import os
from datetime import datetime  # Menambahkan impor datetime
import subprocess

url = "http://192.168.62.254:8080/shot.jpg" # Sesuaikan dengan IP pada aplikasi IP Webcam di Smartphone
save_folder = "feb"
save_path_prefix = "captured_image_"  # Awalan nama file gambar yang disimpan
save_path_suffix = ".jpg"  # Ekstensi file gambar yang disimpan
counter = 1  # Counter untuk nomor urut gambar yang disimpan

# Membuat folder 'feb' jika belum ada
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    cv2.imshow("Gl-Tech Lab", cv2.resize(img, (600, 300)))
    
    key = cv2.waitKey(1)
    if key == 27:  # Tekan Esc untuk keluar
        subprocess.run(["python", "pdf_maker.py"])  # Menjalankan pdf_maker.py saat Esc ditekan
        break
    elif key == 32:  # Tekan spasi untuk mengambil gambar
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = os.path.join(save_folder, f"{save_path_prefix}{timestamp}_{counter}{save_path_suffix}")
        cv2.imwrite(save_path, img)
        print("Gambar telah diambil dan disimpan sebagai", save_path)
        counter += 1

cv2.destroyAllWindows()
