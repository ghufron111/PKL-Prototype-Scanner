from fpdf import FPDF
import os

pdf = FPDF()
pdf.set_auto_page_break(0)

img_list = [x for x in os.listdir("feb")]

for img in img_list:
    pdf.add_page(orientation='L')  # Menentukan orientasi halaman sebagai lanskap
    image = "feb\\" + img
    pdf.image(image, x=10, y=10, w=280)  # Sesuaikan koordinat dan ukuran gambar, lebar=280 karena orientasi lanskap
    
pdf.output("images.pdf")
print("PDF conversion completed...")

# Menghapus file gambar setelah dikonversi menjadi PDF
for img in img_list:
    os.remove(os.path.join("feb", img))

print("Image files deleted.")
