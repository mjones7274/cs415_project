LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'Main','User','muser@email.com','12345','2024-01-18 10:15:03',1,'2024-02-28 09:59:07'),
    (2,'Willie','Nelson','willie.nelson@email.com','12345','2024-01-18 21:40:15',1,'2024-02-08 18:52:27'),
    (3,'James','Hetfield','jhetfield@email.com','12345','2024-01-25 05:12:45',1,'2024-02-27 15:09:51'),
    (4,'Amelia','Earhart','aearhart@email.com','12345','2024-01-29 16:24:33',1,'2024-02-08 18:52:27'),
    (5,'Peewee','Herman','pherman@email.com','12345','2024-01-25 05:12:45',1,'2024-02-08 18:52:27'),
    (6,'Steve','Rogers','srogers@email.com','12345','2024-01-30 05:29:22',1,'2024-01-30 20:37:15'),
    (7,'Jimmy','John','jjohn@email.com','12345','2024-01-25 05:12:45',1,'2024-02-08 18:52:27'),
    (8,'Ronald','McDonald','rmcdonald@email.com','12345','2024-02-08 18:41:45',1,'2024-02-08 18:52:27'),
    (9,'Mario','Jumpman','mjumpman@email.com','12345','2024-02-08 18:53:37',1,'2024-02-08 18:54:02'),
    (10,'Abraham','Lincoln','alincoln@email.com','12345','2024-02-08 19:26:06',1,'2024-02-28 09:59:07'),
    (11,'Jimmy','Dean','jdean@email.com','12345','2024-02-08 19:38:18',1,'2024-02-28 09:59:07'),
    (12,'Sam','Adams','sadams@email.com','12345','2024-02-09 00:38:52',1,'2024-02-28 09:59:07'),
    (13,'George','Washington','gwashington@eamil.com','12345','2024-02-09 00:40:21',1,'2024-02-28 09:59:07'),
    (14,'Thomas','Edison','tedison@email.com','12345','2024-02-09 00:42:45',1,'2024-02-28 09:59:07'),
    (15,'Albert','Einstein','aeinstein@email.com','12345','2024-02-09 00:44:42',1,'2024-02-28 09:59:07'),
    (16,'Jack','Frost','jfrost@email.com','12345','2024-02-09 00:47:24',1,'2024-02-28 09:59:07');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;