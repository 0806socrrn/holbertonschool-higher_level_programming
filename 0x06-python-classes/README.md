# 0x06. Python - Classes and Objects
## Details
      By Guillaume          Weight: 1                Ongoing project - started May 24, 2022 , must end by May 25, 2022           - you're done with 0% of tasks.              Checker was released at May 24, 2022 3:36 PM        An auto review will be launched at the deadline       ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/247/oop-meme.jpg) 

## Background Context
OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum). 
As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!
Read or watch the below resources in the order presented.
## Resources
Read or watch :
* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/izl1kO1isRJo6h_Ce2pmhw) 
 (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes,  ` classmethod `  and  ` staticmethod `  yet)
* [Object-Oriented Programming](https://intranet.hbtn.io/rltoken/hA0enGhhhBgtbDEED2FFYA) 
 (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The  ` __init__ `  Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
* [Properties vs. Getters and Setters](https://intranet.hbtn.io/rltoken/33gDTd_1onhh3vkeKQv-Jw) 

* [Learn to Program 9 : Object Oriented Programming](https://intranet.hbtn.io/rltoken/aFk7Ki8TPw5vZZBx2JXvIQ) 

* [Python Classes and Objects](https://intranet.hbtn.io/rltoken/CFTUXsxbTVu4xb698_2bmQ) 

* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/DK1vkIQ0xT1fmMrmBcSGiA) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/IGj3GprYnPJ9YUl7WM9TEg) 
 ,  without the help of Google :
### General
* Why Python programming is awesome 
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is  ` self ` 
* What is a method
* What is the special  ` __init__ `  method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is the  ` __dict__ `  of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use the  ` getattr `  function
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/python3 ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version  ` 2.8.* ` )
* All your files must be executable
* The length of your files will be tested using  ` wc ` 
* All your modules should have a documentation ( ` python3 -c 'print(__import__("my_module").__doc__)' ` )
* All your classes should have a documentation ( ` python3 -c 'print(__import__("my_module").MyClass.__doc__)' ` )
* All your functions (inside and outside a class) should have a documentation ( ` python3 -c 'print(__import__("my_module").my_function.__doc__)' `  and  ` python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' ` )
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
## More Info
Documentation is now mandatory!  Each module, class, and method must contain docstring as comments.  [Example Google Style Python Docstrings](https://intranet.hbtn.io/rltoken/SYdQnrcR2jL5hIs5TkIN5Q) 

## Trace
To help you with your journey, feel free to try your code  [here](https://intranet.hbtn.io/rltoken/-sgdZGK2LrEOKZ75BGzjYA) 
  with some dedicated test for each task. You will be able to see in real time your code and what is really happening.
You can find  [here](https://intranet.hbtn.io/rltoken/ap_SNmxc3S2iiHVPfgCMwQ) 
  is a quick explanation about how to use it.
### Quiz questions
Great!          You've completed the quiz successfully! Keep going!          (Show quiz)#### 
        
        Question #0
    
 Quiz question Body In this following code, what is   ` User `  ?
```bash
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

```
 Quiz question Answers * A class

* A string

* An attribute

* A method

* An instance

 Quiz question Tips #### 
        
        Question #1
    
 Quiz question Body In this following code, what is   ` id `  ?
```bash
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

```
 Quiz question Answers * A public instance attribute

* A public class attribute

* A public class method

* A public instance method

* A private class attribute

* A protected class attribute

 Quiz question Tips #### 
        
        Question #2
    
 Quiz question Body In this following code, what is   ` __password `  ?
```bash
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

```
 Quiz question Answers * A public class attribute

* A public instance attribute

* A protected class attribute

* A protected instance attribute

* A private class attribute

* A private instance attribute

 Quiz question Tips #### 
        
        Question #3
    
 Quiz question Body In this following code, what is   ` is_new `  ?
```bash
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

```
 Quiz question Answers * A public class attribute

* A public instance attribute

* A protected class attribute

* A protected instance attribute

* A private class attribute

* A private instance attribute

 Quiz question Tips #### 
        
        Question #4
    
 Quiz question Body What do these lines print?
```bash
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.is_new

```
 Quiz question Answers * is_new

* Nothing

* False

* True

 Quiz question Tips #### 
        
        Question #5
    
 Quiz question Body What do these lines print?
```bash
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.id

```
 Quiz question Answers * 89

* id

* User.id

* Nothing

 Quiz question Tips #### 
        
        Question #6
    
 Quiz question Body What do these lines print?
```bash
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User("John")
>>> u.name

```
 Quiz question Answers * name

* None

* John

* no name

 Quiz question Tips #### 
        
        Question #7
    
 Quiz question Body What do these lines print?
```bash
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.name

```
 Quiz question Answers * name

* None

* John

* no name

 Quiz question Tips ## Tasks
### 0. My first square
          mandatory         Progress vs Score  Task Body Write an empty class   ` Square `   that defines a square:
* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/0x06$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x06-python-classes ` 
* File:  ` 0-square.py ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Square with size
          mandatory         Progress vs Score  Task Body Write a class   ` Square `   that defines a square by: (based on   ` 0-square.py `  )
* Private instance attribute:  ` size ` 
* Instantiation with  ` size `  (no type/value verification)
* You are not allowed to import any module
Why?
Why  ` size `  is private attribute?
The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.
```bash
guillaume@ubuntu:~/0x06$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/0x06$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x06-python-classes ` 
* File:  ` 1-square.py ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Size validation
          mandatory         Progress vs Score  Task Body Write a class   ` Square `   that defines a square by: (based on   ` 1-square.py `  )
* Private instance attribute:  ` size ` 
* Instantiation with optional  ` size ` :  ` def __init__(self, size=0): ` *  ` size `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` size must be an integer ` 
* if  ` size `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` size must be >= 0 ` 

* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/0x06$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x06-python-classes ` 
* File:  ` 2-square.py ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Area of a square
          mandatory         Progress vs Score  Task Body Write a class   ` Square `   that defines a square by: (based on   ` 2-square.py `  )
* Private instance attribute:  ` size ` 
* Instantiation with optional  ` size ` :  ` def __init__(self, size=0): ` *  ` size `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` size must be an integer ` 
* if  ` size `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` size must be >= 0 ` 

* Public instance method:  ` def area(self): `  that returns the current square area
* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/0x06$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/0x06$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x06-python-classes ` 
* File:  ` 3-square.py ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Access and update private attribute
          mandatory         Progress vs Score  Task Body Write a class   ` Square `   that defines a square by: (based on   ` 3-square.py `  )
* Private instance attribute:  ` size ` :* property  ` def size(self): `  to retrieve it
* property setter  ` def size(self, value): `  to set it:*  ` size `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` size must be an integer ` 
* if  ` size `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` size must be >= 0 ` 


* Instantiation with optional  ` size ` :  ` def __init__(self, size=0): ` 
* Public instance method:  ` def area(self): `  that returns the current square area
* You are not allowed to import any module
Why?
Why a getter and setter?
Reminder:   ` size `   is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc.Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.
```bash
guillaume@ubuntu:~/0x06$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/0x06$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x06-python-classes ` 
* File:  ` 4-square.py ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Printing a square
          mandatory         Progress vs Score  Task Body Write a class   ` Square `   that defines a square by: (based on   ` 4-square.py `  )
* Private instance attribute:  ` size ` :* property  ` def size(self): `  to retrieve it
* property setter  ` def size(self, value): `  to set it:*  ` size `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` size must be an integer ` 
* if  ` size `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` size must be >= 0 ` 


* Instantiation with optional  ` size ` :  ` def __init__(self, size=0): ` 
* Public instance method:  ` def area(self): `  that returns the current square area
* Public instance method:  ` def my_print(self): `  that prints in stdout the square with the character  ` # ` :* if  ` size `  is equal to 0, print an empty line

* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/0x06$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/0x06$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x06-python-classes ` 
* File:  ` 5-square.py ` 
 Self-paced manual review  Panel footer - Controls 
### 6. Coordinates of a square
          mandatory         Progress vs Score  Task Body Write a class   ` Square `   that defines a square by: (based on   ` 5-square.py `  )
* Private instance attribute:  ` size ` :* property  ` def size(self): `  to retrieve it
* property setter  ` def size(self, value): `  to set it:*  ` size `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` size must be an integer ` 
* if  ` size `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` size must be >= 0 ` 


* Private instance attribute:  ` position ` :* property  ` def position(self): `  to retrieve it
* property setter  ` def position(self, value): `  to set it:*  ` position `  must be a tuple of 2 positive integers, otherwise raise a  ` TypeError `  exception with the message  ` position must be a tuple of 2 positive integers ` 


* Instantiation with optional  ` size `  and optional  ` position ` :  ` def __init__(self, size=0, position=(0, 0)): ` 
* Public instance method:  ` def area(self): `  that returns the current square area
* Public instance method:  ` def my_print(self): `  that prints in stdout the square with the character  ` # ` :* if  ` size `  is equal to 0, print an empty line
*  ` position `  should be use by using space - Don’t fill lines by spaces when  ` position[1] > 0 ` 

* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

guillaume@ubuntu:~/0x06$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/0x06$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x06-python-classes ` 
* File:  ` 6-square.py ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 4 advanced tasks now!](https://intranet.hbtn.io/projects/247/unlock_optionals) 

×#### Recommended Sandbox
[Running only]() 
### 1 image(1/5 Sandboxes spawned)
### Ubuntu 20.04
Basic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Holberton Foundations
SSHSFTP[Webterm](https://intranet.hbtn.io/user_containers/20136/webterm) 
[Restart]() 
[Destroy]() 
#### Credentials
Hostd0e3df2a9605.382951ab.hbtn-cod.ioUsernamed0e3df2a9605Passwordbec8653482c2d48c9d21#### Web access
[HTTPS](https://d0e3df2a9605.382951ab.hbtn-cod.io/) 
[HTTP](http://d0e3df2a9605.382951ab.hbtn-cod.io/) 
[3000](http://d0e3df2a9605.382951ab.hbtn-cod.io:3000/) 
[4000](http://d0e3df2a9605.382951ab.hbtn-cod.io:4000/) 
[5000](http://d0e3df2a9605.382951ab.hbtn-cod.io:5000/) 
[5001](http://d0e3df2a9605.382951ab.hbtn-cod.io:5001/) 
[8000](http://d0e3df2a9605.382951ab.hbtn-cod.io:8000/) 
[8080](http://d0e3df2a9605.382951ab.hbtn-cod.io:8080/) 
#### Port mapping
SSH49162HTTP49161HTTPS49160300049159MySQL49158400049157500049156500149155800049154808049153