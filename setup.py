from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='EcoSim',
    version='0.0.1',
    description='A library for ecological systems modeling and simulations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/FlacSy/EcoSim',
    author='FlacSy',
    author_email='flacsy.tw@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib'
    ],
)
