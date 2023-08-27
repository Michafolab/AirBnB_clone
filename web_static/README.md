AirBnB Clone License: MIT Build Status




HBnB Logo

Contents
Description
Environment
Further Information
Requirements
Repo Contents
Installation
Usage
Built with




Acknowledgements
Description 📄
This is the first phase of a four phase project, to create a basic clone of the AirBnB web app. In this first phase a basic console was created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.

Environment 💻

Repo Contents 📋
This repository constains the following files:




File	Description



AUTHORS	Contains info about authors of the project





base_model.py	Defines BaseModel class (parent class), and methods




user.py	Defines subclass User




amenity.py	Defines subclass Amenity




city.py	Defines subclass City




place.py	Defines subclass Place




review.py	Defines subclass Review




state.py	Defines subclass State




file_storage.py	Creates new instance of class, serializes and deserializes data




console.py	creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object




test_base_model.py	unittests for base_model




test_user.py	unittests for user




test_amenity.py	unittests for amenity




test_city.py	unittests for city








test_place.py	unittests for place




test_review.py	unittests for review




test_state.py	unittests for state




test_file_storage.py	unittests for file_storage




test_console.py	unittests for console




Installation 🛠️



Clone the repository and run the console.py

$ git clone https://github.com/------/AirBnB_clone.git
Usage 🔧
Method	Description
create	Creates object of given class
show	Prints the string representation of an instance based on the class name and id
all	Prints all string representation of all instances based or not on the class name
update	Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
destroy	Deletes an instance based on the class name and id (save the change into the JSON file)
count	Retrieve the number of instances of a class
help	Prints information about specific command
quit/ EOF	Exit the program
