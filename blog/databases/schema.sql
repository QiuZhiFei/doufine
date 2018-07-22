CREATE TABLE `application` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_id` longtext NOT NULL,
  `created_at` longtext NOT NULL,
  `original_pic` longtext NOT NULL,
  `scheme` longtext NOT NULL,
  `text` longtext NOT NULL,
  `title` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;