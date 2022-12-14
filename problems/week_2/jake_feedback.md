Here was your first solution:

```python
def add_zeroes(zeroes, string_input):
    zero_string = ""
    while zeroes != 0:
        zero_string += str(0)
        zeroes -= 1
        #print(zeroes)
    return zero_string + string_input
```

So first off, what I'd like you to do is use type hints and doc strings in all your functions. 

If I were to add these to your function, it would look like this:

```python
def add_zeroes(zeroes: int, string_input: str) -> str:
    """Adds a specified number of 0's to the beginning of a string."""

    ...
```

Type hints are used next to parameters in function definitions. Next to each parameter, you use a colon `:` and specify the _type_ that the parameter will be, whether that be an integer, string, list, etc.  

The doc string is just the string just under the function definition.  Giving people an idea of what the function does is actually really important.  In code review, we are all aware of what the coding problems were, but when somebody is reading your code and they have no idea what you are doing, type hints and doc strings help them a lot to decipher your code.

Now, as for the logic of your function, you did a great job of making it work with a while-loop.  

One little thing you could do is instead of converting the integer `0` to a string before adding it to the `zero_string` variable like this: `zero_string += str(0)`, is you could literally just add a string that contains a 0: `zero_string += '0'`.

Also, we could avoid a loop altogether by multiplying a string by an integer.  Anytime we multiply an integer N by a string, it produces a new string that contains the original string N number of times.  For example:

`4 * '0'` would equate to a string containing 4 zeroes: `'0000'`

Knowing this, we could create our zeroes string pretty easily:

```python
zero_string = zeroes * '0'
```

In the function it would look like this:


```python
def add_zeroes(zeroes: int, string_input: str) -> str:
    """Adds a specified number of 0's to the beginning of a string."""

    zero_string = zeroes * '0'

    return zero_string + string_input
```

You could even shorten this to one line because math's order of operations takes effect:

```python
def add_zeroes(zeroes: int, string_input: str) -> str:
    """Adds a specified number of 0's to the beginning of a string."""

    return zeroes * '0' + string_input
```



Now for your second solution:

```python
def find_average(input):
    quan = 0
    total = 0
    for i in input:
        quan += 1
        total += int(i)
    average = total / quan
    return int(average)
```

After adding type hints and a doc-string, I got this:

```python
def find_average(input: list) -> int:
    """Finds the average of a list of numbers.  Rounds up to the nearest whole number."""

    quan = 0
    total = 0
    for i in input:
        quan += 1
        total += int(i)
    average = total / quan
    return int(average)
```

One thing we also want to do is be very explicit with our parameter and variable names.  For this example, I made some changes:

```python
def find_average(numbers: list) -> int:
    """Finds the average of a list of numbers.  Rounds up to the nearest whole number."""

    quantity = 0
    total = 0
    for number in numbers:
        quantity += 1
        total += int(number)
    average = total / quantity

    return int(average)
```

Now lets talk about the logic.  It was smart how you updated both the quantity and total variables during your for-loop.  Luckily though, we use a some built-in functions so we don't need a loop at all.

For example, the built-in `sum()` function can take in a list of numbers and returns the sum.  

Also, the built-in `len()` function can take in a list and give you the length of that list.  

So, if we were to implement this in your solution, it would look like this:

```python
def find_average(numbers: list) -> int:
    """Finds the average of a list of numbers.  Rounds up to the nearest whole number."""

    quantity = len(numbers)
    total = sum(numbers)

    average = total / quantity

    return int(average)
```

So, one last note for this solution is that we still aren't rounding up a number.  See if you can take this solution and figure out how to round up.


<br/>

Now, here is your last solution:

```python
def create_list(user_input):
    counter = 0
    list_output = []
    while counter != user_input:
        counter += 1
        list_output.append(2**counter)
        print(counter)
    return list_output
```

After adding type hints and a doc string this is what I have:

```python
def power_of_twos(limit: int) -> list:
    """Creates a list of the powers of 2 up to a given degree."""

    counter = 0
    list_output = []
    while counter != limit:
        counter += 1
        list_output.append(2**counter)
        print(counter)
        
    return list_output
```

So, now for the logic.  You did a good job using a while-loop, although I'd generally recommend avoiding while-loops.  In other coding languages they might be more common, but in Python we actually have some better mechanisms we can use.  

Additionally, we really don't need to use a counter in Python.  

In this particular exercise, we really need to loop through all the numbers, starting from the number `1` up to the limit given to us.  We can easily create a range of numbers using the `range()` function.  

For example, this would loop through the numbers 1, 2, 3, 4, and 5:

```python
for number in range(1, 6):
    print(number)
```

`number` is the loop variable that we've defined, and we are looping through a range of numbers.  Notice that we passed out starting number `1`, but the ending number `6` is one higher that what we wanted.  This is because a range object will include every number _up to_ the given last number.  That's why `range(1, 6)` actually produces a range from 1 to 5.

Anyway, if we were to use this in our function, we could avoid a counter altogether:

```python
def power_of_twos(limit: int) -> list:
    """Creates a list of the powers of 2 up to a given degree."""


    list_output = []

    for number in range(1, limit + 1):

        list_output.append(2 ** number)
        print(number)

    return list_output
```

Lastly, and this is a bit more advanced, we could put all of this code into a _list comprehension_.  The code in this example is so common that the Python developers created a shortcut called a list comprehension.  We can take this same idea, where we loop through something and add some value to a list on each iteration of the loop, and put it onto one line. 

If we used a list comprehension in this example, it would look like this:

```python
def power_of_twos(limit: int) -> list:
    """Creates a list of the powers of 2 up to a given degree."""


    list_output = [ number ** 2 for number in range(1, limit + 1) ]

    return list_output
```

Again, list comprehensions are an intermediate topic, but try and notice that I almost just took the code from the previous example and moved it around. Some people, even people in the unit, might warn against using comprehensions because they are confusing. 

The fact is though, you **should** be using them.
