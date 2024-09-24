## 1. What is Python
Python is a high-level, interpreted programming language known for its simplicity and readability, making it popular for tasks like web development, data analysis, automation, and artificial intelligence.

## 2. Difference between Mutable and Immutable
- Mutable: Objects whose values can be changed after creation.
- Immutable: Objects whose values cannot be changed after creation.

## 3. Basic difference between list, tuple, set or dictionary
In Python, lists, tuples, dictionaries, and sets are all data structures, but they differ in how they store and manage data. 

A **list** is a mutable, ordered collection that allows duplicate values. You can modify, add, or remove items after the list is created. A **tuple** is similar to a list but is immutable, meaning its elements cannot be changed once it’s created, making it ideal for storing fixed data. Both lists and tuples maintain the order of elements.

On the other hand, a **dictionary** is a mutable collection of key-value pairs. Each key must be unique, and it allows you to retrieve values based on their corresponding keys rather than their position, making dictionaries suitable for structured data. Lastly, a **set** is an unordered collection of unique elements, meaning it automatically removes duplicates and does not allow indexing or slicing like lists or tuples. Unlike dictionaries, sets only store values, not key-value pairs. 

In summary, lists and tuples focus on ordered sequences, dictionaries store key-value pairs, and sets emphasize uniqueness.

## 4. why datatypes is called an object?
In Python, data types are called objects because everything in Python, including primitive data types like integers, strings, and even functions, is implemented as an object. Each object has attributes (data) and methods (functions) associated with it, and Python treats all data and entities uniformly as objects, following its object-oriented programming model.

## 5. Memory Managment in Python
In Python, memory management involves tracking and managing the allocation and deallocation of memory for objects.

Reference Counting: Python keeps track of how many references point to each object. When the reference count drops to zero, the memory for that object is freed.

Garbage Collection: Python uses a garbage collector to clean up objects that are no longer reachable, especially those involved in circular references.

```python
a = [1, 2, 3]  # 'a' references a list object
b = a          # 'b' also references the same list object

# Both 'a' and 'b' point to the same list
print(a is b)  # Output: True

# Modifying the list through 'a'
a.append(4)
print(b)       # Output: [1, 2, 3, 4], 'b' reflects the change

# When 'a' and 'b' go out of scope or are reassigned, the reference count drops.
```

## 6. "is" keyword in Python
 It checks whether two variables point to the same object in memory, not whether they have the same value.

## Object Types / Data types
- Number : 1234. 3.14, 3+4j, 0b111, Decimal(), Fraction
- String : 'spam', "Bob's"
- List : [1,2,3,4,5], ["pranjal","rastogi"], [1,2['a','b']]
- Tuple : (1, 'spam', 4, 'U')
- Dictionary : {'food': 'spam', 'taste': 'yum'}
- Set : set('abc'), {'a','b','c'}
- File : open('eggs.txt')
- Boolean : True, False
- None : None
- Functions, modules, classes
- Advance: Decoraters, Generators, Iterators, MetaProgramming 

## 7. Difference between repr(), str() and print()
1. repr() : Provides a string that is unambiguous and ideally suitable for debugging. It aims to give you a string that would recreate the object if passed back into Python.
Output: Usually, the result of repr() is more technical and often includes quotes around strings.

2. str() : Provides a readable and more human-friendly string representation of the object. It’s what you see when printing things for user-facing content.
Output: Less technical, focuses on clarity.

3. print() : Simply prints the result of str() to the console. It is used for displaying output to the user.
Output: Does not return anything; it just shows the string on the console.

```python

x = "Hello, World!"

# repr() example
print(repr(x))  # Output: "'Hello, World!'"

# str() example
print(str(x))  # Output: "Hello, World!"

# print() example (similar to str())
print(x)  # Output: Hello, World!

```
- repr(x) gives "'Hello, World!'", which includes quotes because it’s meant to represent the object precisely.
- str(x) just shows "Hello, World!" without extra details.
- print(x) behaves like str() and prints the result directly to the console.

In summary, repr() is for developers (debugging), str() is for users (readable output), and print() simply displays the result of str().

## 8. what is slicing dicing in python
- Slicing: Extracting a portion (or slice) of a sequence like a list, string, or tuple using a specific range of indices.
- Dicing: This term is often used to mean slicing with multiple dimensions (e.g., in a 2D array or matrix), but it’s not a formal Python term. Think of it as slicing in more complex data structures.

``` python
sequence[start:stop:step]
```

```python
# Slicing a list
my_list = [1, 2, 3, 4, 5, 6]

# Slice from index 1 to 4
print(my_list[1:4])  # Output: [2, 3, 4]

# Slice with step of 2
print(my_list[0:6:2])  # Output: [1, 3, 5]

```

## what is lamda function in python
A **lambda function** in Python is a small, anonymous function that can have any number of arguments but only one expression. It's often used when you need a simple function for a short period of time.

Here's an example:

```python
# Regular function
def add(x, y):
    return x + y

# Lambda function
add = lambda x, y: x + y
```

Both do the same thing, but the lambda function is written in a more compact way. It's mainly used for quick, throwaway functions inside other functions like `map()`, `filter()`, or `sorted()`.

## Explain *args and **kwargs in python
In Python:

- `*args` allows you to pass a variable number of **positional arguments** to a function. It collects the extra arguments as a tuple.

  Example:
  ```python
  def my_func(*args):
      for arg in args:
          print(arg)

  my_func(1, 2, 3)  # Output: 1 2 3
  ```

- `**kwargs` allows you to pass a variable number of **keyword arguments** (name=value pairs). It collects them as a dictionary.

  Example:
  ```python
  def my_func(**kwargs):
      for key, value in kwargs.items():
          print(f"{key} = {value}")

  my_func(a=1, b=2)  # Output: a = 1, b = 2
  ```

In short, `*args` is for passing many positional arguments, and `**kwargs` is for passing many keyword arguments.

## What is yield in python 
In Python, `yield` is used in a function to turn it into a **generator**. Instead of returning a value and ending the function, `yield` pauses the function, saves its state, and returns a value. The next time the generator is called, it resumes from where it left off.

This is useful when you want to produce a series of values lazily, without storing them all in memory at once.

Example:

```python
def count_up_to(n):
    for i in range(1, n+1):
        yield i

counter = count_up_to(3)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
```

The function `count_up_to` generates numbers one by one using `yield`.

## self and __init__ use in python

- `**self**` refers to the instance of the class. It allows you to access the attributes and methods of the class in the current object. It's used in instance methods to refer to the object being created or modified.

  Example:
  ```python
  class Car:
      def drive(self):
          print("Car is driving")
  ```

- `**__init__()**` is the **constructor method** that gets called automatically when an object is created. It's used to initialize the object's attributes.

  Example:
  ```python
  class Car:
      def __init__(self, color):
          self.color = color  # Set color attribute when object is created
  ```

In short, `self` refers to the object, and `__init__()` initializes the object’s attributes when it’s created.

## Behind the scene of loops in python
In Python, behind the scenes, loops like `for` and `while` work by **iterating over items** one by one.

- **For Loop:** When you use a `for` loop, Python looks for an object that can be **iterated** (like a list, tuple, or string). It fetches each item using an internal method called `__iter__()` and processes it one by one.
  
  Example:
  ```python
  for i in [1, 2, 3]:
      print(i)
  ```

- **While Loop:** In a `while` loop, Python keeps executing the code **as long as the condition is true**. It checks the condition before each iteration.

  Example:
  ```python
  i = 0
  while i < 3:
      print(i)
      i += 1
  ```

In simple terms, `for` loops iterate over items, and `while` loops repeat based on a condition, both ensuring that code runs multiple times efficiently.

## why we use iter() and next() in for loop 
In Python, `iter()` and `next()` are used to manually handle iteration, providing more control over the loop process. Here's why:

1. **`iter()`**: The `iter()` function converts an iterable (like a list or tuple) into an **iterator**. An iterator is an object that remembers its position during iteration.

   Example:
   ```python
   my_list = [1, 2, 3]
   iterator = iter(my_list)
   ```

2. **`next()`**: The `next()` function **fetches the next item** from an iterator. Each time you call `next()`, it moves to the next element until there are no more items left, at which point it raises a `StopIteration` exception.

   Example:
   ```python
   print(next(iterator))  # Output: 1
   print(next(iterator))  # Output: 2
   ```

**In a `for` loop**, Python **automatically** uses `iter()` and `next()` behind the scenes to go through each item in the iterable. You don't usually see these functions, but they allow Python to loop over items efficiently.

In short, `iter()` initializes the iterator, and `next()` fetches items from it. The `for` loop handles this for you automatically.

## What is scope and closure in python
In Python:

- **Scope** refers to the region where a variable can be accessed. Python has four types of scope:
  1. **Local**: Variables defined inside a function.
  2. **Enclosing**: Variables in the outer function when dealing with nested functions.
  3. **Global**: Variables defined at the top level of the script or module.
  4. **Built-in**: Predefined names like `print()`, `len()`, etc.

  Example:
  ```python
  x = 10  # Global scope

  def func():
      y = 5  # Local scope
  ```

- **Closure** occurs when a **nested function remembers** the variables from its enclosing function, even after the outer function has finished executing. This allows the inner function to access and use the variables from its outer function's scope.

  Example:
  ```python
  def outer():
      x = 10
      def inner():
          print(x)  # Closure: inner remembers x from outer
      return inner

  my_func = outer()
  my_func()  # Output: 10
  ```

In short, **scope** defines where a variable is accessible, and **closure** allows a nested function to "remember" variables from its parent function even after the parent has finished.

## What is static method
A static method is a method that can be called directly from a class without creating an instance of that class. Static methods are useful for performing general operations that don't depend on a specific object's state or behavior.

## What is use isinstance() function
The isinstance() function returns True if the specified object is of the specified type, otherwise False. 

