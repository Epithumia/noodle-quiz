from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='noodle_quiz',
      version='0.1.2',
      description='Noodle-Quiz (Not Moodle Quiz generator) is a set of utilities to generate quizzes for Moodle',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.10',
      ],
      url='https://github.com/Epithumia/noodle-quiz',
      author='Epithumia',
      author_email='rafael.lopez@universite-paris-saclay.fr',
      license='MIT',
      packages=['noodle_quiz'],
      include_package_data=True,
      zip_safe=False)
