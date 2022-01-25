-- MySQL Script generated by MySQL Workbench
-- Tue Jan 25 17:37:11 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema my_Models
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema my_Models
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `my_Models` DEFAULT CHARACTER SET utf8 ;
USE `my_Models` ;

-- -----------------------------------------------------
-- Table `my_Models`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_Models`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_Models`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_Models`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `body` TEXT(500) NULL,
  PRIMARY KEY (`id`),
  INDEX `usr_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `usr`
    FOREIGN KEY (`user_id`)
    REFERENCES `my_Models`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
insert into users (username,email)
values ('Вася Пупкин','Vasya_Pupkin666@example.com');
insert into users (username,email)
values ('Евгений Юрьевич','Evgeniy_Potapov777@example.com');
insert into posts (user_id,body)
values (1,'Hello World');
insert into posts (user_id,body)
values (2,'My homework');
insert into posts (user_id,body)
values (1,'Ignorance is not a problem if there is a desire to learn');
select *from users;
SELECT u.id as ID_пользователя,p.id as ID_сообщения,u.username as Имя_пользователя,p.body as Сообщение
FROM posts p
JOIN users u on u.id = p.user_id;
