Here's one of your solutions:

```python
def numbers(list):

    highest_3 = list
    highest_3.sort()
    highest_3.reverse()
    print(highest_3[0:3])
    print()
```

Don't forget to start using type hints and doc strings.  It really does help other people when they're reading your code.
Also, we have to avoid using built-in keywords as parameters or variable names.  In this case, your parameter is just called `list`, which in Python actually references the built-in list class.  I'd recommend using a parameter that shows what is in the list.  Something like `nums` would suffice.  If we applied all of this to your function, it would look something like this:

```python
def sort_numbers(nums: list) -> list:
    """Returns a list containing the three highest numbers of another list in descending order."""
```

As for the logic, I liked what you did.  It's clean, easy to read, and you used built-in functions which are always more resource efficient than loops.  

One thing you could've done is sorted the list and reversed it in one step: `highest_3.sort(reverse=True)`

--- 

Here's another solution:

```python
def old_fashion_text (string) :

    keypad = {
    '1' : ['.', ',', '?', '!', ':'],
    '2' : ['A', 'B', 'C'],
    '3' : ['D', 'E', 'F'],
    '4' : ['G', 'H', 'I'],
    '5' : ['J', 'K', 'L'],
    '6' : ['M', 'N', 'O'],
    '7' : ['P', 'Q', 'R', 'S'],
    '8' : ['T', 'U', 'V'],
    '9' : ['W', 'X', 'Y', 'Z'],
    '0' : [' ']
    }

    txt = string.upper()

    result = ""
    keys = list(keypad.items())

    for i in range(len(txt)):
        for j in range(len(keys)):
            for k in range(len(keys[j][1])):
                if txt[i] == keys[j][1][k]:
                    result+=((k+1)*keys[j][0])
                    result += '-'

    print(result)
```

In code review I mentioned how by looping through the `range(len(some_object))` we can essentially loop through the indices of an object, but generally in Python we can just loop through the items in the object itself.

For example, instead of looping through the indices of the inputted text:

`for i in range(len(txt)):`

we could just loop through each character:

`for char in txt:`

This new initial for-loop would require you to change the rest of the code, but this is much more readable.  Obviously this is some code you found online, but I just wanted to mention this regardless.

Overall, great job finding solutions though.  It doesn't matter if you have to google something.  The best thing you can do is just take the time to analyze the code and figure out how it actually works.
