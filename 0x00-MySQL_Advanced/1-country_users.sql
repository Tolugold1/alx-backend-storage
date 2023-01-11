-- table with country field consisting of enumeration of
-- countries: US, CO and TN, never null (= default will be
-- the first element of the enumeration, here US)
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    country ENUM('US', 'CO', 'TN') NOT NULL
);
