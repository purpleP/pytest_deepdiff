from setuptools import setup

setup(
    name='pytest_deepdiff',
    description='Use deepdiff library to compare things in asserts',
    author='Michael Doronin',
    author_email='warrior2031@gmail.com',
    version='0.1',
    entry_points = {
        'pytest11': [
            'pytest_deepdiff = pytest_deepdiff',
        ]
    },
    install_requires=['deepdiff', ],
    classifiers=[
        'Framework :: Pytest',
    ],
)
