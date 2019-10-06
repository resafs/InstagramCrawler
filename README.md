# Instagram-Posts-Crawler-Users
Merupakan program yang berguna untuk mendapatkan dan mengolah konten post di Instagram menjadi Dataset.

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

### Tentang
- Tujuan
1. Menghasilkan **Dataset Posts** berupa username, caption, hashtag, likes, dan comments.

- Cara Kerja<br>
1. Program ini akan mengambil followers dari akun pengguna program
2. Kemudian akan dilanjutkan mengambil konten post dari setiap followers
3. Setelah selesai, target selanjutnya akan dipilih dengan cara menargetkan yang memiliki followers terbanyak dari daftar followers pertama
4. Kembali ke langkah 1, tetapi dengan target yang sudah dipilih sebelumnya
5. Program akan berhenti ketika koneksi tidak mendukung atau mencapai besar data yang ditentukan dalam format MB (MegaByte).
6. Hasil berupa Dataset Posts dengan format CSV berupa username, caption, hashtag, likes, dan comments.



### Yang di Butuhkan
- Python 3.5+
- Koneksi yang Bagus
- Akun Instagram
- Library Python berupa: selenium, emoji, time, emoji, string, csv, os
- Chrome WebDriver

### Cara Penggunaan
- Mengumpulkan Dataset Posts
1. Unduh/clone repository ini.
2. Install python dan library yang diperlukan. Untuk library dapat diinstall melalui cmd: ```pip install <nama library>```
3. Download Chrome WebDriver dan taruh file exe nya di folder yang sama dengan file ini.
4. Jalankan script python crawl.py dengan mengklik 2x atau dengan command ```InstagramCrawler.py```
5. Isi input nama file akun dan username pertama yang ingin dipakai, kemudian masukan nama file sesuai keinginan
6. Hasil terdapat di folder yang sama seperti penyimpan code ```InstagramCrawler.py```

## Kontak

- Resa Fajar Sukma - [@zeHapOs9875Ea](https://github.com/zeHapOs9875Ea) - rezasukma96@gmail.com
- Muhammad Bagas Pradana - [@bagas050201](https://github.com/bagas050201) - bagaspradana0201@gmail.com

Project Link: [https://https://github.com/zeHapOs9875Ea/InstagramCrawler/](https://github.com/https://github.com/zeHapOs9875Ea/InstagramCrawler/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/zeHapOs9875Ea/InstagramCrawler.svg?style=flat-square
[contributors-url]: https://github.com/zeHapOs9875Ea/InstagramCrawler/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/zeHapOs9875Ea/InstagramCrawler.svg?style=flat-square
[forks-url]: https://github.com/zeHapOs9875Ea/InstagramCrawler/network/members
[stars-shield]: https://img.shields.io/github/stars/zeHapOs9875Ea/InstagramCrawler.svg?style=flat-square
[stars-url]: https://github.com/zeHapOs9875Ea/InstagramCrawler/stargazers
[issues-shield]: https://img.shields.io/github/issues/zeHapOs9875Ea/InstagramCrawler.svg?style=flat-square
[issues-url]: https://github.com/zeHapOs9875Ea/InstagramCrawler/issues
