from setuptools import setup, find_packages


def requirements(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    print(lines)
    return lines


setup(
    name='ansibleinviewer',
    version='0.1',
    author='Piotr Sykulski',
    author_email='pitersk@gmail.com',
    install_requires=requirements('requirements.txt'),
    python_requires='>=3.4',
    packages=find_packages(),
    entry_points='''
    [console_scripts]
    ansibleinviewer=ansibleinviewer.main:main
    '''

)
