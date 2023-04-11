# Noodle-Quiz
Noodle-Quiz (Not Moodle Quiz generator) is a set of utilities to generate quizzes for Moodle

## Example usage

```python
from noodle_quiz import Quiz
from noodle_quiz.question_types import Description, Numeric 
q = Quiz()
d = Description('Exercice 1', 'Description')
n = Numeric('Question #1', [4], 'Calculate 2+2')
q.add_questions([d, n])
q.save_to_path('test.xml')
```