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
