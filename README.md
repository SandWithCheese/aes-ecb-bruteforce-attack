# Implementasi Algoritma Brute Force untuk Mengeksploitasi Kelemahan Keamanan pada Metode Enkripsi AES-ECB

## Deskripsi Permasalahan

Enkripsi AES dalam mode ECB memiliki celah keamanan yang dikenal karena sifatnya yang deterministik. Ini berarti bahwa jika plaintext yang sama dienkripsi dua kali dengan key yang sama, hasil enkripsinya akan sama. Pada implementasi tertentu, jika plaintext memiliki pola tertentu atau jika serangkaian plaintext yang berbeda dienkripsi dengan key yang sama, serangkaian blok ciphertext yang sama akan dihasilkan.

Eksploitasi enkripsi AES-EBC mungkin terjadi ketika terdapat service yang memungkinkan penggunaan key yang sama untuk mengenkripsi banyak plaintext. Dalam kasus ini, penyerang dapat menggunakan pendekatan brute force, yaitu mencoba semua kemungkinan kombinasi plaintext untuk menemukan pola yang sesuai dengan ciphertext yang diberikan. Dengan menggunakan scripting Python atau bahasa pemrograman lainnya, penyerang dapat secara otomatis memanipulasi input dan membandingkan blok-blok enkripsi dengan pola yang sudah diketahui.

## Cara Menjalankan Program

1. Buat virtual environment python

   ```bash
   python -m venv .venv
   ```

2. Aktivasi virtual environment python

   Jika menggunakan Linux, gunakan command berikut:

   ```bash
   source .venv/bin/activate
   ```

   Jika menggunakan Windows, gunakan command berikut:

   ```bash
   .\.venv\Scripts\activate
   ```

3. Install seluruh requirements

   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan server

    ```bash
    python server.py
    ```

5. Gunakan terminal yang lain, jalankan attack

    ```bash
    python attack.py
    ```

## Pembuat Program

| NAMA ANGGOTA         | NIM      |
|----------------------|----------|
| Ahmad Naufal Ramadan | 13522005 |
