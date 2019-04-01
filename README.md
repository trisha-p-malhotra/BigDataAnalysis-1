# BigDataAnalysis-1
Video game sales Dataset analysis


software required for Installation :

MYSQL SERVER Community edition 6.3  ---------  https://www.mysql.com/products/community/
PyCharm Community edition version 2017.3 -------- https://www.jetbrains.com/pycharm/download/#section=windows
R (togaware.com) -------  https://bitbucket.org/kayontoga/rattle/downloads/


-----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
data /code files used for analysis: 

artificial_key_model.mwb
game_desc_sales.csv
genre.csv
platform.csv
publisher.csv
review_table.csv
VGS_project.csv
VGS.csv
eda.py
consolewar.py
consolewars8.py
Linear_Regression.py
Polynomial_Regression.py
reg.py
sql.py

--------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
 
Process: 
---------------------
Creating tables in database
---------------------
There are 2 ways to do this .
option1) 
--open menu in worknbench ... File ----> open model and select the artificial_key_model.mwb file . 
-- once the ER diagram is loaded , open(menu) ....Database ---->Forward Engineer. Once the option is selected , new window will open, prompting the user to create tables from the ER . Click next to create the tables.

option2)

execute the below SQL statements in parallel. 

load the model from MySQL database artificial_key_model.mwb

SQL statements

---------------------
CREATE TABLE IF NOT EXISTS `mydb`.`game_desc_sales` (
  `game_id` BIGINT NOT NULL,
  `game_name` VARCHAR(100) NOT NULL,
  `Year_of_release` INT NOT NULL,
  `Platform` VARCHAR(100) NOT NULL,
  `Genre_id` INT NOT NULL,
  `Publiser` VARCHAR(100) NOT NULL DEFAULT 'N/A',
  `Developer` VARCHAR(100) NOT NULL DEFAULT 'N/A',
  `publisher_id` INT NOT NULL,
  `platform_id` INT NOT NULL,
  `NA_sales` DOUBLE NOT NULL DEFAULT 0,
  `JPN_sales` DOUBLE NOT NULL DEFAULT 0,
  `EU_sales` DOUBLE NOT NULL DEFAULT 0,
  `Other_sales` DOUBLE NOT NULL DEFAULT 0,
  `Global_sales` DOUBLE NOT NULL DEFAULT 0,
  PRIMARY KEY (`game_id`),
  INDEX `fk_game_desc_sales_Genre_table1_idx` (`Genre_id` ASC),
  INDEX `fk_game_desc_sales_Tpublisher1_idx` (`publisher_id` ASC),
  INDEX `fk_game_desc_sales_Platform1_idx` (`platform_id` ASC),
  CONSTRAINT `fk_game_desc_sales_Genre_table1`
    FOREIGN KEY (`Genre_id`)
    REFERENCES `mydb`.`Genre_table` (`genre_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_game_desc_sales_Tpublisher1`
    FOREIGN KEY (`publisher_id`)
    REFERENCES `mydb`.`Tpublisher` (`publisher_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_game_desc_sales_Platform1`
    FOREIGN KEY (`platform_id`)
    REFERENCES `mydb`.`Platform` (`platform_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
---------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Review_table` (
  `game_id` BIGINT NOT NULL,
  `Critic_score` FLOAT NULL DEFAULT NULL,
  `Critic_count` BIGINT NULL DEFAULT 0,
  `User_score` FLOAT NULL DEFAULT NULL,
  `User_count` BIGINT NULL,
  `Sales_table_game_id` BIGINT NOT NULL,
  PRIMARY KEY (`game_id`),
  CONSTRAINT `fk_Review_table_game_desc_sales1`
    FOREIGN KEY (`game_id`)
    REFERENCES `mydb`.`game_desc_sales` (`game_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
-----------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Platform` (
  `platform_id` INT NOT NULL AUTO_INCREMENT,
  `platform_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`platform_id`),
  UNIQUE INDEX `platform_name_UNIQUE` (`platform_name` ASC))
ENGINE = InnoDB

------------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Tpublisher` (
  `publisher_id` INT NOT NULL AUTO_INCREMENT,
  `publisher_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`publisher_id`),
  UNIQUE INDEX `publisher_name_UNIQUE` (`publisher_name` ASC))
ENGINE = InnoDB
------------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Genre_table` (
  `Genre` VARCHAR(20) NOT NULL DEFAULT 'Miscellaneous',
  `genre_id` INT NOT NULL AUTO_INCREMENT,
  UNIQUE INDEX `Genre_UNIQUE` (`Genre` ASC),
  PRIMARY KEY (`genre_id`))
ENGINE = InnoDB

-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

Data Loading

--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------

To load the data , go to SCHEMAS (left side  window) , under that select the DB that has been created now and then select the table , right click on it and select Data import wizard . A new window will be popped asking us to select a file . Select the  file relative to that table name and load that file . 
Similarly do the same for all the remaining tables.

--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------
Analysis . 

--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------
Most of the analysis was done in Python.

To do the EDA analysis 
	execute the eda.py file install the necessary packages(numpy,pandas,matplotlib.pyplot,seaborn).

For the console wars (7th gen)
	 execute the cosolewar.py file

for 8th gen 
	execute consolewars8.py

for the simple linear regression 
	execute the linear.py

for polynomial regression 
	execute Polynomial_Regression.py

Note: use the dataset file, 
make sure the csv file is named VGS.csv,
have the csv file in the same directory
and install the necessary packages(numpy,pandas,matplotlib.pyplot,seaborn).





Optional

creating a ODBC connection string (windows ) 

create a conection string using the database name, username,password and name the connection in DSN field . 

--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------

connecting to R 
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
Install RODBC package in Rattle . 

Once it is installed, 

enter library(rattle)   command 

then enter library(RODBC)  command

then enter rattle()


new window will pop up having the GUI of R .

select the source tab and then look for ODBC .

once the ODBC is selected , enter the DSN name previously created in the DSN field and hit enter .

once this is done, go to the drop box and select the table on which the analysis would be performed.

---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------

connecting to python.

A sample analysis code in sql.py file explains on how to connect to the MYSql server with python editor.



 



