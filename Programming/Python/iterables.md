# Iterables
are objects that can be iterated over, like lists, tuples, dictionaries, sets, strings, and generators.

## List
A list is a collection of items that can be of different types.
  
  ```python
  my_list = [1, 2, 3, 4, 5]
  my_list = ["Hello", "World"]
  my_list = [1, "Hello", 3.4, True]
  ```

Featues:
- Lists are mutable, meaning that you can change their content after creation.
- Lists are ordered, meaning that the items have a defined order, and that order will not change.
- Lists allow duplicate values, meaning that you can have two items that are the same.

## Tuple
A tuple is a collection of items that can be of different types.
    
    ```python
    my_tuple = (1, 2, 3, 4, 5)
    my_tuple = ("Hello", "World")
    my_tuple = (1, "Hello", 3.4, True)
    ```
Featues:
- Tuples are immutable, meaning that you can't change their content after creation.
- Tuples are ordered, meaning that the items have a defined order, and that order will not change.
- Tuples allow duplicate values, meaning that you can have two items that are the same.


> Tuples are more memory efficient than the lists. When it comes to the time efficiency, tuples have a slight advantage  
> over the lists especially when we consider lookup value. If you have data that shouldn't change,  
> you should choose tuple data type over lists