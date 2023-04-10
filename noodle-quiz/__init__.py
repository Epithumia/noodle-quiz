from typing import TextIO, List
from exc import MandatoryFieldMissing
from question_types import Question


class Quiz:
    def __init__(self, questions: List[Question]):
        if questions is None or len(questions) == 0:
            raise MandatoryFieldMissing('questions')

        self.questions = questions

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
