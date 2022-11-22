### Be a cliche (Difficulty 1 out of 10)

Print `Hello World!`.

Example solutions:

```python
# Solution 1
print('Hello World!')

# Solution 2
my_string = 'Hello World'

print(my_string)
```



### Create your first function (Difficulty 3 out of 5)

Create a function that prints a greeting of your choice and execute it.

Example solutions:

```python
def greeting() -> str:
    """Prints a generic greeting."""

    print('Good morning!  Welcome to code review.')

greeting()
```

### Print a greeting for any name (Difficulty 4 out of 10)

Create a function that can take a first name as input and print a greeting that includes the name within it.

Here are some examples:

| Name | Output |
| --- | --- |
| `'Alice'` | `'Good morning, Alice!'` |
| `'Bob'` | `'Good morning, Bob!'` |
| `'John'` | `'Good morning, John!'` |

Example Solution:

```python
# Solution 1
def personal_greeting(name: str) -> str:
    """Prints a greeting to a specific name."""

    greeting = 'Good morning, ' + name + '!'
    print(greeting)

# Solution 2
def personal_greeting(name: str) -> str:
    """Prints a greeting to a specific name."""

    greeting = 'Good morning, {}!'.format(name)
    print(greeting)

# Solution 3
def personal_greeting(name: str) -> str:
    """Prints a greeting to a specific name."""

    greeting = f'Good morning, {name}!'
    print(greeting)
```


### Space shuttle count down (Difficulty 5 out of 10)

Create a function that, when executed, prints out a space shuttle countdown.  Your function should start at 10, and print one number in the countdown once every second.  Instead of printing out 0, your function should print `'Lift off!'` as the final message.

Example solutions:

```python
from time import sleep

def countdown():
    for num in range(10, 0, -1):
        sleep(1)
        print(f'{num}!')
    sleep(1)
    print('Lift off!')

countdown()
```
