from setuptools import setup, find_packages

setup(
    name='jformat',
    version='0.0.1',
    description='Reformats files to stdout',
    install_requires=['click', 'colorama'],
    entry_points="""
        [console_scripts]
        jformat=jformat.main:main
        """,
    author='John Doe',
    author_email='hangghost@gmail.com',
    packages=find_packages(),
)

# python3 setup.py develop
# which jformat
