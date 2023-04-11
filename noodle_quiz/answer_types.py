from typing import List

from .exc import MandatoryFieldMissing


class Answer:
    pass


class NumericAnswer(Answer):
    def __init__(self, answer_fraction, value, format='moodle_auto_format', feedback='', tolerance=0):
        if answer_fraction is None:
            raise MandatoryFieldMissing('answer_fraction')

        if value is None:
            raise MandatoryFieldMissing('value')

        self.answer_fraction = answer_fraction
        self.value = value
        self.format = format
        self.feedback = feedback
        self.tolerance = tolerance

    def __str__(self):
        s = f'<answer fraction="{str(self.answer_fraction)}" format="{self.format}">\n'
        s += f'<text>{str(self.value)}</text>\n'
        s += f'<feedback format="html">\n<text>{self.feedback}</text>\n</feedback>\n'
        s += f'<tolerance>{str(self.tolerance)}</tolerance>\n'
        s += '</answer>\n'
        return s


class ClozeItem:
    def __init__(self, answer_fraction, value, feedback='', tolerance=0, is_first=False):
        if answer_fraction is None:
            raise MandatoryFieldMissing('answer_fraction')

        if value is None:
            raise MandatoryFieldMissing('value')

        self.answer_fraction = answer_fraction
        self.value = value
        self.feedback = feedback
        self.tolerance = tolerance
        self.is_first = is_first

    def __str__(self):
        if self.is_first:
            return f'%{str(self.answer_fraction)}%{str(self.value)}:{str(self.tolerance)}#{self.feedback}'
        else:
            return f'~%{str(self.answer_fraction)}%{str(self.value)}:{str(self.tolerance)}#{self.feedback}'


class ClozeAnswer(Answer):
    def __init__(self, items: List[ClozeItem], score: int | float, cloze_type='NUMERICAL', text_before='',
                 text_after=''):
        if items is None or len(items) == 0:
            raise MandatoryFieldMissing('items')

        if score is None:
            raise MandatoryFieldMissing('score')

        self.items = items
        self.score = score
        self.cloze_type = cloze_type
        self.text_before = text_before
        self.text_after = text_after

    def __str__(self):
        s = self.text_before + '\n{'
        s += f'{str(self.score)}:{self.cloze_type}:'
        for item in self.items:
            s += str(item)
        s += '}\n'
        s += f'{self.text_after}'
        return s
