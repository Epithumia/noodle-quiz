# Noodle-Quiz
Noodle-Quiz (Not Moodle Quiz generator) is a set of utilities to generate quizzes for Moodle

## Example usage

```python
from noodle_quiz import Quiz
from noodle_quiz.question_types import Description, Numeric, MultipleChoice
from noodle_quiz.answer_types import NumericAnswer, MultipleChoiceAnswer
q = Quiz()
d = Description('Exercice 1', 'Description')
a = NumericAnswer(100, 4)
n = Numeric('Question #1', [a], 'Calculate 2+2')
ans1 = MultipleChoiceAnswer(50, 2)
ans2 = MultipleChoiceAnswer(50, -2)
ans3 = MultipleChoiceAnswer(-100, 4)
qcm = MultipleChoice('QCM1', 'Solve for x: $$x^2 = 4$$', [ans1, ans2, ans3], single_choice=False)
ansX = MultipleChoiceAnswer(100, 42)
ansY = MultipleChoiceAnswer(0, 'Not 42')
qcu = MultipleChoice('QCM2', 'What is the product of 7 by 8 ?', [ansX, ansY])
q.add_questions([d, n, qcm, qcu])
q.save_to_path('test.xml')
```