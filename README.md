# Ujian Akhir Semester (UAS) - Mata Kuliah PPKPL

## Identitas
- **Nama:** Andri Rahmadani
- **NIM:** 2110817110008

## Daftar Uji Fungsionalitas

### 1. Periksa Fungsi Login
- **Positive: LG_001**
  - **Deskripsi:** Sukses login dengan valid email dan password.
- **Negative: LG_002**
  - **Deskripsi:** Gagal login dengan invalid email dan valid password.
- **Negative: LG_003**
  - **Deskripsi:** Gagal login dengan valid email dan invalid password.

### 2. Periksa Fitur Interaksi Postingan
- **Positive: IP_001**
  - **Deskripsi:** Sukses memberikan upvote di postingan pengguna lain.
- **Positive: IP_002**
  - **Deskripsi:** Sukses memberikan downvote di postingan pengguna lain.
- **Positive: IP_003**
  - **Deskripsi:** Sukses memberikan komentar di postingan pengguna lain.

### 3. Periksa Fitur Pencarian
- **Positive: PC_001**
  - **Deskripsi:** Sukses menampilkan hasil pencarian sesuai dengan kata kunci.
- **Negative: PC_002**
  - **Deskripsi:** Mencari dengan kata kunci tidak valid.

### 4. Membuat Pertanyaan
- **Positive: PT_001**
  - **Deskripsi:** Membuat pertanyaan yang mirip dengan pengguna lain.
- **Negative: PT_002**
  - **Deskripsi:** Membuat pertanyaan mengandung kalimat typo.
- **Positive: PT_003**
  - **Deskripsi:** Membuat pertanyaan valid dan belum pernah ditanyakan oleh pengguna lain.

### 5. Mengedit Kredensial Pekerjaan
- **Negative: KP_001**
  - **Deskripsi:** Menambahkan kredensial pekerjaan dengan tahun tidak valid.
- **Positive: KP_002**
  - **Deskripsi:** Menambahkan kredensial pekerjaan dengan data valid.
- **Positive: KP_003**
  - **Deskripsi:** Menghapus kredensial.

### 6. Follow dan Unfollow Pengguna Lain
- **Positive: FU_001**
  - **Deskripsi:** Mengikuti pengguna lain.
- **Positive: FU_002**
  - **Deskripsi:** Berhenti mengikuti pengguna lain.
