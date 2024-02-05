AirBnB Clone Project:

Welcome to the AirBnB clone project! This project aims to build a simplified version of the AirBnB platform. The primary goal is to create a command-line interface (CLI) that allows users to manage AirBnB objects such as users, states, cities, places, etc.

Project Overview:

1. BaseModel Class
To kickstart the project, a parent class named BaseModel has been implemented. This class takes care of the initialization, serialization, and deserialization of future instances. It serves as the foundation for all other classes within the project.

2. Serialization Flow
The project establishes a simple flow of serialization and deserialization:

Instance <-> Dictionary <-> JSON String <-> File
This process enables the conversion of Python objects to a format that can be easily stored in files and later reconstructed.

3. AirBnB Classes
The project defines various classes for AirBnB objects, and these classes inherit from the BaseModel. Some of the initial classes include User, State, City, and Place. Each class is designed to represent a specific entity within the AirBnB ecosystem.

4. Abstracted Storage Engine
The project introduces the first abstracted storage engine: File storage. This engine is responsible for storing and retrieving serialized objects to and from files. It plays a crucial role in persisting data across sessions.

5. Unit Testing
Comprehensive unit tests have been implemented to validate the functionality of each class and the storage engine. These tests ensure the correctness of the implementation and help maintain code reliability.

Getting Started

Follow these steps to get started with the AirBnB clone project:

Clone the repository: git clone [repository_url]
Navigate to the project directory: cd airbnb_clone
Run the command-line interpreter: python3 console.py
Start managing AirBnB objects using the CLI commands.
CLI Commands

The CLI supports a variety of commands for creating, updating, deleting, and querying AirBnB objects. Refer to the command documentation for a complete list of available commands.

Contribution Guidelines

Contributions to the project are welcome! Please follow the guidelines outlined in the CONTRIBUTING.md file to ensure a smooth collaboration process.


