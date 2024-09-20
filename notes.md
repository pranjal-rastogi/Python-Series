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
