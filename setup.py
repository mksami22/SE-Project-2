from setuptools import setup, find_packages

setup(
    name='GITS',
    version='0.1',
    description='GITS project',
    author='CSC510-Group48',
    author_email='gitsimplified@gmail.com',
    packages=find_packages(),
    tests_require=['pytest'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: GITS Project",
    ],

    license='MIT',
    install_requires=[
        'pytest',
    ]
)
