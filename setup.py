from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gasoptics',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,  
    package_data={
        "gasoptics.fluids": ["*.json"],  
    },
    install_requires=[
        "numpy",
    ],
    author='Ali Karimi',
    author_email='karimi1991ali@gmail.com',
    description='A library for thermodynamic and transport property calculations of gases.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/karimialii/gasoptics',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
