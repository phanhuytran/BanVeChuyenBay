-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: airlineht
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (1,'nguyentrong','202cb962ac59075b964b07152d234b70'),(2,'phanhuy','202cb962ac59075b964b07152d234b70');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `airport`
--

LOCK TABLES `airport` WRITE;
/*!40000 ALTER TABLE `airport` DISABLE KEYS */;
INSERT INTO `airport` VALUES (1,'Noi Bai','Ha Noi'),(2,'Tan Son Nhat','TP HCM'),(3,'Cam Ranh','Khanh Hoa'),(4,'Long Khanh','Dong Nai'),(5,'Da Nang','Da Nang'),(6,'Phan Thiet','Binh Thuan'),(7,'Vinh','Vinh'),(8,'Cat Bi','Hai Phong');
/*!40000 ALTER TABLE `airport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `flight schedule`
--

LOCK TABLES `flight schedule` WRITE;
/*!40000 ALTER TABLE `flight schedule` DISABLE KEYS */;
INSERT INTO `flight schedule` VALUES (1,1,6,NULL,'2020-12-06','00:00:00',30,1),(2,1,6,NULL,'2020-12-07','01:00:00',40,1),(3,2,1,NULL,'2020-12-06','02:00:00',30,3),(4,1,4,NULL,'2020-12-07','01:00:00',30,4);
/*!40000 ALTER TABLE `flight schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `plane`
--

LOCK TABLES `plane` WRITE;
/*!40000 ALTER TABLE `plane` DISABLE KEYS */;
INSERT INTO `plane` VALUES (1),(2),(3),(4),(5),(6),(7);
/*!40000 ALTER TABLE `plane` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `seat`
--

LOCK TABLES `seat` WRITE;
/*!40000 ALTER TABLE `seat` DISABLE KEYS */;
INSERT INTO `seat` VALUES (1,1,1),(2,1,1),(3,1,1),(4,1,1),(5,1,1),(6,1,1),(7,1,1),(8,1,1),(9,1,1),(10,1,1),(11,1,1),(12,1,1),(13,1,1),(14,1,1),(15,1,1),(16,2,1),(17,2,1),(18,2,1),(19,2,1),(20,2,1),(21,2,1),(22,2,1),(23,2,1),(24,2,1),(25,2,1),(26,2,1),(27,2,1),(28,2,1),(29,2,1),(30,2,2),(31,1,2),(32,1,2),(33,1,2),(34,1,2),(35,2,2),(36,2,1),(37,1,3),(38,1,3),(39,1,3),(40,2,3),(41,2,3),(42,2,3),(43,2,3);
/*!40000 ALTER TABLE `seat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (1,'Trọng','Nguyễn','ndt050800@gmail.com','0943940261',NULL,1,NULL,'ADMIN'),(2,'Huy','Trần','tph@gmail.com','037733337',NULL,1,'2020-12-06','STAFF');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (1,1,NULL,NULL,'2020-12-06 21:22:00','Quê',NULL,1);
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `type_seat`
--

LOCK TABLES `type_seat` WRITE;
/*!40000 ALTER TABLE `type_seat` DISABLE KEYS */;
INSERT INTO `type_seat` VALUES (1,'class 1',5),(2,'class 2',5);
/*!40000 ALTER TABLE `type_seat` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-07 10:37:47
