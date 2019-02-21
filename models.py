TABLES = {}
TABLES['_users'] = (
    "CREATE TABLE `_users` ("
    "  `uuid` int(11) NOT NULL AUTO_INCREMENT,"
    "  `device_id` varchar(64) NOT NULL,"
    "  PRIMARY KEY (`uuid`),"
    "  UNIQUE (`device_id`)"
    ")")
TABLES['_groups'] = (
    "CREATE TABLE `_groups` ("
    "  `uuid` int(11) NOT NULL,"
    "  `guuid` int(11) NOT NULL,"
    "  `group_name` varchar(32) NOT NULL,"
    "  PRIMARY KEY (`uuid`, `guuid`), KEY `uuid` (`uuid`)"
    ")")
