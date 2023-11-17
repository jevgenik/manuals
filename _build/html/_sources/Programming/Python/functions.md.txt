Examples of functions in Python

```python
def my_function():
    print("Hello World")

my_function()
```

```python
def my_function(name):
    print("Hello " + name)

my_function("John")
```

```python
def my_function(name = "John"):
    print("Hello " + name)

my_function()
```

The *args parameter allows you to write a function that can accept a varying number of 
individual positional arguments in each call. Your code packs all of these arguments into a tuple named args
Args is just a name. You can choose any name you want, but args is the convention.

```python
def my_function(*args):
    print("The youngest child is " + args[2]) # kids[2] is the third item in the tuple

my_function("Emil", "Tobias", "Linus")
```

```python
