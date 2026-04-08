CREATE DATABASE sttracker;
USE sttracker;

CREATE TABLE department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO department VALUES
(1,'Computer'),
(2,'IT'),
(3,'Civil'),
(4,'Mechanical'),
(5,'Electrical'),
(6,'AI & DS');

CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    dob DATE,
    gender VARCHAR(10),
    email VARCHAR(100),
    phone_no VARCHAR(15),
    address VARCHAR(100),
    admission_date DATE,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);

INSERT INTO student VALUES
(1,'Amit Kumar','2002-05-12','Male','amit@gmail.com','9000000001','Ahmedabad','2023-06-15',1),
(2,'Priya Shah','2001-08-22','Female','priya@gmail.com','9000000002','Surat','2023-06-16',2),
(3,'Rohit Patel','2002-01-15','Male','rohit@gmail.com','9000000003','Vadodara','2023-06-17',4),
(4,'Sneha Joshi','2001-11-05','Female','sneha@gmail.com','9000000004','Rajkot','2023-06-18',5),
(5,'Kunal Mehta','2000-07-19','Male','kunal@gmail.com','9000000005','Bhavnagar','2023-06-19',3),
(6,'Nisha Verma','2002-03-30','Female','nisha@gmail.com','9000000006','Junagadh','2023-06-20',6);

CREATE TABLE faculty (
    faculty_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone_no VARCHAR(15),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);

INSERT INTO faculty VALUES
(1,'Rajesh Patel','rajesh@college.com','9876543210',1),
(2,'Neha Shah','neha@college.com','9876543211',2),
(3,'Amit Mehta','amit@college.com','9876543212',4),
(4,'Pooja Desai','pooja@college.com','9876543213',5),
(5,'Kunal Joshi','kunal@college.com','9876543214',3),
(6,'Sneha Trivedi','sneha@college.com','9876543215',6);

CREATE TABLE course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    faculty_id INT,
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)
);

INSERT INTO course VALUES
(101,'DBMS',1),
(102,'Python',2),
(103,'Thermodynamics',3),
(104,'Power Systems',4),
(105,'Construction Planning',5),
(106,'Digital Electronics',6);

CREATE TABLE enrollment (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

INSERT INTO enrollment VALUES
(1,1,101,'2023-07-01'),
(2,2,102,'2023-07-01'),
(3,3,103,'2023-07-01'),
(4,4,104,'2023-07-01'),
(5,5,105,'2023-07-01'),
(6,6,106,'2023-07-01');

CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    attendance_date DATE,
    status VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

INSERT INTO attendance VALUES
(1,1,101,'2024-01-01','Present'),
(2,1,101,'2024-01-02','Present'),
(3,2,102,'2024-01-01','Absent'),
(4,3,103,'2024-01-01','Present'),
(5,4,104,'2024-01-01','Late'),
(6,5,105,'2024-01-01','Absent'),
(7,6,106,'2024-01-01','Present');

CREATE TABLE grade (
    grade_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    marks_obtained INT,
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

INSERT INTO grade VALUES
(1,1,101,85),
(2,2,102,78),
(3,3,103,90),
(4,4,104,65),
(5,5,105,72),
(6,6,106,88);

SELECT * FROM student;
SELECT * FROM faculty;
SELECT * FROM course;
SELECT * FROM enrollment;
SELECT * FROM attendance;
SELECT * FROM grade;

SELECT s.name, d.department_name
FROM student s, department d
WHERE s.department_id = d.department_id;

SELECT name FROM student WHERE department_id = 1;

SELECT s.name, g.marks_obtained
FROM student s, grade g
WHERE s.student_id = g.student_id AND g.marks_obtained > 80;

SELECT name FROM student ORDER BY name LIMIT 3;

SELECT s1.name AS student1, s2.name AS student2, s1.department_id
FROM student s1
JOIN student s2
ON s1.department_id = s2.department_id
AND s1.student_id <> s2.student_id;

SELECT d.department_name, COUNT(s.student_id) AS total_students
FROM department d
JOIN student s
ON d.department_id = s.department_id
GROUP BY d.department_name
HAVING COUNT(s.student_id) > 1;

UPDATE attendance
SET status = 'Present'
WHERE student_id = 2 AND attendance_date = '2024-01-01';

UPDATE grade
SET marks_obtained = 80
WHERE student_id = 4 AND course_id = 104;

DELETE FROM attendance
WHERE status = 'Late';

DELETE FROM enrollment
WHERE student_id = 6;


SELECT name FROM student WHERE department_id <> 2;

SELECT d.department_name, COUNT(s.student_id)
FROM department d, student s
WHERE d.department_id = s.department_id
GROUP BY d.department_name;

SELECT c.course_name, AVG(g.marks_obtained)
FROM course c, grade g
WHERE c.course_id = g.course_id
GROUP BY c.course_name;

SELECT MAX(marks_obtained) FROM grade;
SELECT MIN(marks_obtained) FROM grade;
SELECT SUM(marks_obtained) FROM grade;

SELECT s.name, g.marks_obtained
FROM student s, grade g
WHERE s.student_id = g.student_id
AND g.marks_obtained > (SELECT AVG(marks_obtained) FROM grade);

SELECT s.name, c.course_name, f.name
FROM student s, enrollment e, course c, faculty f
WHERE s.student_id = e.student_id
AND e.course_id = c.course_id
AND c.faculty_id = f.faculty_id;

SELECT DISTINCT department_id FROM student;
SELECT name FROM student WHERE name LIKE 'A%';
SELECT name FROM student WHERE department_id IN (1,2);
SELECT name FROM student WHERE department_id NOT IN (3,4);

SELECT student_id, COUNT(attendance_id)
FROM attendance
GROUP BY student_id;

SELECT status, COUNT(status)
FROM attendance
GROUP BY status;

SELECT s.name, c.course_name
FROM student s
INNER JOIN enrollment e ON s.student_id = e.student_id
INNER JOIN course c ON e.course_id = c.course_id;

SELECT s.name, c.course_name
FROM student s
LEFT JOIN enrollment e ON s.student_id = e.student_id
LEFT JOIN course c ON e.course_id = c.course_id;

SELECT s.name, c.course_name
FROM student s
RIGHT JOIN enrollment e ON s.student_id = e.student_id
RIGHT JOIN course c ON e.course_id = c.course_id;

CREATE VIEW student_department_view AS
SELECT s.student_id, s.name, d.department_name
FROM student s
INNER JOIN department d ON s.department_id = d.department_id;

SELECT * FROM student_department_view;

SELECT student_id,
(SUM(status='Present')/COUNT(*))*100 AS attendance_percentage
FROM attendance
GROUP BY student_id;

SELECT student_id, marks_obtained,
CASE
WHEN marks_obtained >= 85 THEN 'Distinction'
WHEN marks_obtained >= 70 THEN 'First Class'
WHEN marks_obtained >= 50 THEN 'Pass'
ELSE 'Fail'
END AS result
FROM grade;
