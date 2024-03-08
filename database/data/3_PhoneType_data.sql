LOCK TABLES `PhoneType` WRITE;
/*!40000 ALTER TABLE `PhoneType` DISABLE KEYS */;
INSERT INTO `PhoneType` VALUES (1,'Mobile'),(2,'Home'),(3,'Work'),(4,'Emergency');
/*!40000 ALTER TABLE `PhoneType` ENABLE KEYS */;
UNLOCK TABLES;