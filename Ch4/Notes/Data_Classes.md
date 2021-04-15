# 4. Data Classes

## Defining a data class
- Main purpose of using classes is to contain and represent data
- Our code creates classes (such as Book class in previous modules)
    - Then uses the init function to store values on the instance of the class
- If this is a common pattern, why doesn't Python automate this? Why do I have to explicitly
store each argument on the object by setting attributes on the self parameter
    - Starting in Python 3.7 you don't need to anymore!
    - New feature called the Data Class, which helps in the automation and managing
    of classes that mostly exist just to hold data
    - Documentation: https://docs.python.org/3/library/dataclasses.html
- Refer to dataclass_start.py

## Using post initialization
- How to perform additional object initialization if the dataclass automatically writes the init 
function for you
  - For example we way want to create attributes on our Book class that depend on the values 
      of other attributes, but we can't write init because dataclass already does that
  - The dataclass decorator provides a function called __post_init__
- Refer to postinit_start.py

## Using default views
- Dataclasses provide abil to define default values for their attributes subject to some rules
- Refer to datadefault_start.py

## Immutable data classes
- Occasionally you want to create classes whose data can't be changed (immutable)
- Python dataclasses make this possible by specifying an argument to the dataclass decorator
- Refer to immutable_start.py

