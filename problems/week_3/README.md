### Find an easter egg (Difficulty 2 out of 10)

Tim Peters, a contributor to the styling standards of Python, created a list of coding principles called the 'Zen of Python'.  You can import and print these principles using a built-in module.

Do some googling and figure out how to import these principles. 

###  Find the 3 highest numbers (Difficulty 3 out of 10)

Create a function to find the 3 largest numbers in a list.

Your function should take a list of numbers as input and return the three highest numbers in _descending_ order.


Examples:

| Input | Output |
| --- | --- | 
| `[1, 2, 3, 4, 5]` | `[5, 4, 3]` |
| `[12, 29, 48, 32, 1]` | `[48, 32, 29]` |
| `[98, 38, 29, 3]` | `[98, 38, 29]` |

### Add a number to its reverse (Difficulty 4 out of 10)

Create a function to reverse the digits of a given number and add it to the original.

Examples:

| Input | Logic | Output |
| --- | --- | --- |
|  `21`   |  21 + 12   | `33` |
|   `32`  |  32 + 23   | `55` |
| `123` | 123 + 321  | `444` |
| `3548` | 3548 + 8453  | `444` |

### Old Fashioned Texting (Difficulty 6 out of 10)

Remember trying to text on an older cell phone?  You'd have to press a number multiple times to select a certain letter.

Create a function to convert a string into number presses on an old cell phone.  Separate each sequence by a hyphen.

Examples:

| Input | Output |
| --- | --- |
| `'hello world'` | `'44-33-555-555-666-0-9-666-777-555-3'` |
| `'idk my bff jill'` | `'444-3-55-0-6-999-0-22-333-333-0-5-444-555-555'` |
| `'she mad woke frfr'` | `'7777-44-33-0-6-2-3-0-9-666-55-33-0-333-777-333-777'` |

###  Find Friday the 13ths (Difficulty 8 out of 10)

Create a function that given a year, returns every month that had/has a Friday the 13th.  

Your function should return a list of month names.

Examples:

| Input | Output |
| --- | --- | 
| `2019` | `['September', 'December']` |
| `1995` | `['January', 'October']` |
| `1980` | `['June']` |