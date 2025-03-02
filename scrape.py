from bs4 import BeautifulSoup

# Path ke file HTML lokal
file_path = r"C:\Polban\Projek 1.1\latihan.html"  # Sesuaikan dengan lokasi file

# Membuka file dan membaca isinya
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parsing HTML menggunakan BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Contoh 1: Mengambil heading utama (h1)
h1 = soup.find('h1')
print('Heading Utama:', h1.get_text() if h1 else 'Tidak ditemukan')

# Contoh 2: Mengambil semua heading (h1 hingga h6)
for level in range(1, 7):
    for heading in soup.find_all(f'h{level}'):
        print(f'H{level}:', heading.get_text())

# Contoh 3: Mengambil semua paragraf dalam <article id="tentang">
tentang = soup.find('article', id='tentang')
if tentang:
    paragraphs = tentang.find_all('p')
    for idx, p in enumerate(paragraphs, 1):
        print(f'Paragraf {idx} dalam Tentang:', p.get_text())

# Contoh 4: Mengambil semua link dalam navigasi
nav = soup.find('nav')
if nav:
    links = nav.find_all('a')
    for link in links:
        print('Link Navigasi:', link.get('href'), '-', link.get_text())

# Contoh 5: Mengambil input pada formulir di footer
footer = soup.find('footer')
if footer:
    inputs = footer.find_all('input')
    for inp in inputs:
        tipe = inp.get('type')
        nama = inp.get('name')
        print('Input Form:', nama, 'Tipe:', tipe)
