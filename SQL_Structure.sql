-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 10, 2023 at 04:37 PM
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
-- Database: `quizpro`
--
CREATE DATABASE IF NOT EXISTS `quizpro` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `quizpro`;

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
  `quiztheme` varchar(255) NOT NULL,
  `creationdate` datetime NOT NULL,
  `ownerid` varchar(255) NOT NULL,
  `seqcount` int(11) NOT NULL,
  `isdraft` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `quizid` (`quizid`),
  KEY `ownerid` (`ownerid`)
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
  ADD CONSTRAINT `quizlist_ibfk_1` FOREIGN KEY (`ownerid`) REFERENCES `users` (`userid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
