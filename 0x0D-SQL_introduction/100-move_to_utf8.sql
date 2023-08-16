-- converts hbtn_0c_0 database to UTF8 
-- converts Table first_table to UTF8
-- converts Field name in first_table to UTF8
USE `hbtn_0c_0`
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
