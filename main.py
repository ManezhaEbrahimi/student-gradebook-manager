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