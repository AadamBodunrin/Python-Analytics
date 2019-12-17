-- Show the databases in the whole system
SHOW databases;

-- Create a new database as long as it doesn't exist
CREATE database IF NOT EXISTS SchoolDB;

-- Pick the database we intend to work with
USE SchoolDB;

-- Delete a database. 
-- DROP database SchoolDB;

-- Create a table with columns Student, Course & Enrolls_in
CREATE TABLE IF NOT EXISTS Student (
	ssn VARCHAR(11) NOT NULL PRIMARY KEY, 
	f_name VARCHAR(20) NOT NULL, 
	l_name VARCHAR(20) NOT NULL, 
	phone VARCHAR(10),
	city VARCHAR(20) NOT NULL,
	zip VARCHAR(5) NOT NULL
);

CREATE TABLE IF NOT EXISTS Course (
	number VARCHAR(3) NOT NULL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	room INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Enrolls_in (
	ssn VARCHAR(11) NOT NULL,
	class VARCHAR(3) NOT NULL,
	score FLOAT,
	CONSTRAINT pk_enroll PRIMARY KEY (ssn,class)
);

-- Populate the table Student, Course & Enrolls_in
INSERT IGNORE INTO Student VALUES ("111-22-3333","JOHN","CHILDS","6461231212","New York","10025");
INSERT IGNORE INTO Student (SSN,f_name,l_name,city,zip) VALUES ("123-12-1234","Mary","Arias","New York","10011");
INSERT IGNORE INTO Student VALUES ("555-11-7777","Roberto","Perez","9173335479","San Francisco","94110");
INSERT IGNORE INTO Student VALUES ("222-33-4455","Lila","Pennington","4251231212","Seattle","98105");

INSERT IGNORE INTO Course VALUES ("c1","Data analytics",1127);
INSERT IGNORE INTO Course VALUES ("c2","Python",303);
INSERT IGNORE INTO Course VALUES ("c3","corp fin",331);
INSERT IGNORE INTO Course VALUES ("c4","prod. mgmt",1127);
INSERT IGNORE INTO Course VALUES ("c5","Ethics",303);
INSERT IGNORE INTO Course VALUES ("c6","leadership",303);
INSERT IGNORE INTO Course VALUES ("c7","bus analytics",1127);

INSERT IGNORE INTO Enrolls_in VALUES ("111-22-3333","c1",93.00);
INSERT IGNORE INTO Enrolls_in VALUES ("123-12-1234","c1",87.00);
INSERT IGNORE INTO Enrolls_in VALUES ("111-22-3333","c2",95.00);
INSERT IGNORE INTO Enrolls_in VALUES ("222-33-4455","c3",44.00);
INSERT IGNORE INTO Enrolls_in VALUES ("555-11-7777","c1",36.00);

-- Show table of the database you are using
SHOW tables;

-- View details of table student
DESCRIBE Student;

-- Get everything from table student
SELECT *
	FROM student;

-- From the student table, return all the details of students that live in New York
SELECT *
	FROM student
    WHERE city = 'New York';
    
-- Show only the first and last name of students in New York
SELECT f_name, l_name
	FROM student
    WHERE city = "New York";

-- Show unique entries of cities in table student
SELECT DISTINCT city
	FROM student;

-- return ssn of student ranked by f_name in asending and descending order.
SELECT ssn 
	FROM student 
    ORDER BY f_name ASC;

SELECT ssn 
	FROM student 
    ORDER BY f_name DESC;


SELECT AVG(score)  
	FROM Enrolls_in;
    
SELECT AVG(score)
	FROM Enrolls_in
    WHERE class = "c1";

SELECT class, AVG(score)
	FROM Enrolls_in
    GROUP BY class;

SELECT class, AVG(score)
	FROM Enrolls_in
    GROUP BY class
    HAVING COUNT(score) > 1;
    
SELECT class, AVG(score) AS AVERAGE
	FROM Enrolls_in
    GROUP BY class;

CREATE TEMPORARY TABLE IF NOT EXISTS Averages
	SELECT class, AVG(Score) AS Average
		FROM Enrolls_in
        GROUP BY class;
      
CREATE TEMPORARY TABLE IF NOT EXISTS Summary
	SELECT class, AVG(score) AS average, COUNT(score) AS count
		FROM Enrolls_in
        GROUP BY class
        ORDER BY count DESC;

 DROP TEMPORARY TABLE Averages;
 
SELECT * 
	FROM Summary;

SELECT s.f_name, s.l_name, e.class
	FROM student s, Enrolls_in e
    WHERE s.ssn = e.ssn;

SELECT e.class
	FROM student s, Enrolls_in e
    WHERE s.f_name = "JOHN" AND s.l_name = "CHILDS"
    AND s.ssn = e.ssn AND e.score >= 95;

SELECT c.name
	FROM student s, Enrolls_in e, course c
    WHERE s.f_name = "JOHN" and s.l_name = "CHILDS" 
    AND s.ssn = e.ssn AND e.class = c.number;

SELECT c.number, c.name, c.room, e.ssn, e.score
	FROM course c
    INNER JOIN Enrolls_in e
    ON c.number = e.class;

SELECT c.name
	FROM student s
    INNER JOIN Enrolls_in e ON s.ssn = e.ssn
    INNER JOIN course c ON c.number = e.class
    WHERE s.f_name = "JOHN";