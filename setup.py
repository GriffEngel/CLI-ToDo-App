from setuptools import setup

setup(
    name="clitodo",
    version="0.0.1",
    description="Command line app to make lists of tasks based on status",
    entry_points={
        "console_scripts": ["clitodo=main:main"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS independent",
    ],
    python_requires=">=3.5",
)
