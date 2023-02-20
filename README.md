# AirBnB clone - The console

<br><br>
## Description

The project at hand is to create an AirBnB clone web application. The first step of this project is to write a command interpreter using Python to manage the objects within the application. This command interpreter will be crucial to the success of the rest of the project, as it will be used for HTML/CSS templating, database storage, API, front-end integration, and more.

The command interpreter will allow users to create new objects, retrieve objects from various sources, perform operations on objects, update object attributes, and destroy objects. The main goal is to build a parent class (called BaseModel) to manage the initialization, serialization, and deserialization of future instances. This will be done by creating a simple flow of serialization/deserialization that goes from Instance <-> Dictionary <-> JSON string <-> file.

Furthermore, all classes that are used for AirBnB (User, State, City, Place, etc.) will inherit from BaseModel. The first abstracted storage engine of the project, File storage, will also be created. Finally, all unittests will be created to validate all the classes and storage engines in the project.

After completing this project, participants will have learned how to create a Python package, create a command interpreter using the cmd module, implement Unit testing in a large project, serialize and deserialize a class, write and read a JSON file, manage datetime, handle UUIDs, and handle named arguments in a function.

The project requires Python scripts that will be compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5). The files should end with a new line, and the first line of each file should be exactly #!/usr/bin/python3. A README.md file, at the root of the folder of the project, is mandatory. The code should use pycodestyle (version 2.7.*), and all the files must be executable.

The project also requires Python unit tests that will be executed by using the command python3 -m unittest discover tests. The files should end with a new line and should be inside a folder called tests. The tests should use the unittest module, and all test files should have the extension .py. The file organization in the tests folder should be the same as the project.

The project requires a strong emphasis on documentation for all modules, classes, and functions. The documentation should be a real sentence explaining the purpose of the module, class, or method, and the length of the documentation will be verified. It is also encouraged to work together on test cases to ensure that no edge cases are missed.

Finally, the project should be stored on a single repository, and there should be one project repository per group.
<br><br>
## Installation

1. Clone the repository with the following command:
```bash
git clone https://github.com/HugoCLI/holbertonschool-AirBnB_clone.git
```

2. Navigate to the project folder:
```bash
cd holbertonschool-AirBnB_clone
```
<br><br>
## Contributors

- Valentin Melia <valentin.melia@holbertonstudents.com>
- Hugo Chilemme <huogo.chilemme@holbertonstudents.com>
- Pauline Parmigiani <pauline.parmigiani@holbertonstudents.com>
