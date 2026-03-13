from setuptools import setup, find_packages
setup(
    name='codebeat',
    version='0.1',
    description='CodeBeat is a line-by-line Python function tracer for debugging and performance analysis. It measures execution time per line across multiple runs, showing mean and standard deviation to identify bottlenecks',
    author='Suman Kumar Raj',
    author_email='sumanraj112002@gmail.com',
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",


)
