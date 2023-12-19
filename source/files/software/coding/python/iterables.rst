=========
Iterables
=========
Iterables are objects that can be iterated over, like lists, tuples, dictionaries, sets, strings, and generators.

List
====
List is a collection of items that can be of different types (heterogeneous).

.. code-block:: python

   my_list = [1, 2, 3, 4, 5]
   my_list = ["Hello", "World"]
   my_list = [1, "Hello", 3.4, True]

   # Accessing items
   print(my_list[0]) # 1

Featues:

- Lists are mutable, meaning that you can change their content after creation.
- Lists are ordered, meaning that the items have a defined order, and that order will not change.
- Lists allow duplicate values, meaning that you can have two items that are the same.

Tuple
=====
Tuple is a collection of items that can be of different types (heterogeneous).
    
.. code-block:: python

   my_tuple = (1, 2, 3, 4, 5)
   my_tuple = ("Hello", "World")
   my_tuple = (1, "Hello", 3.4, True)
  
   # Accessing items
   print(my_tuple[1]) # Hello
  
Featues:

- Tuples are **immutable**, meaning that you can't change their content after creation.
- Tuples are ordered, meaning that the items have a defined order, and that order will not change.
- Tuples allow duplicate values, meaning that you can have two items that are the same.

.. note::   
   Tuples are more memory efficient and faster (looking up values) than the lists. If you have data that shouldn't change,  
   you should choose tuple data type over lists


Dictionary
==========
Dictionary is a collection of items that can be of different types (heterogeneous).
Dictionary is a collection of key-value pairs.
Dictionaries are useful for fast lookups and retrieval of values based on keys.


.. code-block:: python

   my_dict = {
       "name": "John",
       "age": 36,
       "country": "Norway"
   }

   # Accessing items
   print(my_dict["name"]) # John

Array
=====
Array is a collection of items of the same type (homogeneous)  
Array is **faster than list**.  
Array must be declared before they can be used because they are not part of the standard Python.  

.. code-block:: python

   from array import array

   int_array = array('i', [1, 2, 3, 4, 5])
   gloat_array = array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
