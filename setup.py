from setuptools import setup, find_packages

setup(
    name='template_python',
    version='0.0.1',
    author='Louie Slocombe',
    author_email='louies@hotmail.co.uk',
    description='Template',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/LouieSlocombe/template_python',
    packages=find_packages(include=['template_python', 'template_python.*']),
    package_data={
        'template_python': [
            'data/*',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    install_requires=[
        'numpy',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
        ],
    },
)
