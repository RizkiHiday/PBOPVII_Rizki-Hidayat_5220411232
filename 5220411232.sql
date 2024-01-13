-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 13 Jan 2024 pada 12.18
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411232`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `planet_objects`
--

CREATE TABLE `planet_objects` (
  `id` int(255) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `jarak` float NOT NULL,
  `massa` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `space_objects`
--

CREATE TABLE `space_objects` (
  `id` int(255) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `umur` int(255) NOT NULL,
  `tinggi` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `space_objects`
--

INSERT INTO `space_objects` (`id`, `nama`, `umur`, `tinggi`) VALUES
(7, 'Rizki Hidayat ', 19, 176),
(8, 'Rizka ', 22, 165),
(9, 'Riski', 22, 195),
(10, 'Wahyu', 22, 170),
(11, 'Kun', 25, 169);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `planet_objects`
--
ALTER TABLE `planet_objects`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `space_objects`
--
ALTER TABLE `space_objects`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `planet_objects`
--
ALTER TABLE `planet_objects`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `space_objects`
--
ALTER TABLE `space_objects`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

