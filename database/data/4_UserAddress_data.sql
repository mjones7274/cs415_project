LOCK TABLES `UserAddress` WRITE;
/*!40000 ALTER TABLE `UserAddress` DISABLE KEYS */;
INSERT INTO `UserAddress` VALUES (1,1,'100 Fake St','','Fake City','UT','84032','United States',1),
    (2,1,'200 Fake Ave','','Faker City','UT','84033','United States',3),
    (3,2,'200 Fake Ave','','Fakie City','UT','84033','United States',1),
    (4,6,'101 Fake St','','Fake City','UT','12345','United States',2),
    (5,7,'101 Fake St','','Fake City','UT','12345','United States',3),
    (6,3,'100 Fake St','','Fake City','UT','84032','United States',1),
    (7,4,'100 Fake St','','Fake City','UT','84032','United States',3),
    (8,5,'100 Fake St','','Fake City','UT','84032','United States',2),
    (9,8,'100 Fake St','','Fake City','UT','84032','United States',1),
    (10,9,'100 Fake St','','Fake City','UT','84032','United States',3),
    (11,10,'100 Fake St','','Fake City','UT','84032','United States',2),
    (12,11,'100 Fake St','','Fake City','UT','84032','United States',1),
    (13,12,'100 Fake St','','Fake City','UT','84032','United States',1),
    (14,13,'100 Fake St','','Fake City','UT','84032','United States',2),
    (15,14,'100 Fake St','','Fake City','UT','84032','United States',3),
    (16,15,'100 Fake St','','Fake City','UT','84032','United States',1),
    (17,16,'100 Fake St','','Fake City','UT','84032','United States',2);
/*!40000 ALTER TABLE `UserAddress` ENABLE KEYS */;
UNLOCK TABLES;
