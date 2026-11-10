# Mini Binary Analyzer

Mini Binary Analyzer adalah alat command-line berbasis Python untuk melihat informasi dasar file dan menganalisis beberapa struktur file ELF. Hasil ditampilkan sebagai tabel di terminal menggunakan [Rich](https://github.com/Textualize/rich).

## Status Project

Project ini masih dalam tahap pengembangan aktif. Fitur, opsi command-line, dan cara penggunaan dapat berubah seiring penambahan fitur dan perbaikan. README ini akan diperbarui agar sesuai dengan kemampuan project saat ini.

## Fitur

- Mendeteksi format berdasarkan magic bytes: ELF, PE, PNG, dan PDF.
- Menampilkan nama file, ukuran file, dan magic bytes.
- Mengekstrak string ASCII yang dapat dicetak (minimal 4 karakter).
- Melihat section ELF, termasuk offset, ukuran, flags, dan preview data.
- Melihat dynamic symbol ELF.
- Melihat dynamic dependencies ELF.

> Pemeriksaan section, symbol, dan dependencies hanya ditujukan untuk file ELF. File yang tidak valid atau bukan ELF dapat menghasilkan error.

## Persyaratan

- Python 3.10 atau lebih baru.
- `pip`.

## Instalasi

Clone repository, lalu pindah ke folder project:

```bash
git clone <URL-REPOSITORY>
cd MiniBinaryAnalyzer
```

Disarankan menggunakan virtual environment:

```bash
python -m venv .venv
```

Aktifkan environment:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

Install dependency:

```bash
pip install -r requirements.txt
```

## Penggunaan

Semua perintah dijalankan dari folder utama project.

Tampilkan informasi dasar file:

```bash
python main.py path/to/file
```

Di Windows, contoh path file:

```powershell
python main.py .\sample.exe
```

Ekstrak string ASCII:

```bash
python main.py --strings path/to/file
```

Inspeksi section ELF:

```bash
python main.py --sections path/to/elf
```

Inspeksi symbol ELF:

```bash
python main.py --symbols path/to/elf
```

Inspeksi dynamic dependencies ELF:

```bash
python main.py --dependencies path/to/elf
```

Jalankan semua pemeriksaan yang tersedia melalui CLI:

```bash
python main.py --all path/to/file
```

`--all` menjalankan deteksi format, ekstraksi strings, serta pemeriksaan ELF sections, symbols, dan dependencies. Karena pemeriksaan ELF hanya cocok untuk file ELF, gunakan opsi ini pada file ELF agar semua pemeriksaan dapat berjalan sesuai tujuan.

Untuk melihat opsi CLI:

```bash
python main.py --help
```
## Catatan

- Opsi analisis hanya dapat dipilih satu per perintah, kecuali `--all`.
- Ekstraksi string saat ini hanya mencari karakter ASCII yang dapat dicetak, dengan panjang minimum 4 karakter.
- Modul pemeriksaan keamanan (`security_analyzer.py`) tersedia di source code, tetapi belum terhubung ke CLI.
- Dependency di `requirements.txt` dipasang sekaligus menggunakan `pip install -r requirements.txt`.


## Catatan lagi 
project ini juga masih dalam masa pengembangan jadi masih akan ada update fitur yang akan datang mulai dari:
-  menganalasisis secara static hingga dynamic 
- melakukan patching dalam binary 
- hingga bisa menganalisa beberapa kerentanan dalam sebuah softwre hingga memory coruption 


## Lisensi

Belum ada lisensi yang ditentukan. Tambahkan file lisensi sebelum mendistribusikan project jika diperlukan.
