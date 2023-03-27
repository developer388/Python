""" 
Learning Python

1. Data types:

1. int      int(3.5)t  int('3')f
2. float    float(7)t  float('3.4')f
3. bool     bool(1)t   bool(0)f bool([1,2,3])t bool([])f
4. str      str(7)     str(4.5)
5. None     
6. list
7. dict
9. tuple
10. set

2. Operators

Arithmetic operators
+ addition
- subtraction
* multiplication
/ divison
% modulus
** exponential (x to the power y)
// floor division


Assignment operators
=    equal to
+=   x = x + y
-=   x = x - y
*=   x = x * y

Comparison operators
==   equal to
!=   not equal to
>    greater than
<    less than
>=   greater than or equal to
<=   less than or equal to

Logical operators
and
or
not

Identity operators
is       check if object reference is same
is not   check if obect reference is not same

Membership operators
in       check if x is present in a collection data type
not in   check if x is not present in a collection data type



Internal Functions
type(variable_name) : Returns data type of a variable
len(variable_name)  : Returns len of str, list

"""


""" 
3. str data type  
    indexing
    slicing
    concatenation
    immutable
    .format()
    f string
    multi line string
"""
name = "Nikhil Gautam"

print('name[0:6]   = ', name[0:6])
print('name[:6]    = ',  name[:6])
print('name[3:6]   = ', name[3:6])
print('name[6:]    = ', name[6:])
print('name[:]     = ',  name[:])
print('name[-1]    = ', name[-1])
print('name[-1,-3] = ', name[-4:-1])

# str concatenation

first_name = 'Nikhil'
last_name = 'Gautam'
full_name = first_name + last_name 

print('full_name = ', full_name)

# str methods
animal = 'elephant'
print('str is immutable = ', animal.capitalize(),animal.upper(), animal)
print('find index of a substring = ', animal.find('e'), animal.index('e'))
print('join() = ',   ','.join(['n','i','k','h','i','l']))


#str formating 
print("Hi {}".format("Nikhil"))
print("Hello {0}, Is {1} your friend?".format('Nikhil', 'Mayank'))
print("Hello {1}, Is {0} your friend?".format('Nikhil', 'Mayank'))

person = {
    "name": "nikhil",
    "dob" : "06-01-1993"
}

print("Name: {name} DOB: {dob}".format(name=person['name'], dob=person['dob']))
print("Name: {name} DOB: {dob}".format(**person))

#f str is fastest, expressions are evaluated at runtime
print(f"Name: {person['name']} DOB: {person['dob']}")
print(f"5*100 = {5*100}")

multi_line_string = (
    f"Hi {full_name}. "
    f"Your dob is {person['dob']}. "
    f"Your sirname is {last_name}."
)

print(multi_line_string)

multi_line_string =  f"Hi {full_name}. "\
                    f"Your dob is {person['dob']}. "\
                    f"Your sirname is {last_name}."

print(multi_line_string)

""" 
4. Python Collections  
    list    ordered, indexed and changeable, allows duplicate members
    tuple   ordered, indexed and unchangeable, allows duplicate members
    dict    ordered (from v3.7), key based index and changeable, no duplicate members
    set     unordered, unindexed, no duplicate members

   
   list
   
    Lists are ordered.
    Lists can contain any arbitrary objects. 
    List elements can be accessed by index.
    Lists can be nested to arbitrary depth.
    Lists are mutable.
    Lists are dynamic.
"""

# internal functions
numbers = [8,6,2,1,7,3,0]
print(len(numbers), max(numbers), min(numbers))

# use of + operator
numbers = numbers + [11,12,13,14]
print(numbers)

# use of * operator
numbers = numbers * 2
print(numbers)

# use of in operator
print(8 in numbers)

# update multiple list values
numbers[0:4] = [0,1,2,3,4]
print(numbers)

# delete multiple list values
numbers [0:4] = []
print(numbers)

# delete by index
del numbers[0]
print(numbers)

# delete multiple list values by del operator
del numbers[0:2]
print(numbers)


# append()  add an item to the end of the list
numbers = [1,2,3]
numbers.append(4)
print(numbers)

# extend() extends a list with iterable
numbers.extend([5,6,7])
print(numbers)


# insert(index, value) insert a new value at sepecified index
numbers.insert(0, -1)
print(numbers)


# remove() find and removes an item from the lis
#          if item is not present, exception is raised
numbers.remove(-1)
print(numbers)

# pop(index=) remove an item from the specified index
#             returns the item removed
#             default value for index is -1, last item of list
print(numbers.pop())

"""
  4.2 
  
  tuple
  
  Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
  
  Tuples are immutable, assigning a value results in exception
  
  Program execution is faster when manipulating a tuple than it is for the equivalent list. (This is probably not going to be noticeable when the list or tuple is small.

  Sometimes you don’t want data to be modified. If the values in the collection are meant to remain constant for the life of the program, using a tuple instead of a list guards against accidental modification

  There is another Python data type that you will encounter shortly called a dictionary, which requires as one of its components a value that is of an immutable type. A tuple can be used for this purpose, whereas a list can’t be.
"""

t = (1,2,3)

# unpacking
a, b, c = t
print(a,b,c)

# packing
t = c, b, a
print(t)

# swap
a = 10
b = 40

a, b = b, a
print(a, b)


"""
  4.3
  
  dict
  
"""

# defining dictionary
employee = {
    "code" : 5504,
    "name" : "Nikhil Gautam"
}

employee2 = dict([
        ('code', 5505),
        ('name', 'Mayank')
    ])
    
employee3 = dict(code=5506, name='Vinay')

print(employee)
print(employee2)
print(employee3)


# accessing keys in dictionary
# bracket method, raises exception if a key is not present
print(employee['name'])

# buit in immutable types can be used as dictionary key
d = {int: 1, float: 2, bool: 3}
print(d)

# tuple can also be used since its immutable
d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}

# list and dict cannot be used as a dict key because they are mutable

# hash() function returns the hash value for an object 
print(hash('Nikhil'))

# in and not in operator can be used to check the existence of keys
print('name' in employee)

# Built in functions
# clear() empties a dict
person.clear()
print(person)

# get(key, default) returns none if key doesn't exists
#                    returns defult value if key doesn't exists
print(employee.get('name'))
print(employee.get('age', 0)) 

# items() returns a list of tuples containing the key-value pairs
print(employee.items())

# keys() returns a list of all keys
print(employee.keys())

# values() returns a list of all values
print(employee.values())


# pop(key, default) Removes a key from a dictionary, if it is present, and returns its value.
#                   default value is returned if key doesn't exists

print(employee.pop('name'))
print(employee)

employee['age'] = 19

# popitem() Removes the last added key-value pair from a dictionary
#           Returns key value pair as tuple

print(employee.popitem())


# update() Merges a dictionary with another dictionary or with an iterable of key-value pairs.

employee.update({'department': 'Technology', 'age': 20})
print(employee)



"""
  4.4
  
  set
     unordered collection of unique elements
     sets are mutable
     elements of a set are immutable
     sets are created using {} with comma seperated values
     set() constructor can create set from iterables by removing duplicates
    
     in operator can be used to check existence of a element 
    
    .clear() empities a set
    .add()   add a item to set, doest return error if value is duplicate
    .update() add multiple values to set
    .remove() removes an element, returns error if value doest exists
    .discard() removes an element, doesn't return error
    .copy() creates shallow copy
    .pop() removes and returns the element randomly
    
    .union() returns new set containing all elements that are in either set
    .intersection() return a new set containing all elements that are in both sets
    .symmetric_difference() returns a new set containtingall that are exactly in one of the set
    .isubset() to check if all elemets of a set are in another set
    .superset() to check if a is superset of b
    .isdisjoint() to check if two sets have no member in common
    
    
"""
"""
  5. Condtional evaluation
  if else

      if <condition> :
            <statement>
      else :
            <statement>
            
  else if
  
        if <condition> :
            <statement>
        elif <condition> :
            <statement>
        else :
            <statement>
  empty if
        if <condition> :
            pass
            
  teneary if else
 
  variable = <true statement> if <expression> else <false statement>
        
"""

isActive = True

if isActive == True:
    print('Employee is active')
else:
    print('Employee is in active')
    
isActive = None

if isActive == True:
    print('Employee is active')
elif isActive == False:
    print('Employee is inactive')
else:
    print('Employee status not found')
    
isActive = True if full_name == 'NikhilGautam' else False
print(isActive)


"""
  6. Loops
  
  while loop                indefinite iteration
  
  while <condition> :
        <statement1>
        <statement2>
        <statement3>
        if <condition>:
            continue
        
        if <condition>:
            break
        
        
  else:
        <statement4>

 else block is optional and is executed when loop is ended
"""
counter = 0

while counter<10:
    print('counter={}'.format(counter))
    counter+=1
    
    if counter == 5:
        break
    
else:
    print("while loop is finished")


"""
 
 for loop                   definite iteration
 
 for <var> in <iterable>:
    <statement>
 else:
    <statement>
    
 iterable means an object can be used in iteration

 if an object is iterable, it can be passed to the built-in Python function iter(), which returns something called an iterator

 str, list, tuple, dict, set, and frozenset are iterables

 internal next(iterable) function can be used to iterate over iterables
 
 optional else statement executes when for loop is completed
 optional else statement is not executed if for loop is terminated using break statement

"""

# list
animals = ['Dog', 'Cat', 'Elephant', 'Monkey']

for animal in animals:
    print(animal)

# dict
dog = {
    "species": "mamal",
    "leg_count": 4,
    "age": 20,
    "isPet": True
}

for key in dog:
    print(key)

# .items() returns a tuple of key-value pair
for key, value in dog.items():
    print(key, value)
    
# list of tuple
t = [(1,1,1),(2,2,2)]
for a,b,c in t:
    print(a,b,c)

"""
   range(start, end, increment_by)
   
   range() returns an object of class range, not a list or tuple of the values. Because a range object is an iterable, you can obtain the values by iterating over them with a for loop:


"""

for i in range(5):
    print(i)

for i in range(0,20,2):
    print(i)


"""
   Function

   def function_name(parameter1, parameter2):
        <statement1>
        <statement2>
        return result
    
    Positional arguments    
        sayhello('Nikhil', 'Gautam)  Positional arguments must agree in order and number with the parameters declared in the function definition.
    
    Keyword arguments
    sayhello(last_name='Gautam', first_name='Nikhil') Keyword arguments must agree with declared parameters in number, but they may be specified in arbitrary order.
    
    Default parameters
    sayhello(first_name='un named'):   Default parameters allow some arguments to be omitted when the function is called.
    
   
    Call by value   
    Passing an immutable object, like an int, str, tuple, or frozenset, to a Python function acts like pass-by-value. The function can’t modify the object in the calling environment.

    Call by reference
    Passing a mutable object such as a list, dict, or set acts somewhat—but not exactly—like pass-by-reference. The function can’t reassign the object wholesale, but it can change items in place within the object, and these changes will be reflected in the calling environment.    
    
    
    Variable-Length Positional Argument *
    
    Tuple packing can be used:
    When a parameter name in a Python function definition is preceded by an asterisk (*), it indicates argument tuple packing. Any corresponding arguments in the function call are packed into a tuple that the function can refer to by the given parameter name. 
    
    Variable-Length Keyword Argument **
    
    Double asterisk (**) can be used with Python function parameters and arguments to specify dictionary packing and unpacking
    
    
    Docstring
    
    When the first statement in the body of a Python function is a string literal, it’s known as the function’s docstring. A docstring is used to supply documentation for a function. It can contain the function’s purpose, what arguments it takes, information about return values, or any other information you think would be useful.
    
    In the interactive Python interpreter, you can type help(<function_name>) to display the docstring for <function_name>
    
    Function Annotations
    As of version 3.0, Python provides an additional feature for documenting a function called a function annotation. Annotations provide a way to attach metadata to a function’s parameters and return value.
    
    
    Lambda function
    
    lambda arg: expression
    lambda x: x+1
    (lambda x: x+1)(arg)
"""

# Variable-Length Argument using tuple packing
t = (1,2,3,4,5,6,7,8,9)

def sum(*arg):
    result = 0
    for i in arg:
        result+= i
    return result

print('sum = ',sum(5,10,15,20,15,30))

# pass tuple with * for tuple unpacking
print('sum = ',sum(*t))

# Variable-Length Keyword Argument with dict

def employee_info(**arg):
    for key, value in arg.items():
        print(key, value)
    return arg.items()

print(employee_info(name="Nikhil", location="Gurgaon"))
print(employee_info(**dog))



# Docstring

def avg(*args):
     """Returns the average of a list of numeric values."""
     return sum(args) / len(args)

print(avg.__doc__)
print(help(avg))

# Funtion Annotation

def f(a: 'first value', b: 'second value') -> 'returns sum':
    pass

print(f.__annotations__)

inc = lambda a: a+1

print('inc() = ', inc(2))

print( (lambda a: a+1) (2) )

"""
 Namespaces and Scope
 
 A namespace is a collection of currently defined symbolic names along with information about the object that each name references. You can think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves. Each key-value pair maps a name to its corresponding object.
 
 In a Python program, there are four types of namespaces:

    1.Built-In
    2.Global
    3.Enclosing
    4.Local


The Built-In Namespace
    The built-in namespace contains the names of all of Python’s built-in objects. These are available at all times when Python is running. You can list the objects in the built-in namespace with the following command:
    dir(__builtins__)
    The Python interpreter creates the built-in namespace when it starts up. This namespace remains in existence until the interpreter terminates.    

The Global Namespace
    The global namespace contains any names defined at the level of the main program. Python creates the global namespace when the main program body starts, and it remains in existence until the interpreter terminates.
    The interpreter also creates a global namespace for any module that your program loads with the import statement. 

The Local and Enclosing Namespaces
    The interpreter creates a new namespace whenever a function executes. That namespace is local to the function and remains in existence until the function terminates.


Variable Scope

Suppose you refer to the name x in your code, and x exists in several namespaces. How does Python know which one you mean?
The answer lies in the concept of scope. The scope of a name is the region of a program in which that name has meaning. The interpreter determines this at runtime based on where the name definition occurs and where in the code the name is referenced

To return to the above question, if your code refers to the name x, then Python searches for x in the following namespaces in the order shown:

1. Local: If you refer to x inside a function, then the interpreter first searches for it in the innermost scope that’s local to that function.

2. Enclosing: If x isn’t in the local scope but appears in a function that resides inside another function, then the interpreter searches in the enclosing function’s scope.

3. Global: If neither of the above searches is fruitful, then the interpreter looks in the global scope next.

4. Built-in: If it can’t find x anywhere else, then the interpreter tries the built-in scope.


Python Namespace Dictionaries

globals() function
The built-in function globals() returns a reference to the current global namespace dictionary. You can use it to access the objects in the global namespace

locals() function
Python also provides a corresponding built-in function called locals(). It’s similar to globals() but accesses objects in the local namespace instead

 A Subtle Difference Between globals() and locals()
 globals() returns an actual reference to the dictionary that contains the global namespace. That means if you call globals(), save the return value, and subsequently define additional variables, then those new variables will show up in the dictionary that the saved return value points to
 locals(), on the other hand, returns a dictionary that is a current copy of the local namespace, not a reference to it. Further additions to the local namespace won’t affect a previous return value from locals() until you call it again. Also, you can’t modify objects in the actual local namespace using the return value from locals()



The global Declaration
What if you really do need to modify a value in the global scope from within f()? This is possible in Python using the global declaration


"""

# access global variable from function

max_limit = 30

def updateLimit(limit):
    global max_limit
    max_limit = limit

updateLimit(40)
print('maxLimit=',max_limit)


"""
nonlocal Declaration

nonlocal is used for enclosing scope, global keyword cannot be used for enclosing scopes


"""
# nonlocal is used for enclosing scope

def outer():
    x = 20

    def inner():
         nonlocal x
         x = 40

    inner()
    print('outer x = ', x)

outer()

"""
   Exception Handling
   
   There can be two type of errors in a python program
   
   1. Syntax Error : compile time error
   2. Exception : run time error 
   
   keywords
     raise     manually throw an error
     assert    raise assertion exception when condition is false
     try       all statements are executed until an exception is encountered
     except    used to catch and handle the exception(s) that are encountered in the try clause (pass statement can be used)
     else      lets you code sections that should run only when no exceptions are encountered in the try clause
     finally   enables you to execute sections of code that should always run, with or without any previously encountered exceptions
     
     program halts when an unhandled exception occurs in code execution
     

"""


# throw

x = 10
if x > 5:
    pass
    #raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# assert
#assert (False), 'Assertion Exception'

# try-catch else finally
try:
    if x < 5:
        raise Exception('X should be less than 5')
except Exception as e:
    print('Error:', e)
else:
    print('No error occured')
finally:
    print('release used resources')



"""
  Class
  
  Define a class
  
  class <class_name>:
      <statement1>
      <statement2>
  
  Constructor
    __init__() function is used to define a constructor in class
    First paramenter is always self
  
  class Dog:
     def __init__():
          <statement1>
  
  Instance Attributes
     variables defined inside __init__() with self are instance attribues
     
  Class Attribues
     variables defined outside __init__() are class attributes
     changing the value of a class attribute with an object reference turns class attribute into instnace attribute
     
  Instance Method
     Instance methods are functions that are defined inside a class and can only be called from an instance of that class.
     First paramenter is always self
     
  Inheritance
  class child_class_name (parent_class_name):
  
  Method Overiding
  To override a method defined on the parent class, you define a method with the same name
  
  Access Parent Class Members using super()
  You can access the parent class from inside a method of a child class by using super()
  
  isinstance(reference_variable_name, class_name) function can be used to check if a reference belongs to a class
  
"""

# Class

class Animal:
    planet='Earth'          # class attribute
    def __init__(self, name, species):
        self.name = name    # instance attribute
        self.species = species
        
    def info(self):
        return self.name
    
        
dog = Animal("Dog","Mammal")
print(dog, dog.info())


class Monkey(Animal):
    def info(self):
        return self.name, self.species
    
    def old_info(self):
        return super().info()

d = Monkey("Monkey", "Mamal")
print(d, d.info(), d.planet, isinstance(d, Animal), d.old_info())


