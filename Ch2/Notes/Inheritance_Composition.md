#2. Inheritance and Composition
- Inheritance is a core concept of OOP in Python
    - Defines a way for a given class to inherit att and methods from one or more base classes
    - Makes it easy to centralize common functionality and data in one plaace instead of duplicated
    
## Understanding Inheritance
- Refer to inheritance_start.py

##Abstract base classes
- Common design pattern in programming is providing a base class that defines a template  for other classes to inherit 
  from, but with some twists
- Don't want consumers of your base class to be able to create instances of the base class itself, because its just 
  intended to be a blueprint or idea
- Want subclasses to provide concrete implementations of this idea
- Want to enforce the constraint that there are certain methods in the base class that sub classes have to implement
- Refer to abstract_start.py
