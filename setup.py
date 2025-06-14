from setuptools import setup

setup(
    name="cli-todo",
    version="1.0.0",
    description="Command line app to make lists of tasks based on status",
    py_modules=["cli-todo"],
    entry_points={
        "consoles_scripts": [
            "CLIToDo=clitodo:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS independent",
    ],
    python_requires=">=3.5"
    
)