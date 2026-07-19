class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        if self.max_score == 0:
            return 0.0
        return (score / self.max_score) * 100

    def grade_message(self, score):
        pct = self.calculate_percentage(score)
        if pct >= 50:
            return "Good job, you passed!"
        return "Needs more work."

    def display_info(self):
        return f"{self.title} (Max Score: {self.max_score})"

class Quiz(Assessment):
    def display_info(self):
        return f"Quiz: {self.title} | Max Score: {self.max_score}"

    def grade_message(self, score):
        pct = self.calculate_percentage(score)
        if pct >= 85:
            return "Great quiz result!"
        elif pct >= 60:
            return "Passed the quiz."
        return "Needs more practice."

class Exam(Assessment):
    def display_info(self):
        return f"Exam: {self.title} | Max Score: {self.max_score}"

    def grade_message(self, score):
        pct = self.calculate_percentage(score)
        if pct >= 55:
            return "Passed the exam!"
        return "Failed the exam. Try harder next time."

class Project(Assessment):
    def display_info(self):
        return f"Project: {self.title} | Max Score: {self.max_score}"

    def grade_message(self, score):
        pct = self.calculate_percentage(score)
        if pct >= 90:
            return "Excellent project work!"
        elif pct >= 60:
            return "Project approved."
        return "Project needs revision."
class Student:
    def __init__(self, student_id, name, email):
        self._student_id = student_id
        self._name = name
        self._email = email
        self.courses = []

    def get_id(self):
        return self._student_id

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self._email = new_email
            return True
        return False

    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)

    def display_info(self):
        print(f"ID: {self._student_id} | Name: {self._name} | Email: {self._email} | Enrolled in: {self.courses}")


class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []
        self.assessments = []

    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)

    def add_assessment(self, assessment):
        self.assessments.append(assessment)

    def find_assessment(self, title):
        for asm in self.assessments:
            if asm.title.lower() == title.lower():
                return asm
        return None

    def display_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Enrolled Students: {len(self.students)}")
        if self.assessments:
            print("Assessments:")
            for asm in self.assessments:
                print("  - " + asm.display_info())
        else:
            print("Assessments: None")
class Gradebook:
    def __init__(self, passing_grade=55.0):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.comments = {}
        self.passing_grade = passing_grade

    def add_student(self, student):
        s_id = student.get_id()
        if s_id in self.students:
            return False
        self.students[s_id] = student
        self.grades[s_id] = {}
        self.comments[s_id] = {}
        return True

    def add_course(self, course):
        code = course.course_code
        if code in self.courses:
            return False
        self.courses[code] = course
        return True

    def enroll_student(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll_course(course_code)
            course.add_student(student_id)
            if course_code not in self.grades[student_id]:
                self.grades[student_id][course_code] = {}
            return True
        return False

    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            self.courses[course_code].add_assessment(assessment)
            return True
        return False

    def record_grade(self, student_id, course_code, assessment_title, score):
        if student_id not in self.students:
            return "Error: Student not found."
        if course_code not in self.courses:
            return "Error: Course not found."
        student = self.students[student_id]
        if course_code not in student.courses:
            return "Error: Student is not enrolled in this course."
        course = self.courses[course_code]
        assessment = course.find_assessment(assessment_title)
        if not assessment:
            return "Error: Assessment not found in this course."
        if score < 0 or score > assessment.max_score:
            return f"Error: Score must be between 0 and {assessment.max_score}."
        self.grades[student_id][course_code][assessment.title] = score
        return f"Grade saved! Feedback: {assessment.grade_message(score)}"

    def add_comment(self, student_id, course_code, comment_text):
        if student_id in self.students and course_code in self.courses:
            if course_code in self.students[student_id].courses:
                self.comments[student_id][course_code] = comment_text
                return True
        return False

    def calculate_average(self, student_id, course_code):
        if student_id not in self.grades or course_code not in self.grades[student_id]:
            return None
        student_grades = self.grades[student_id][course_code]
        course = self.courses[course_code]
        if not student_grades:
            return None
        total_pct = 0.0
        for title, score in student_grades.items():
            asm = course.find_assessment(title)
            if asm:
                total_pct += asm.calculate_percentage(score)
        return total_pct / len(student_grades)

    def get_letter_grade(self, average):
        if average is None:
            return "N/A"
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def get_pass_fail(self, average):
        if average is None:
            return "No grades yet"
        if average >= self.passing_grade:
            return "Passed"
        return "Failed"

    def show_report(self, student_id):
        if student_id not in self.students:
            print("Student not found!")
            return
        student = self.students[student_id]
        print("\n================ REPORT CARD ================")
        print(f"Student: {student.get_name()} (ID: {student.get_id()})")
        print(f"Email: {student.get_email()}")
        print("---------------------------------------------")
        if not student.courses:
            print("Not enrolled in any courses.")
            return
        for code in student.courses:
            course = self.courses[code]
            print(f"Course: {course.course_code} - {course.course_name}")
            course_grades = self.grades[student_id].get(code, {})
            for title, score in course_grades.items():
                asm = course.find_assessment(title)
                pct = asm.calculate_percentage(score) if asm else 0.0
                print(f"  * {title}: {score}/{asm.max_score} ({pct:.1f}%)")
            avg = self.calculate_average(student_id, code)
            letter = self.get_letter_grade(avg)
            status = self.get_pass_fail(avg)
            if avg is None:
                print("  Average Score: N/A")
            else:
                print(f"  Average Score: {avg:.2f}%")
            print(f"  Letter Grade:  {letter} (Custom Feature)")
            print(f"  Status:        {status}")
            comment = self.comments[student_id].get(code, "No comments.")
            print(f"  Teacher Comment: \"{comment}\"")
            print("---------------------------------------------")

    def search_student(self, query):
        print(f"\nSearching for '{query}':")
        for s_id, student in self.students.items():
            if query.lower() in s_id.lower() or query.lower() in student.get_name().lower():
                student.display_info()

    def delete_student(self, student_id):
        if student_id not in self.students:
            return False
        for course in self.courses.values():
            if student_id in course.students:
                course.students.remove(student_id)
        del self.students[student_id]
        del self.grades[student_id]
        del self.comments[student_id]
        return True

def show_menu():
    print("\n--- GRADEBOOK MENU ---")
    print("1. Register Student")
    print("2. View Registered Students")
    print("3. Create Course")
    print("4. Enroll Student in Course")
    print("5. Add Assessment")
    print("6. Record Student Score")
    print("7. Add Teacher Comment (Custom Feature)")
    print("8. View Student Report")
    print("9. Search Student")
    print("10. Remove Student")
    print("11. Update Student Email")
    print("12. View Course Info")
    print("0. Exit")


def main():
    my_gradebook = Gradebook()
    s1 = Student("S001", "Manezha Ebrahimi", "mnz.ebrahim1@gmail.com")
    my_gradebook.add_student(s1)
    c1 = Course("PY101", "Python Programming")
    my_gradebook.add_course(c1)
    my_gradebook.enroll_student("S001", "PY101")
    my_gradebook.add_assessment("PY101", Quiz("Quiz 1", 10))
    my_gradebook.record_grade("S001", "PY101", "Quiz 1", 8)

    while True:
        show_menu()
        choice = input("Enter option (0-12): ").strip()
        if choice == "1":
            s_id = input("Student ID: ").strip()
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            if s_id and name:
                s = Student(s_id, name, email)
                if my_gradebook.add_student(s):
                    print("Student added!")
                else:
                    print("ID already exists.")
            else:
                print("ID and Name cannot be empty.")
        elif choice == "2":
            if not my_gradebook.students:
                print("No students registered.")
            for student in my_gradebook.students.values():
                student.display_info()
        elif choice == "3":
            code = input("Course Code: ").strip().upper()
            name = input("Course Name: ").strip()
            if code and name:
                c = Course(code, name)
                if my_gradebook.add_course(c):
                    print("Course added!")
                else:
                    print("Course code already exists.")
        elif choice == "4":
            s_id = input("Student ID: ").strip()
            c_code = input("Course Code: ").strip().upper()
            if my_gradebook.enroll_student(s_id, c_code):
                print("Student enrolled!")
            else:
                print("Failed to enroll. Check ID and Course Code.")
        elif choice == "5":
            c_code = input("Course Code: ").strip().upper()
            if c_code not in my_gradebook.courses:
                print("Course not found.")
                continue
            title = input("Assessment Title (e.g. Midterm): ").strip()
            try:
                max_score = float(input("Max Score: "))
            except ValueError:
                print("Must be a number.")
                continue
            print("Type: (1) Quiz (2) Exam (3) Project")
            t = input("Choice: ").strip()
            if t == "1":
                asm = Quiz(title, max_score)
            elif t == "2":
                asm = Exam(title, max_score)
            elif t == "3":
                asm = Project(title, max_score)
            else:
                asm = Assessment(title, max_score)
            my_gradebook.add_assessment(c_code, asm)
            print("Assessment added to course!")
        elif choice == "6":
            s_id = input("Student ID: ").strip()
            c_code = input("Course Code: ").strip().upper()
            title = input("Assessment Title: ").strip()
            try:
                score = float(input("Score: "))
            except ValueError:
                print("Must be a number.")
                continue
            print(my_gradebook.record_grade(s_id, c_code, title, score))
        elif choice == "7":
            s_id = input("Student ID: ").strip()
            c_code = input("Course Code: ").strip().upper()
            comment = input("Teacher Comment: ").strip()
            if my_gradebook.add_comment(s_id, c_code, comment):
                print("Comment added!")
            else:
                print("Could not add comment.")
        elif choice == "8":
            s_id = input("Student ID: ").strip()
            my_gradebook.show_report(s_id)
        elif choice == "9":
            q = input("Enter Name or ID to search: ").strip()
            my_gradebook.search_student(q)
        elif choice == "10":
            s_id = input("Student ID to delete: ").strip()
            if my_gradebook.delete_student(s_id):
                print("Student removed.")
            else:
                print("Student not found.")
        elif choice == "11":
            s_id = input("Student ID: ").strip()
            if s_id in my_gradebook.students:
                new_email = input("New Email: ").strip()
                student = my_gradebook.students[s_id]
                if student.set_email(new_email):
                    print("Email updated!")
                else:
                    print("Invalid email format.")
            else:
                print("Student not found.")
        elif choice == "12":
            c_code = input("Course Code: ").strip().upper()
            if c_code in my_gradebook.courses:
                my_gradebook.courses[c_code].display_info()
            else:
                print("Course not found.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
