
CREATE DATABASE IF NOT EXISTS perpustakaan;
USE perpustakaan;

CREATE TABLE IF NOT EXISTS buku (
    id INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(255) NOT NULL,
    penulis VARCHAR(255) NOT NULL,
    tahun INT NOT NULL
);
CREATE TABLE peminjaman (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_buku INTEGER,
    nama_peminjam TEXT,
    tanggal_pinjam DATE,
    tanggal_kembali DATE
);
CREATE TABLE penerbit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_buku INTEGER,
    nama_penerbit TEXT,
);
