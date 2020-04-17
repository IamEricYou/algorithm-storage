# SQL cheat sheet

## Syntax 
>Database & Table

```sql
CREATE DATABASE [database]; -- CREATE DATABSE
DROP DATABASE [database]; -- DELETE DATABASE
-- CREATE TABLE & DATA TYPE DIVERSITY
CREATE TABLE [table] (
    -- NUMBERS
    temp1 BIT(64),
    -- TRUE 1 ,FALSE 0
    temp2 BOOLEAN, 
    -- -128 ~ 127 // 0 ~ 255
    temp3 TINYINT(1),
    -- NOT IMPORTANT
    temp4 SMALLINT(10),
    -- 10 means width of the column
    temp5 INT(10) NOT NULL AUTO_INCREMENT UNIQUE,
    -- BIG BIG INT
    temp6 BIGINT(10),
    temp7 FLOAT(10),
    -- 8 BYTE // THIS IS NOT A STANDARD SYNTAX FOR MYSQL
    temp8 DOUBLE PRECISION(10),
    temp9 REAL(10),

    -- STRING / CHARACTER

    -- TAKES EXACTLY 10 length of memory
    temp10 CHAR(10),
    -- This will allow 5 length of memory if you put 5 chars in this column
    temp11 VARCHAR(10),
    
    temp12 TEXT,
    temp13 LONGTEXT, 

    -- ENUM / SET act like array in sql. 

    -- ETC
    
    -- YYYY-MM-DD
    temp15 DATE,
    -- HH:MM:SS
    temp16 TIME,
    -- YYYY:MM-DD HH:MM:SS
    temp17 DATETIME, 
    temp18 TIMESTAMP(10),
    temp19 YEAR(2)
)ENGINE=InnoDB;
```

> Constraints Reference from [Here](https://www.w3schools.com/sql/sql_constraints.asp)

```sql
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    column3 datatype constraint,
    ....
);

NOT NULL -- Ensures that a column cannot have a NULL value
UNIQUE -- Ensures that all values in a column are different
PRIMARY KEY -- A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
FOREIGN KEY -- Uniquely identifies a row/record in another table
CHECK -- Ensures that all values in a column satisfies a specific condition
DEFAULT -- Sets a default value for a column when no value is specified
INDEX -- Used to create and retrieve data from the database very quickly
```

> ALTER & CHANGE 

```sql
-- ADD
ALTER TABLE [table_name] ADD [column_name] [datatype];
-- DROP
ALTER TABLE [table_name] DROP COLUMN [column_name];
-- MODIFY
ALTER TABLE [table_name] MODIFY COLUMN [column_name] [datatype];\
```

Iamge is from [Here](https://www.jrebel.com/blog)
![](SQL/q1.JPG)