from typing import List

from .exc import MandatoryFieldMissing, InvalidFieldValue
from .answer_types import NumericAnswer, ClozeAnswer, MultipleChoiceAnswer


class Question:
    pass


class Description(Question):
    def __init__(self, title, text=''):
        if title is None or len(title) == 0:
            raise MandatoryFieldMissing('title')

        self.title = title
        self.text = text

    def __str__(self):
        s = f'<question type="description">\n<name>\n<text>{self.title}</text>\n</name>\n'
        s += f'<questiontext format="html">\n<text><![CDATA[{self.text}]]></text>\n'
        s += '</questiontext>\n<generalfeedback format="html">\n<text></text>\n</generalfeedback>\n' \
             '<defaultgrade>0</defaultgrade>\n<penalty>0.</penalty>\n<hidden>0</hidden>\n</question>'
        return s


class Essay(Question):
    def __init__(self, title, text='', general_feedback='', default_grade=1, is_essay=True, allowed_files=0,
                 required_files=0, penalty=0, response_required=0, hidden=False, grader_info='', response_template='',
                 lines=5):
        if title is None or len(title) == 0:
            raise MandatoryFieldMissing('title')

        if 0 < allowed_files < required_files:
            raise InvalidFieldValue('required_files', required_files,
                                    f'less or equal than allowed files ({allowed_files})')

        self.title = title
        self.text = text
        self.general_feedback = general_feedback
        self.default_grade = default_grade
        self.penalty = penalty
        self.hidden = hidden
        self.is_essay = is_essay
        self.allowed_files = allowed_files
        self.required_files = required_files
        self.response_required = response_required
        self.grader_info = grader_info
        self.response_template = response_template
        self.lines = lines
        if is_essay:
            self.response_format = 'editor'
        else:
            self.response_format = 'noinline'

    def __str__(self):
        s = f'<question type="essay">\n<name>\n<text>{self.title}</text>\n</name>\n'
        s += f'<questiontext format="html">\n<text><![CDATA[{self.text}]]></text>\n</questiontext>\n'
        s += f'<generalfeedback format="html">\n<text>{self.general_feedback}</text>\n</generalfeedback>\n'
        s += f'<defaultgrade>{str(self.default_grade)}</defaultgrade>\n'
        s += f'<penalty>{str(self.penalty)}</penalty>\n'
        s += f'<hidden>{1 if self.hidden else None}</hidden>\n'
        s += f'<responseformat>{self.response_format}</responseformat>\n'
        s += f'<responserequired>{self.response_required}</responserequired>\n'
        s += f'<responsefieldlines>{str(self.lines)}</responsefieldlines>\n'
        if self.allowed_files > 0:
            s += f'<attachments>{str(self.allowed_files)}</attachments>\n'
            s += f'<attachmentsrequired>{str(self.required_files)}</attachmentsrequired>\n'
        else:
            s += '<attachments>0</attachments>\n'
            s += '<attachmentsrequired>0</attachmentsrequired>\n'
        s += f'<graderinfo format="html">\n<text>{self.grader_info}</text>\n</graderinfo>\n'
        s += f'<responsetemplate format="html">\n<text>{self.response_template}</text>\n</responsetemplate>\n'
        s += '</question>\n\n\n'
        return s


class Numeric(Question):
    def __init__(self, title: str, answers: List[NumericAnswer], text='', general_feedback='', default_grade=1,
                 penalty=1, hidden=0, unit_grading_type=0, unit_penalty=0.1, show_units=3, units_left=0):
        if title is None or len(title) == 0:
            raise MandatoryFieldMissing('title')

        if answers is None or len(answers) == 0:
            raise MandatoryFieldMissing('answers')

        if unit_grading_type not in [0, 1]:
            raise InvalidFieldValue('unit_grading_type', unit_grading_type, [0, 1])

        self.title = title
        self.text = text
        self.answers = answers
        self.general_feedback = general_feedback
        self.default_grade = default_grade
        self.penalty = penalty
        self.hidden = hidden

        self.unit_grading_type = unit_grading_type
        self.unit_penalty = unit_penalty
        self.show_units = show_units
        self.units_left = units_left

    def __str__(self):
        s = f'<question type="numerical">\n<name>\n<text>{self.title}</text>\n</name>\n'
        s += f'<questiontext format="html">\n<text><![CDATA[\n{self.text}]]></text>\n</questiontext>\n'
        s += f'<generalfeedback format="html">\n<text>{self.general_feedback}</text>\n</generalfeedback>\n'
        s += f'<defaultgrade>{str(self.default_grade)}</defaultgrade>\n'
        s += f'<penalty>{self.penalty}</penalty>\n'
        s += f'<hidden>{self.hidden}</hidden>\n'
        for a in self.answers:
            s += str(a)
        s += f'<unitgradingtype>{self.unit_grading_type}</unitgradingtype>\n'
        s += f'<unitpenalty>{str(self.unit_penalty)}</unitpenalty>\n'
        s += f'<showunits>{self.show_units}</showunits>\n'
        s += f'<unitsleft>{self.units_left}</unitsleft>\n'
        s += '</question>\n'
        return s


class Cloze(Question):
    def __init__(self, title: str, parts: List[ClozeAnswer], general_feedback='', penalty=0, hidden=0):
        if title is None or len(title) == 0:
            raise MandatoryFieldMissing('title')

        if parts is None or len(parts) == 0:
            raise MandatoryFieldMissing('text')

        self.title = title
        self.parts = parts
        self.general_feedback = general_feedback
        self.penalty = penalty
        self.hidden = hidden

    def __str__(self):
        s = f'<question type="cloze">\n<name>\n<text>{self.title}</text>\n</name>\n'
        s += f'<questiontext format="html">\n<text>' \
             f'<![CDATA[{"".join(str(p) for p in self.parts)}]]>' \
             f'</text>\n</questiontext>\n'
        s += f'<generalfeedback format="html">\n<text>{self.general_feedback}</text>\n</generalfeedback>\n'
        s += f'<penalty>{str(self.penalty)}</penalty>\n'
        s += f'<hidden>{self.hidden}</hidden>\n'
        s += '</question>\n'
        return s


class MultipleChoice(Question):
    def __init__(self, name: str, question_text: str, answers: List[MultipleChoiceAnswer], general_feedback='',
                 default_grade=1, penalty=0.333333, hidden=False, single_choice=True, shuffle_answers=True,
                 answer_numbering='abc', show_std_instructions=True, correct_feedback='',
                 partially_correct_feedback='', incorrect_feedback='', show_num_correct=True):
        if name is None:
            raise MandatoryFieldMissing('name')
        self.name = name

        if question_text is None:
            raise MandatoryFieldMissing('question_text')
        self.question_text = question_text

        if len(answers) == 0:
            raise InvalidFieldValue('answers', answers, 'answers must be a non-empty list of MultipleChoiceAnswer')

        self.answers = answers
        self.general_feedback = general_feedback
        self.default_grade = default_grade
        self.penalty = penalty
        self.hidden = hidden
        self.single_choice = single_choice
        self.shuffle_answers = shuffle_answers
        if answer_numbering not in ['abc']:
            raise InvalidFieldValue('answer_numbering', answer_numbering, str(['abc']))
        self.answer_numbering = answer_numbering
        self.show_std_instructions = show_std_instructions
        self.correct_feedback = correct_feedback
        self.partially_correct_feedback = partially_correct_feedback
        self.incorrect_feedback = incorrect_feedback
        self.show_num_correct = show_num_correct
        self.validate()

    def validate(self):
        total = 0
        if not self.single_choice:
            for a in self.answers:
                if a.fraction > 0:
                    total += a.fraction
            if total < 100:
                raise InvalidFieldValue('Sum of answer fractions', total, 'The total of fractions is less than 100%')
            if total > 100:
                raise InvalidFieldValue('Sum of answer fractions', total, 'The total of fractions is greater than 100%')
        else:
            for a in self.answers:
                if a.fraction == 100:
                    total += 1
                elif 0 < a.fraction < 100:
                    raise InvalidFieldValue('Answers', total,
                                            'There cannot be partially correct (0<fraction<100) answers')
            if total < 1:
                raise InvalidFieldValue('Correct answer', total, 'There must be one correct (fraction=100) answer')
            if total > 1:
                raise InvalidFieldValue('Correct answer', total, 'There must be only one correct (fraction=100) answer')

    def __str__(self):
        s = '<question type="multichoice">\n'
        s += f'<name><text>{self.name}</text></name>\n'
        s += f'<questiontext format="html"><text><![CDATA[{self.question_text}]]></text></questiontext>\n'
        s += f'<generalfeedback format="html"><text>{self.general_feedback}</text></generalfeedback>\n'
        s += f'<defaultgrade>{self.default_grade}</defaultgrade>\n'
        s += f'<penalty>{self.penalty}</penalty>\n'
        s += f'<hidden>{1 if self.hidden else 0}</hidden>\n'
        s += f'<idnumber></idnumber>\n<single>{"true" if self.single_choice else "false"}</single>\n'
        s += f'<shuffleanswers>{"true" if self.shuffle_answers else "false"}</shuffleanswers>\n'
        s += f'<answernumbering>{self.answer_numbering}</answernumbering>\n'
        s += f'<showstandardinstruction>{self.show_std_instructions}</showstandardinstruction>\n'
        s += f'<correctfeedback format="html"><text>{self.correct_feedback}</text></correctfeedback>\n'
        s += f'<partiallycorrectfeedback format="html">' \
             f'<text>{self.partially_correct_feedback}</text>' \
             f'</partiallycorrectfeedback>\n'
        s += f'<incorrectfeedback format="html">' \
             f'<text>{self.incorrect_feedback}</text>' \
             f'</incorrectfeedback>\n'
        if self.show_num_correct:
            s += '<shownumcorrect/>\n'
        for a in self.answers:
            s += str(a)
        s += '</question>'
        return s
