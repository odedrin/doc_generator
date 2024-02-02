from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt', 'r') as req:
        return req.read().splitlines()

setup(
    name='doc_generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=read_requirements(),  # Your dependencies
    entry_points={
        'console_scripts': [
            'setup-git-hook=doc_generator.scripts.setup_git_hook:main',
        ],
    },
)
