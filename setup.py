from setuptools import setup, find_packages

setup(
    name='Optimization Techniques',
    version='0.1',
    packages=find_packages(),
    install_requires=["numpy","random","matplotlib"],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Keerthivasan S',
    author_email='keerthi77459@gmail.com',
    description='Some Optimization Problems for Machine Learning',
    url='https://github.com/KeerthiVasan-ai/optimization-techniques-lab', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
)
