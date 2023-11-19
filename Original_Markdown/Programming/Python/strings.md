my_string = "Hello, world!"

- `str()` is a built-in function used to convert an object into a string.
          e.g str(2) will return "2"



## List comprehension
List comprehension allows you to generate a new list by applying an expression to each item in an existing  
iterable (e.g., a list, tuple, or range) and optionally filtering the items based on a condition.  
It offers a shorter syntax when you want to create a new list based on the values of an existing list

`new_list = [expression for item in iterable if condition]`
- expression: This is the expression that is evaluated for each item in the iterable.  
              It generates the values that will be included in the new list.
- item: This is a variable that takes on each value in the iterable one at a time.
- iterable: This is the collection you want to iterate over (e.g., a list, tuple, or range).
- condition (optional): This is an optional filter that specifies whether the item should be included in the new list.  
  If the condition is omitted, all items from the iterable will be included in the new list.

Examples: 

squared_numbers = [x ** 2 for x in range(10)]  
Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
even_numbers = [x for x in numbers if x % 2 == 0]  
Result: [2, 4, 6, 8, 10]  


NB! Strings are iterable, so you can use list comprehension to generate a list of characters from a string.  
Example:  
my_string = "Hello, world!"  
characters = [x for x in my_string]  
Result: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!']  