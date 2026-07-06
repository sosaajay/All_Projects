CREATE DATABASE UNIVERDB;
USE UNIVERDB;

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

INSERT INTO Departments VALUES
(1, 'Computer Science'),
(2, 'Mathematics'),
(3, 'Physics'),
(4, 'Chemistry'),
(5, 'Electronics'),
(6, 'Mechanical');

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    BirthDate DATE,
    EnrollmentDate DATE
);

INSERT INTO Students VALUES
(1, 'John', 'Doe', 'john.doe@gmail.com', '2000-01-15', '2022-05-01'),
(2, 'Jane', 'Smith', 'jane.smith@gmail.com', '1999-05-25', '2021-05-01'),
(3, 'Amit', 'Patel', 'amit.patel@gmail.com', '2001-03-10', '2023-06-12'),
(4, 'Neha', 'Shah', 'neha.shah@gmail.com', '2000-07-18', '2019-07-20'),
(5, 'Rahul', 'Mehta', 'rahul.mehta@gmail.com', '1998-11-05', '2018-06-30'),
(6, 'Priya', 'Verma', 'priya.verma@gmail.com', '2002-09-22', '2024-01-10');

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    DepartmentID INT,
    Credits INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

INSERT INTO Courses VALUES
(101, 'Introduction to SQL', 1, 3),
(102, 'Data Structures', 1, 4),
(103, 'Biology', 2, 3),
(104, 'Physics', 3, 4),
(105, 'Chemistry', 4, 3),
(106, 'Electronics', 5, 4);

CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    DepartmentID INT,
    Salary INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

INSERT INTO Instructors VALUES
(1, 'Alice', 'Johnson', 'alice.johnson@gmail.com', 1, 80000),
(2, 'Bob', 'Lee', 'bob.lee@gmail.com', 2, 75000),
(3, 'Ravi', 'Kumar', 'ravi.kumar@gmail.com', 1, 90000),
(4, 'Sunita', 'Sharma', 'sunita.sharma@gmail.com', 3, 70000),
(5, 'Anil', 'Gupta', 'anil.gupta@gmail.com', 4, 72000),
(6, 'Meena', 'Bhat', 'meena.bhat@gmail.com', 5, 78000);

CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

INSERT INTO Enrollments VALUES
(1, 1, 101, '2022-08-11'),
(2, 2, 102, '2021-08-11'),
(3, 3, 101, '2023-07-01'),
(4, 3, 102, '2023-07-01'),
(5, 4, 103, '2019-08-05'),
(6, 5, 104, '2018-08-10');

SELECT s.StudentID, s.FirstName, e.CourseID
FROM Students s
INNER JOIN Enrollments e ON s.StudentID = e.StudentID;

SELECT s.StudentID, s.FirstName, e.CourseID
FROM Students s
LEFT JOIN Enrollments e ON s.StudentID = e.StudentID;

SELECT s.StudentID, s.FirstName, e.CourseID
FROM Students s
RIGHT JOIN Enrollments e ON s.StudentID = e.StudentID;

SELECT s.FirstName, c.CourseName
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
JOIN Courses c ON e.CourseID = c.CourseID;

SELECT CourseID
FROM Courses
WHERE Credits > (SELECT AVG(Credits) FROM Courses);

SELECT *
FROM Instructors
WHERE Salary > (SELECT AVG(Salary) FROM Instructors);

SELECT EnrollmentID,
       YEAR(EnrollmentDate) AS EnrollYear,
       MONTH(EnrollmentDate) AS EnrollMonth
FROM Enrollments;

SELECT EnrollmentID,
       DATEDIFF(CURDATE(), EnrollmentDate) AS DaysDifference
FROM Enrollments;

SELECT EnrollmentID,
       DATE_FORMAT(EnrollmentDate, '%d-%m-%Y') AS FormattedDate
FROM Enrollments;

SELECT StudentID, CONCAT(FirstName, ' ', LastName) AS FullName
FROM Students;

SELECT UPPER(FirstName), LOWER(LastName)
FROM Students;

SELECT TRIM(Email) FROM Students;

SELECT EnrollmentID, EnrollmentDate,
       COUNT(*) OVER (ORDER BY EnrollmentDate) AS RunningTotal
FROM Enrollments;

SELECT StudentID, EnrollmentDate,
       CASE
           WHEN EnrollmentDate < '2020-01-01' THEN 'Senior'
           ELSE 'Junior'
       END AS Status
FROM Students;

SELECT *
FROM Students
WHERE EnrollmentDate > '2022-01-01';

SELECT c.*
FROM Courses c
JOIN Departments d ON c.DepartmentID = d.DepartmentID
WHERE d.DepartmentName = 'Mathematics'
LIMIT 5;

SELECT c.CourseName, COUNT(e.StudentID) AS TotalStudents
FROM Courses c
LEFT JOIN Enrollments e ON c.CourseID = e.CourseID
GROUP BY c.CourseName;

SELECT c.CourseName
FROM Courses c
LEFT JOIN Enrollments e ON c.CourseID = e.CourseID
GROUP BY c.CourseID, c.CourseName
HAVING COUNT(e.StudentID) < 3;

SELECT s.StudentID, s.FirstName
FROM Students s
JOIN Enrollments e1 ON s.StudentID = e1.StudentID
JOIN Enrollments e2 ON s.StudentID = e2.StudentID
WHERE e1.CourseID = 101
  AND e2.CourseID = 102;

SELECT s.*
FROM Students s
LEFT JOIN Enrollments e ON s.StudentID = e.StudentID
WHERE e.StudentID IS NULL;

SELECT MAX(Salary) AS MaxSalary
FROM Instructors
WHERE DepartmentID = 1;

SELECT d.DepartmentName, COUNT(e.StudentID) AS TotalStudents
FROM Departments d
JOIN Courses c ON d.DepartmentID = c.DepartmentID
JOIN Enrollments e ON c.CourseID = e.CourseID
GROUP BY d.DepartmentName;

SELECT CONCAT(FirstName, ' ', LastName) AS InstructorName
FROM Instructors;
