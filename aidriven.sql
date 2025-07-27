-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 05, 2025 at 07:44 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aidriven`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `ID` int(11) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`ID`, `Username`, `Password`) VALUES
(1, 'Admin', 'admin'),
(2, 'admin1', 'admin1');

-- --------------------------------------------------------

--
-- Table structure for table `apply_details`
--

CREATE TABLE `apply_details` (
  `job_id` varchar(50) NOT NULL,
  `job_name` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `mob` varchar(15) DEFAULT NULL,
  `email_id` varchar(255) DEFAULT NULL,
  `usn_number` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `apply_details`
--

INSERT INTO `apply_details` (`job_id`, `job_name`, `branch`, `name`, `mob`, `email_id`, `usn_number`) VALUES
('3', 'adgfa', 'is', 'Punith', '8618424197', 'punithsuresh1234@gmail.com', '1'),
('3', 'adgfa', 'is', 'test6', '1234567899', 'driveformovies01111@gmail.com', '5'),
('2', 'Schneider Electric', 'ECE,IS,CS', NULL, '9352839220', 'SCHLIDER_ELECTRIC@GMAIL.COM', NULL),
('2', 'Schneider Electric', 'IS', 'AKSHAY GHOOLI ', '9292919192', 'akshay_ghooli@gmail.com', '4MC21IS011'),
('4MC21IS011', NULL, NULL, NULL, NULL, NULL, NULL),
('1', 'Software Developer', 'CSE', 'AMULYA ', '1234567899', 'amulyasrinivas@gmail.com', '4MC21IS012'),
('2', 'Data Analyst', 'ISE', 'HARISH', '9378439843', 'harish1hari123@gmail.com', '4MC21IS058'),
('12', 'Data Scientist', 'AI/ML', 'HARISH', '9378439843', 'harish1hari123@gmail.com', '4MC21IS058'),
('2', 'Data Analyst', 'ISE', 'AMULYA ', '1234567899', 'amulyasrinivas@gmail.com', '4MC21IS012'),
('3', 'adgfa', 'is', 'AMULYA ', '1234567899', 'amulyasrinivas@gmail.com', '4MC21IS012');

-- --------------------------------------------------------

--
-- Table structure for table `candidate_details`
--

CREATE TABLE `candidate_details` (
  `ID` int(11) NOT NULL,
  `FirstName` varchar(50) DEFAULT NULL,
  `MiddleName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `MobileNumber` varchar(15) DEFAULT NULL,
  `EmailID` varchar(100) DEFAULT NULL,
  `TenthPercentage` float DEFAULT NULL,
  `TwelfthPercentage` float DEFAULT NULL,
  `Branch` varchar(50) DEFAULT NULL,
  `USNNumber` varchar(20) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `skills` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `candidate_details`
--

INSERT INTO `candidate_details` (`ID`, `FirstName`, `MiddleName`, `LastName`, `Gender`, `MobileNumber`, `EmailID`, `TenthPercentage`, `TwelfthPercentage`, `Branch`, `USNNumber`, `Password`, `skills`) VALUES
(1, 'AMULYA ', 'S', 'S', 'female', '1234567899', 'amulyasrinivas@gmail.com', 92, 84, 'IS', '4MC21IS012', 'AMU', 'Python,Java,C,SQL'),
(2, 'RUSDHA ', '', 'TANZIL', 'female', '8618424197', 'rushu.tanzil@gmail.com', 86, 78, 'EEE', '4MC21EE088', 'RUSHU@123', 'Electrical basics ,c '),
(3, 'KALAVATHI', 'H', 'N', 'female', '8618424197', 'kalavathi_hn@gmail.com', 89, 94, 'IS', '4MC21IS054', 'KALA@KALA', 'Python,Java,C,SQL'),
(4, 'HARISH', 'H', 'D', 'MALE', '9378439843', 'harish1hari123@gmail.com', 81, 92, 'IS', '4MC21IS058', 'hari1234', 'C,Sql,Python,Java'),
(5, 'VINAY', 'H', 'R', 'MALE', '9378435325', 'vinay123vinu@gmail.com', 96, 98, 'MECHANICAL', '4MC21ME072', 'vinuVinay', 'CAD, thermodynamics, fluid mechanics,manufacturing processes'),
(6, 'A', 'KARTHIK', 'LAL', 'MALE', '6278298920', 'karthukarthik@gmail.com', 96, 98, 'EC', '4MC21EC001', 'karthik@@karthu', 'VSLI,C,Communication'),
(7, 'Gowri', '', 'S', 'Female', '9876543210', 'gowri.s@example.com', 92.5, 88, 'IS', '4MC21IS046', 'securePass123', 'C++, Data Structures, Algorithms, Object-Oriented Programming, Competitive Programming, Software Dev'),
(15, 'Manoj', 'Kumar', 'R', 'Male', '9876543210', 'manoj.kumar@example.com', 85.5, 88.2, 'Mechanical', '4MC21ME001', 'pass123', 'AutoCAD, SolidWorks, Thermodynamics'),
(16, 'Arav', NULL, 'Bhat', 'Male', '9876543211', 'arav.bhat@example.com', 82.4, 87.1, 'Mechanical', '4MC21ME002', 'pass123', 'Fluid Mechanics, CAD, ANSYS'),
(17, 'Abhishek', NULL, 'Reddy', 'Male', '9876543212', 'abhishek.reddy@example.com', 80.2, 85, 'Mechanical', '4MC21ME003', 'pass123', 'Manufacturing, CAM, Robotics'),
(18, 'Mohith', NULL, 'Sharma', 'Male', '9876543213', 'mohith.sharma@example.com', 78.9, 83.2, 'Mechanical', '4MC21ME004', 'pass123', 'Mechanical Design, CNC, Automation'),
(19, 'Rohith', NULL, 'Nayak', 'Male', '9876543214', 'rohith.nayak@example.com', 79.6, 82.8, 'Civil', '4MC21CV001', 'pass123', 'Structural Analysis, AutoCAD, Revit'),
(20, 'Sandeep', NULL, 'Gowda', 'Male', '9876543215', 'sandeep.gowda@example.com', 77.5, 81, 'Civil', '4MC21CV002', 'pass123', 'Building Design, Soil Mechanics, GIS'),
(21, 'Prakash', NULL, 'Naik', 'Male', '9876543216', 'prakash.naik@example.com', 80.1, 84.5, 'Civil', '4MC21CV003', 'pass123', 'Construction Management, RCC, Surveying'),
(22, 'Deeksha', NULL, 'Patil', 'Female', '9876543217', 'deeksha.patil@example.com', 88, 90.1, 'EC', '4MC21EC020', 'pass123', 'VLSI, Embedded Systems, PCB Design'),
(23, 'Ankitha', 'H S', NULL, 'Female', '9876543218', 'ankitha.hs@example.com', 87.2, 89.5, 'EC', '4MC21EC002', 'pass123', 'Wireless Communication, FPGA, Antenna Design'),
(24, 'Anup', 'Athreya', NULL, 'Male', '9876543219', 'anup.athreya@example.com', 86, 88.7, 'EC', '4MC21EC003', 'pass123', 'Signal Processing, IoT, MATLAB'),
(25, 'Bharthesh', NULL, 'R', 'Male', '9876543220', 'bharthesh.r@example.com', 85.4, 87.2, 'EC', '4MC21EC004', 'pass123', 'Microcontrollers, Circuit Design, Arduino'),
(26, 'Bhavya', NULL, 'Shetty', 'Female', '9876543221', 'bhavya.shetty@example.com', 84.9, 86.5, 'EC', '4MC21EC005', 'pass123', 'Digital Electronics, Semiconductor Devices, IoT');

-- --------------------------------------------------------

--
-- Table structure for table `company_details`
--

CREATE TABLE `company_details` (
  `ID` int(11) NOT NULL,
  `CompanyName` varchar(100) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `EmailID` varchar(100) NOT NULL,
  `Website` varchar(100) DEFAULT NULL,
  `ContactNumber` varchar(15) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `company_details`
--

INSERT INTO `company_details` (`ID`, `CompanyName`, `Address`, `EmailID`, `Website`, `ContactNumber`, `Username`, `Password`) VALUES
(1, 'DISH', 'bangalore', '123@gmail.com', 'abcd', '08618424197', 'User', 'new'),
(2, 'TCS', 'Pune', 'info@tcs.com', 'www.tcs.com', '0112233445', 'tcs_user', 'password3'),
(3, 'SCHNEIDER ELECTRIC', 'Mumbai', 'contact@schneider.com', 'www.schneider-electric.com', '0123456789', 'schneider_user', 'password1'),
(4, 'COGNIZANT', 'Chennai', 'info@cognizant.com', 'www.cognizant.com', '0987654321', 'cognizant_user', 'password2'),
(5, 'TOYOTA', 'Bangalore', 'contact@toyota.com', 'www.toyota.com', '0223344556', 'toyota_user', 'password4'),
(6, 'ACCENTURE', 'Hyderabad', 'contact@accenture.com', 'www.accenture.com', '0334455667', 'accenture_user', 'password5'),
(7, 'IBM', 'Delhi', 'info@ibm.com', 'www.ibm.com', '0445566778', 'ibm_user', 'password6'),
(8, 'TEXASAI', 'Noida', 'info@texasai.com', 'www.texasai.com', '0556677889', 'texasai_user', 'password7');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `email`, `message`) VALUES
(1, 'anagha.nadig1@gmail.com', 'Hello ,Tell Me what ?'),
(2, 'anaghapnadig1@gmail.com', 'hello');

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `job_id` int(11) NOT NULL,
  `job_name` varchar(100) NOT NULL,
  `job_location` varchar(100) NOT NULL,
  `number_of_posts` int(11) NOT NULL,
  `branch` varchar(100) NOT NULL,
  `skills` varchar(500) NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `company_address` varchar(100) NOT NULL,
  `company_email_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jobs`
--

INSERT INTO `jobs` (`job_id`, `job_name`, `job_location`, `number_of_posts`, `branch`, `skills`, `company_name`, `company_address`, `company_email_id`) VALUES
(1, 'Software Developer', 'Bangalore', 10, 'CSE', 'Python,Java,C,SQL', '', '', ''),
(2, 'Data Analyst', 'Hyderabad', 5, 'ISE', 'Python,Java,C,SQL', '', '', ''),
(3, 'adgfa', 'afgda', 2342, 'is', 'Python,Java,C,SQL', '', '', ''),
(4, 'AI Engineer', 'Bangalore', 3, 'AI/ML', 'Python,Java,C,SQL', '', '', ''),
(5, 'Backend Developer', 'Pune', 8, 'CSE', 'Python,Java,C,SQL', '', '', ''),
(6, 'Cloud Engineer', 'Noida', 4, 'CSE', 'Python,Java,C,SQL', '', '', ''),
(7, 'Full Stack Developer', 'Bangalore', 6, 'CSE', 'Python,Java,C,SQL', '', '', ''),
(8, 'Machine Learning Engineer', 'Mumbai', 4, 'AI/ML', 'Python,Java,C,SQL', '', '', ''),
(9, 'Cybersecurity Analyst', 'Hyderabad', 5, 'CSE', 'Python,Java,C,SQL', '', '', ''),
(10, 'Blockchain Developer', 'Delhi', 3, 'Blockchain', 'Python,Java,C,SQL', '', '', ''),
(11, 'DevOps Engineer', 'Pune', 7, 'CSE', 'Python,Java,C,SQL', '', '', ''),
(12, 'Data Scientist', 'Chennai', 4, 'AI/ML', 'Python,Java,C,SQL', '', '', ''),
(14, 'Network Engineer', 'Chennai', 7, 'ECE', 'Python,Java,C,SQL', '', '', ''),
(15, 'test', 'abcd', 123, 'CS', 'Python,Java,C,SQL', '', '', ''),
(16, 'test2', 'abcd', 423, 'CS', 'Fluid Mechanics, CAD, ANSYS', '', '', ''),
(17, 'test3', 'abcd', 4233, 'CS', 'C++, Data Structures, Algorithms, Object-Oriented', '', '', ''),
(18, 'test4', 'abcde', 231, 'CS', 'C++, Data Structures, Algorithms, Object-Oriented', 'asdv', 'sjkfdgha', 'liki078@gmail.com'),
(19, 'test5', 'abcde', 2313, 'CS', 'Python,Java,C,SQL', 'asdv', 'sjkfdgha', 'liki078@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `id` int(11) NOT NULL,
  `branch` varchar(255) NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `notification`
--

INSERT INTO `notification` (`id`, `branch`, `message`) VALUES
(7, 'CS', 'CS STUDNETS NEW COMPANY ALTER STAY TUNED!!!'),
(8, 'IS', 'IS STUDNETS STAY TUNED NEW COMPANY ALTEER!!!'),
(9, 'IS', 'AMULYA CALL ME'),
(10, 'CS', '1.AMULYA S S\r\n2.DEEPIKA R S\r\n3.KALAVATHI H N\r\nCONGRATULATIONS TO ABOVE STUDENTS FOR CLEARING APTI OF ACCENTURE\r\n\r\n'),
(11, 'IS', 'ALL OF YOU ASSMEBLE IN ISE COMPUTER LAB FOR APTITUDE'),
(12, 'CS', 'HI'),
(13, 'CS', 'HI'),
(14, 'IS', 'SHRUTHI MA\'AM IS CALLING'),
(15, 'CS', 'hi\r\n');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- Indexes for table `candidate_details`
--
ALTER TABLE `candidate_details`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `USNNumber` (`USNNumber`);

--
-- Indexes for table `company_details`
--
ALTER TABLE `company_details`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `EmailID` (`EmailID`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`job_id`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `candidate_details`
--
ALTER TABLE `candidate_details`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `company_details`
--
ALTER TABLE `company_details`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
