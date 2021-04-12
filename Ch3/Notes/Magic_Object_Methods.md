# 3. Magic Object Methods
- A set of methods that python automatically associates with
every class definition
- Your classes can override these methods to customize a variety 
  of behaviour and make them act just like python's built-in classes
  
- We'll go over just a few
- Define how objects are represented as strings
- Control access to attribute values, both for setting and retrieving
- Add capabilities to classes to allow them to be used in expressions, such as testing for equality
- Make an object callable like a function

## String representation
- Refer to magicstr_start.py

## Equality and comparison
- Plain objects in python by default do not know how to compare themselves to each other, but we can teach them
to do so by using the equality and comparison magic methods
- Refer to magiceq_start.py

## Attribute access
- Pythons magic methods also gives you complete control over how objects attributes are accesed
- Your class can define methods that intercept the method anytime an attribute is set or retrieved
- Refer to magicattr_start.py