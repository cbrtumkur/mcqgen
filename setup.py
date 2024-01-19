from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1 ',
    author='Channabasavaraju Tumkur',
    author_email='cbrtumkur@gmail.com',
    install_requires=[ "openai","langchain","streamlit","python-dotenv","pyPDF2"],
    packages=find_packages()
)