# Noodle-Quiz
Noodle-Quiz (Not Moodle Quiz generator) is a set of utilities to generate quizzes for Moodle

## Example usage

```python
from noodle_quiz import Quiz
from noodle_quiz.question_types import Description, Numeric 
from noodle_quiz.answer_types import NumericAnswer
q = Quiz()
d = Description('Exercice 1', 'Description')
a = NumericAnswer(100, 4)
n = Numeric('Question #1', [a], 'Calculate 2+2')
q.add_questions([d, n])
q.save_to_path('test.xml')
```