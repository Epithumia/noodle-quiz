from typing import TextIO, List
from .exc import InvalidFieldValue
from .question_types import Question


class Quiz:
    def __init__(self, questions: List[Question] = None):

        if questions is None:
            questions = []
        self.questions = questions

    def add_questions(self, questions: Question | List[Question]):
        if type(questions) == Question:
            questions = [questions]

        if type(questions) != list:
            raise InvalidFieldValue('questions', questions, 'questions must be a Question or a list of Questions')

        for q in questions:
            self.questions.append(q)

    def clear_questions(self):
        self.questions.clear()

    def save_to_file(self, f: TextIO):
        s = str(self)
        f.write(s)

    def save_to_path(self, fp: str):
        with open(fp, 'w') as f:
            self.save_to_file(f)

    def __str__(self):
        s = '<?xml version="1.0" encoding="UTF-8"?>\n<quiz>\n'
        for q in self.questions:
            s += str(q)
        s += '\n</quiz>'
        return s
