-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 27, 2023 at 01:17 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `manage_league`
--
CREATE DATABASE IF NOT EXISTS `manage_league` DEFAULT CHARACTER SET utf8 COLLATE utf8_persian_ci;
USE `manage_league`;

-- --------------------------------------------------------

--
-- Table structure for table `league1`
--

CREATE TABLE `league1` (
  `امتیاز` int(3) NOT NULL,
  `ت.گ` int(3) NOT NULL,
  `گ.خ` int(3) NOT NULL,
  `گ.ز` int(3) NOT NULL,
  `باخت` int(2) NOT NULL,
  `تساوی` int(2) NOT NULL,
  `برد` int(2) NOT NULL,
  `بازی` int(2) NOT NULL,
  `تیم` varchar(225) NOT NULL,
  `رتبه` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
