-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 01, 2023 at 12:47 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `obat_pet`
--

-- --------------------------------------------------------

--
-- Table structure for table `supps`
--

CREATE TABLE `supps` (
  `ID` int NOT NULL,
  `Nama_obat` varchar(50) NOT NULL,
  `Harga_obat` int NOT NULL,
  `Deskripsi_obat` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `supps`
--

INSERT INTO `supps` (`ID`, `Nama_obat`, `Harga_obat`, `Deskripsi_obat`) VALUES
(2, 'Obat Kutu', 90000, 'Obat Kutu untuk kucing dan anjing.'),
(3, 'Obat Flu', 150000, 'Obat Flu untuk kucing dan anjing.'),
(15, 'Obat Cacing', 130000, 'Obat Cacing untuk kucing dan anjing.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `supps`
--
ALTER TABLE `supps`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `supps`
--
ALTER TABLE `supps`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
