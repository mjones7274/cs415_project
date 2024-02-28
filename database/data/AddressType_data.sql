LOCK TABLES `AddressType` WRITE;
/*!40000 ALTER TABLE `AddressType` DISABLE KEYS */;
INSERT INTO `AddressType` VALUES (1,'Home'),(2,'Work'),(3,'Billing'),(4,'Shipping'),(5,'Vacation');
/*!40000 ALTER TABLE `AddressType` ENABLE KEYS */;
UNLOCK TABLES;