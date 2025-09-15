from setuptools import find_packages,setup

setup(
    name='RPPL_MCQ_Generator',
    version='0.0.1',
    author='Sandeep Bhujbal',
    author_email='Sandeepb@Rudayapowers.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)

