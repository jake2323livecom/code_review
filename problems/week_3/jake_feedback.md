Here's one of your solutions:

```python
def my_function(numbers):
    top_three = []
    while len(top_three) < 3:
        top_three.append(max(numbers))
        numbers.remove(max(numbers))
    return(top_three)
```

One thing I'll harp on one and one time only is just using type hints and a doc string for your function.  If we did this, the top of your function would look like this:

```python
def my_function(numbers: list[int]):
    """Returns the highest three numbers in a list in decending order."""
```

As for the logic itself, I like how you did it.  I'd challenge you to see if you could solve it without a loop at all.  Unfortunately, since Python is interpreted, it's actually really slow compared to compiled languages, especially when using loops.  Most people don't actually know, however, that the built-in functions are actually written in C, which is a compiled language.  Therefore, one thing you can do is avoid loops and use built-in functions wherever possible. 

This is totally not required, but it is one thing you can do to make your code stand out.

---

Here's one of your other solutions:

```python
def text(phrase):
    ls = []
    for char in phrase:
        for key,value in keyboard.items():
            for letter in value:
                if char == letter:
                    ls.append(key * int(value.index(letter) + 1))
    return(ls)
```

You saw this in code review, but we can get rid of a couple lines of code here.  Instead of looping through each character mapped to a given integer: `for letter in value:`, we can just use a built-in comparison to check and see if the character is in the entire string: `if letter in value:`.  If we use that instead, we no longer need the line beneath it: `if char == letter:`. 

Besides that, you did it exactly like I did.

---

Here's your last solution:

```python
import calendar
cal= calendar.Calendar()

def friday_13(year):
    months = list(range(1,13))
    date = []
    for month in months:
        for x in cal.itermonthdays4(year, month):
            if x[2] == 13 and x[3] == 4:
                date.append(calendar.month_name[month])
    return(date)
```

Nothing wrong with the logic here so good job on this one.  

One thing I'll say (and this applies to some of your other stuff too), is that in the return statement, we don't need parenthesis: `return(date)`.  We can just say `return date`.

Lastly, we don't actually have to turn the range into a list.  We can loop through a range the same way we would loop through a list of numbers.  

Good job!