CREATE DATABASE generatordb;

CREATE TABLE users(
   id INT AUTO_INCREMENT PRIMARY KEY NOT NULL ,
   name VARCHAR(100) NOT NULL,
   surnames VARCHAR(150) NOT NULL,
   age VARCHAR(2) NOT NULL,
   email VARCHAR(255) NOT NULL,
   password VARCHAR(255) NOT NULL,
   user_name VARCHAR(200) NOT NULL
);

CREATE TABLE passwords(
    id_password INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE registries(
    id_regist INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    date_regist DATE NOT NULL,
    hour_regist TIME NOT NULL,
    user_id INT,
    CONSTRAINT fk_user_id
    FOREIGN KEY (user_id)
        REFERENCES users(id)
            ON DELETE CASCADE,
    id_password INT,
    CONSTRAINT fk_id_password
    FOREIGN KEY (id_password) 
        REFERENCES passwords(id_password)
            ON DELETE CASCADE
);

CREATE TABLE password_utility(
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    platform_name VARCHAR(100),
    email_used VARCHAR(255),
    ide_password INT,
    CONSTRAINT fk_ide_password
    FOREIGN KEY (ide_password)
        REFERENCES passwords(id_password)
            ON DELETE CASCADE
);