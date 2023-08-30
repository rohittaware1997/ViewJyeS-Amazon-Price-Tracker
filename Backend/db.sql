
CREATE TABLE USER (
    email_id varchar(255) NOT NULL UNIQUE,
    first_name varchar(255),
    last_name varchar(255),
    PRIMARY KEY (email_id)
);

CREATE TABLE PRODUCT (
    asin_id varchar(255) NOT NULL UNIQUE PRIMARY KEY,
    name varchar(255) NOT NULL UNIQUE,
    amazon_link varchar(255),
    PRIMARY KEY (asin_id)
);

CREATE TABLE CRON_DETAILS (
    email_asin varchar(255) NOT NULL UNIQUE PRIMARY KEY,
    current_price varchar(255) DEFAULT 0,
    linux_command varchar(255),
    notification BOOLEAN DEFAULT FALSE,
    notification_type INTEGER DEFAULT 0,
  	email_id varchar(255),
  	asin_id varchar(255),
  	PRIMARY KEY (email_asin),
    FOREIGN KEY (email_id) REFERENCES USER (email_id),
    FOREIGN KEY (asin_id) REFERENCES PRODUCT (asin_id)
);
/*
HERE email_asin is combination of email#asin (# is separator)
*/
/*Creating new user for register REST API /register*/
INSERT INTO USER (email_id, first_name, last_name);

/*Creating track url REST API /track*/
INSERT INTO PRODUCT (asin_id, name, amazon_link);
INSERT INTO CRON_DETAILS (email_asin, current_price, linux_command, notification, notification_type, email_id, asin_id);

/*get all products for given user given email_id */
SELECT p.name, p.asin_id, p.amazon_link, c.notification, c.notification_type
FROM USER u INNER JOIN CRON_DETAILS c on u.email_id = c.email_id
            INNER JOIN PRODUCT p on p.asin_id = c.asin_id
WHERE u.email_id = {INPUT EMAIL Id}

/* delete cron for given product given asin_id 1) first get command 2) delete id
SELECT c.linux_command
FROM CRON_DETAILS c
WHERE email_asin = {email_asin}


DELETE FROM CRON_DETAILS
WHERE email_asin = {email_asin}

/* get current price of the product */
SELECT c.current_price
FROM CRON_DETAILS
WHERE c.email_asin = {email_asin}
