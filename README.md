# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Permasalahan Bisnis
Permasalahan bisnis yang dihadapi adalah tingginya nilai attrition rate perusahaan Jaya Jaya Maju yang mencapai lebih dari 10%. Nilai Attrition Rate ini menunjukkan banyaknya karyawan yang memutuskan resign dibanding karyawan yang memutuskan untuk terus bekerja diperusahaan tersebut. Banyaknya karyawan yang keluar akan menyebabkan pekerjaan yang sudah berjalan menjadi tertunda, pekerjaan yang harusnya dikerjakan oleh seseorang malah harus tertunda atau dilimpahkan ke pekerja lain agar pekerjaan tersebut bisa selesai. Pekerja yang mendapat beban kerja tambahan akan menyelesaikan pekerjaannya menjadi sedikit lebih lama sehingga alur kerja dalam perusahaan menjadi melambat. Untuk mengetahui hal-hal yang menyebabkan tingginya attrition rate, kita perlu mencari tahu terlebih dahulu faktor faktor yang menyebabkan tingginya attrition rate. Faktor faktor ini bisa berasal baik dari dalam perusahaan seperti fasilitas dan bebam kerja yang diberikan kepada karyawan maupun dari karyawan itu sendiri seperti dari mana dia berasal. Faktor-faktor inilah yang kemudian dipantau dan dijaga nilainya agar nilai attrition rate dapat terus ditekan.
### Cakupan Proyek
1. Membersihkan dan mengolah data awal
2. Menganalisis faktor-faktor yang menyebabkan tingginya Attrition Rate dengan menjawab pertanyaan pada exploratory data analysis dan visualisasi data
3. Membuat business dashboard menggunakan looker.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

Setup environment:

```
pip install numpy pandas matplotlib seaborn squarify
```

## Business Dashboard

Business dashboard proyek ini dibuat menggunakan Google Looker Studio dengan menambahkan fitur filter berdasarkan status karyawan yaitu aktif dan inaktif. Pada dashboard ditampilkan jumlah seluruh karyawan, jumlah karyawan yang aktif dan yang keluar, nilai rata-rata gaji karyawan, nilai rata-rata tahun bekerja karyawan di perusahaan, grafik pie chart perbandingan jumlah berdasarkan status dengan gender, status dengan status pernikahan, attrition rate, dan status dengan bekerja overtime. Selain itu terdapat grafik yang menunjukkan sebaran karyawan berdasarkan usia, departement kerja, bidang pekerjaan, level pekerjaan, jenjang pendidikan, bidang pendidikan yang ditempuh dan kategori gaji karyawan.


Dashboard dibuat dengan menggunakan Google Looker Studio. Dashboard dapat diakses pada link berikut ini:
```
https://lookerstudio.google.com/reporting/e6097218-26aa-4923-b213-27dd7aa18fb7
```
## Conclusion

- Secara total keseluruhan terdapat 1058 karyawan yang bekerja
- Terdapat 879 atau 83% karyawan yang masih aktif bekerja sedangkan 179 atau karyawan 17% memilih untuk keluar dari perusahann.
- Secara keseluruhan karyawan di dominasi oleh laki-laki, tetapi laki-laki juga yang paling banyak keluar dari perusahaan
- secara keseluruhan karyawan di dominasi oleh mereka yang sudah menikah, akan tetapi secara jumlah yang keluar lebih banyak mereka yang masih sigle
- secara keseluruhan karyawan di dominasi oleh lulusan sarjana dan lulusan sarjana juga yang paling banyak keluar dari perusahaan
- Secara keseluruhan departeman rnd yang paling banyak totak karyawan. akan tetapi, departemen rnd juga yang paling banyak keluar dari perusahaan.
- secara keseluruhan karyawan di dominasi oleh karyawan dengan bidang life science, akan tetapi bidang tersebut juga yang paling banyak karyawan yang keluar
- secara total karyawan palimg banyak pada jabatan sales executive, sedangkan yang paling banyak keluar pada bidang laboratory techincian
- secara keseluruhan gaji karyawan masih di bawah rata-rata atau di bawah USD5000 dan karyawan dengan gaji tersebut juga yang paling banyak keluar dari perusahaan.
- karyawan yang masih level 1 menyumbang karyawan yang paling banyak keluar dari perusahaan
- mereka yang bekerja secara overtime yang paling banyak keluar dari perusahaan.

### Rekomendasi Action Items

- Meningkatkan Kesejahteraan Karyawan dengan menaikan gaji karyawan yang masih di bawah rata-rata, Terutama Level dan Bergaji Rendah, Kesimpulan menunjukkan bahwa karyawan dengan gaji di bawah rata-rata (USD5000) dan level 1 memiliki tingkat attrition yang tinggi.
- Fokus pada Retensi Karyawan di Departemen R&D dan Bidang Life Science, Departemen R&D dan bidang Life Science memiliki jumlah karyawan terbanyak, namun juga memiliki attrition rate yang tinggi.
- Memberikan Perhatian Lebih kepada Karyawan Single, Meskipun didominasi oleh karyawan yang sudah menikah, karyawan single memiliki tingkat attrition yang lebih tinggi.
- Mengurangi kerjaan secara overtime kepada karyawan
