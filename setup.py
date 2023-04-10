from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='noodle-quiz',
      version='0.1',
      description='Noodle-Quiz (Not Moodle Quiz generator) is a set of utilities to generate quizzes for Moodle',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.10',
      ],
      url='https://github.com/Epithumia/noodle-quiz',
      author='Epithumia',
      author_email='rafael.lopez@universite-paris-saclay.fr',
      license='MIT',
      packages=['noodle-quiz'],
      include_package_data=True,
      zip_safe=False)