-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 25, 2023 at 10:35 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quizr`
--
CREATE DATABASE IF NOT EXISTS `quizr` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `quizr`;

-- --------------------------------------------------------

--
-- Table structure for table `quizcategories`
--

DROP TABLE IF EXISTS `quizcategories`;
CREATE TABLE IF NOT EXISTS `quizcategories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `categname` varchar(255) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `quizcontents`
--

DROP TABLE IF EXISTS `quizcontents`;
CREATE TABLE IF NOT EXISTS `quizcontents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quizid` varchar(255) NOT NULL,
  `seqnum` int(11) NOT NULL,
  `sideonetype` varchar(255) NOT NULL,
  `sidetwotype` varchar(255) NOT NULL,
  `sideone` varchar(5000) NOT NULL,
  `sidetwo` varchar(5000) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `quizid` (`quizid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `quizlist`
--

DROP TABLE IF EXISTS `quizlist`;
CREATE TABLE IF NOT EXISTS `quizlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quizid` varchar(255) NOT NULL,
  `quizname` varchar(255) NOT NULL,
  `quizcateg` int(3) NOT NULL,
  `creationdate` datetime NOT NULL,
  `lastedit` datetime NOT NULL,
  `ownerid` varchar(255) NOT NULL,
  `seqcount` int(11) NOT NULL,
  `ispublic` tinyint(1) NOT NULL,
  `appearonsearch` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `quizid` (`quizid`),
  KEY `ownerid` (`ownerid`),
  KEY `quizcateg` (`quizcateg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `dob` datetime NOT NULL,
  `regdate` datetime NOT NULL,
  `lastlogin` datetime DEFAULT NULL,
  `sex` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userid` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `quizcontents`
--
ALTER TABLE `quizcontents`
  ADD CONSTRAINT `quizcontents_ibfk_1` FOREIGN KEY (`quizid`) REFERENCES `quizlist` (`quizid`);

--
-- Constraints for table `quizlist`
--
ALTER TABLE `quizlist`
  ADD CONSTRAINT `quizlist_ibfk_1` FOREIGN KEY (`ownerid`) REFERENCES `users` (`userid`),
  ADD CONSTRAINT `quizlist_ibfk_2` FOREIGN KEY (`quizcateg`) REFERENCES `quizcategories` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
