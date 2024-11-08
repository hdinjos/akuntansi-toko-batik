-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Nov 08, 2024 at 11:41 AM
-- Server version: 8.0.35
-- PHP Version: 8.2.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `toko_batik`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('2f385a39f5d4');

-- --------------------------------------------------------

--
-- Table structure for table `daftar_akun`
--

CREATE TABLE `daftar_akun` (
  `id` int NOT NULL,
  `code` varchar(5) NOT NULL,
  `name` varchar(200) NOT NULL,
  `category_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `daftar_akun`
--

INSERT INTO `daftar_akun` (`id`, `code`, `name`, `category_id`) VALUES
(2, 'L9RH6', 'Kas', 3),
(3, 'NUYWJ', 'Bank', 3),
(4, 'R9JUJ', 'Persediaan Barang', 3),
(5, 'IQGX2', 'Piutang Usaha', 3),
(6, 'N7LK6', 'Hutang Usaha', 4),
(7, 'COLBQ', 'Modal', 5),
(8, 'XXICP', 'Modal Ditahan', 5),
(9, 'YY2UZ', 'Pendapatan Penjualan Batik', 6),
(10, 'AWCD2', 'Beban Pembelian Barang (HPP)', 7),
(11, '3ZAJX', 'Beban Sewa Toko', 7),
(12, 'HNN53', 'Beban Gaji', 7),
(13, 'H5SDV', 'Beban Listrik dan Air', 7),
(14, 'D75OB', 'Beban Transportasi', 7),
(15, 'DLSBY', 'Beban Pemasaran (Promosi)', 7);

-- --------------------------------------------------------

--
-- Table structure for table `jurnal_umum`
--

CREATE TABLE `jurnal_umum` (
  `id` int NOT NULL,
  `date` date NOT NULL,
  `note` text NOT NULL,
  `debit` float NOT NULL,
  `credit` float NOT NULL,
  `daftar_akun_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `jurnal_umum`
--

INSERT INTO `jurnal_umum` (`id`, `date`, `note`, `debit`, `credit`, `daftar_akun_id`) VALUES
(1, '2024-11-05', 'Penjualan Batik (Pendapatan)	', 20000000, 0, 2),
(3, '2024-11-18', 'Pendaptan Penjualan', 0, 20000000, 9),
(4, '2024-11-05', 'Pembelian Barang Batik (HPP)', 5000000, 0, 10),
(5, '2024-11-06', 'Pembelian Barang Batik (HPP)', 0, 5000000, 2),
(6, '2024-11-05', 'Beban Sewa Toko', 2000000, 0, 11),
(7, '2024-11-06', 'Beban Sewa Toko', 0, 2000000, 2);

-- --------------------------------------------------------

--
-- Table structure for table `kategori_daftar_akun`
--

CREATE TABLE `kategori_daftar_akun` (
  `id` int NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `kategori_daftar_akun`
--

INSERT INTO `kategori_daftar_akun` (`id`, `name`) VALUES
(3, 'Aset'),
(4, 'Kewajiban'),
(5, 'Ekuitas'),
(6, 'Pendapatan'),
(7, 'Beban');

-- --------------------------------------------------------

--
-- Table structure for table `neraca_lajur`
--

CREATE TABLE `neraca_lajur` (
  `id` int NOT NULL,
  `jenis` varchar(5) NOT NULL,
  `debit` float NOT NULL,
  `credit` float NOT NULL,
  `daftar_akun_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `neraca_lajur`
--

INSERT INTO `neraca_lajur` (`id`, `jenis`, `debit`, `credit`, `daftar_akun_id`) VALUES
(2, 'lb', 4000, 0, 5),
(5, 'nrc', 2300, 0, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `daftar_akun`
--
ALTER TABLE `daftar_akun`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `jurnal_umum`
--
ALTER TABLE `jurnal_umum`
  ADD PRIMARY KEY (`id`),
  ADD KEY `daftar_akun_id` (`daftar_akun_id`);

--
-- Indexes for table `kategori_daftar_akun`
--
ALTER TABLE `kategori_daftar_akun`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `neraca_lajur`
--
ALTER TABLE `neraca_lajur`
  ADD PRIMARY KEY (`id`),
  ADD KEY `daftar_akun_id` (`daftar_akun_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `daftar_akun`
--
ALTER TABLE `daftar_akun`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `jurnal_umum`
--
ALTER TABLE `jurnal_umum`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `kategori_daftar_akun`
--
ALTER TABLE `kategori_daftar_akun`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `neraca_lajur`
--
ALTER TABLE `neraca_lajur`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `daftar_akun`
--
ALTER TABLE `daftar_akun`
  ADD CONSTRAINT `daftar_akun_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `kategori_daftar_akun` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `jurnal_umum`
--
ALTER TABLE `jurnal_umum`
  ADD CONSTRAINT `jurnal_umum_ibfk_1` FOREIGN KEY (`daftar_akun_id`) REFERENCES `daftar_akun` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `neraca_lajur`
--
ALTER TABLE `neraca_lajur`
  ADD CONSTRAINT `neraca_lajur_ibfk_1` FOREIGN KEY (`daftar_akun_id`) REFERENCES `daftar_akun` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
