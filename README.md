# Student Gradebook & Course Manager

## Project Description

Student Gradebook & Course Manager is a terminal-based Python application for managing students, courses, assessments, grades, and student reports.

The application allows users to register students, create courses, enroll students in courses, add different types of assessments, record grades, calculate averages, and view student reports.

## Features

* Register new students
* View all students
* Search for students by name or ID
* Update student email
* Delete students
* Create courses
* View all courses
* Enroll students in courses
* Add quizzes, exams, and projects
* Record student grades
* Calculate assessment percentages
* Calculate student averages
* Show pass or fail status
* Assign letter grades
* Add teacher comments
* Display student reports
* Validate user input and handle errors

## Object-Oriented Programming

This project uses Object-Oriented Programming concepts.

### Main Classes

* `Assessment` – The parent class for different types of assessments.
* `Quiz` – A child class of `Assessment`.
* `Exam` – A child class of `Assessment`.
* `Project` – A child class of `Assessment`.
* `Student` – Stores student information and enrolled courses.
* `Course` – Manages course information, enrolled students, and assessments.
* `Gradebook` – Manages students, courses, grades, comments, and reports.

## Encapsulation

Encapsulation is used in the `Student` class.

Protected attributes such as `_student_id`, `_name`, and `_email` are used to protect student information.

Getter methods are used to access student information, and the `set_email()` method is used to update the student's email after validating it.

## Inheritance

The `Quiz`, `Exam`, and `Project` classes inherit from the `Assessment` class.

This allows the child classes to reuse the common attributes and methods of the parent class.

For example:

```python
class Quiz(Assessment):
```

## Method Overriding

The child classes override methods such as `display_info()` and `grade_message()`.

This allows each type of assessment to provide its own information and feedback.

## Data Structures

The project uses lists and dictionaries.

### Lists

Lists are used to store:

* Student courses
* Enrolled students
* Assessments

### Dictionaries

Dictionaries are used to store:

* Students
* Courses
* Grades
* Teacher comments

Dictionaries make it easier to find students and courses using unique IDs and codes.

## Custom Features

### 1. Letter Grade System

The program converts a student's average percentage into a letter grade such as:

* A
* B
* C
* D
* F

The program also displays whether the student has passed or failed.

### 2. Teacher Comment System

Teachers can add comments for students in specific courses.

These comments are displayed in the student's report.

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python main.py
```

## Example Workflow

1. Register a student.
2. Create a course.
3. Enroll the student in the course.
4. Add a Quiz, Exam, or Project.
5. Record the student's grade.
6. Add a teacher comment.
7. View the student's report.

## Author

**Manezha Ebrahimi**

Final Python Project: Student Gradebook & Course Manager
