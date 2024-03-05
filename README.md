<h1 align="center">AirBnB Clone Project - Command Interpreter</h1>

###

<div align="center">
  <img height="200" src="https://raw.githubusercontent.com/ELMACHHOUNE/AirBnB_clone/main/hbnb.png"  />
</div>

###

<h2 align="left">Project Description</h2>

###

<p align="left">Welcome to the AirBnB clone project! This is the first step in building a full web application, where we'll be creating an AirBnB-like system. The primary goal of this step is to implement a command interpreter that allows the management of various objects within the project, such as User, State, City, and Place.</p>

###

<h2 align="left">Components of the Project</h2>

###

<p align="left"><b>. BaseModel Class:</b> A parent class responsible for the initialization, serialization, and deserialization of instances.<br><br><b>. Serialization Flow:</b> Establish a simple flow for serialization/deserialization, allowing interaction between instances, dictionaries, JSON strings, and files.<br><br><b>. Object Classes:</b> Create classes for each object type used in AirBnB (User, State, City, Place, etc.), with each class inheriting from the BaseModel.<br><br><b>. File Storage:</b> Implement the first abstracted storage engine for the project, focused on storing objects in files.<br><br><b>. Command Interpreter:</b> Develop a command interpreter capable of performing actions like creating new objects, retrieving objects from files or databases, conducting operations on objects, updating object attributes, and destroying objects.<br><br><b>. Unit Tests:</b> Create comprehensive unit tests to validate the functionality of all classes and the storage engine.</p>

###

<h2 align="left">Command Interpreter</h2>

###

<p align="left">Our command interpreter looks like a mini shell and allow us manage the objects of our project:<br><br>. Create a new object (ex: a new User or a new Place)<br>. Retrieve an object from a file, a database etc…<br>. Do operations on objects (count, compute stats, etc…)<br>. Update attributes of an object<br>. Destroy an object</p>

###

<h3 align="left">. How touse it</h3>

###

| Commands | Sample Usage | Functionality |
|----------|--------------|---------------|
| `help`   | `help`       | Displays all commands available |
| `create` | `create <class>` | Creates a new object (e.g., a new User, Place) |
| `update` | `User.update('123', {'name' : 'Greg_n_Mel'})` | Updates attribute of an object |
| `destroy` | `User.destroy('123')` | Destroys specified object |
| `show`   | `User.show('123')` | Retrieves an object from a file or a database |
| `all`    | `User.all()` | Displays all objects in class |
| `count`  | `User.count()` | Returns count of objects in the specified class |
| `quit`   | `quit` | Exits the command interpreter |


###

<h3 align="left">. Execution</h3>

###

<h5 align="left">Interactive Mode</h5>

###

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
###

<h5 align="left">Non-Interactive Mode</h5>

###

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
###

<h2 align="left">Authors</h2>

###

<h4 align="left">. Mohsine Hourmat Allah</h4>

###

<h4 align="left">. Bilal Eneouisser</h4>

###
