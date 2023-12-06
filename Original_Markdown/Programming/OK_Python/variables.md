Global variables in Python.

Example:  

```python
x = "awesome"

def myfunc():
  print("Python is " + x) # Python is awesome

myfunc()
```

The global keyword can be used to change a global variable inside a function.  

```python
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) # Python is fantastic
```

The global keyword is used to create a global variable inside a function.  

```python
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) # Python is fantastic
```


