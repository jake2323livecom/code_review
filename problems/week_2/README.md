### Add zeros to a string (Difficulty 3 out of 10)

Create a function that takes in both a string and an integer, and adds the appropriate number of `'0'`'s to the string.

Examples:

| Input | Output |
| --- | --- |
| `'some_string', 3` | `'000some_string'` |
| `'some_string', 1` | `'0some_string'` |
| `'some_string', 5` | `'00000some_string'` |

### Find the average (Difficulty 3 out of 10)

Create a function that takes a list of numbers and returns the average expressed _as an integer_.  Round up to the next highest integer if need be.

Examples:

| Input | Output |
| --- | --- |
| `[1, 2, 3, 4, 5]` | `3` |
| `[3, 4, 5, 6]` | `5` |
| `[1, 2, 5, 10]` | `5` |

### Generate powers of 2 (Difficulty 4 out of 10)

Create a function that takes in an integer N, and returns a list of the powers of two, up to 2<sup>N</sup>.

Examples:

| Input | Output |
| --- | --- |
| `5` | `[2, 4, 6, 8, 16, 32]` |
| `12` | `[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]` |
| `13` | `[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]` |

### Sort names (Difficulty 5 out of 10)

Create a function that takes two parameters: a list of names and how you want them sorted, and returns the sorted version of the list using the specified method.  The second parameter can be either `'length'` or `'alphabetic'`, and should determine how the list is sorted.  If something other than `'length'` or `'alphabetic'` is passed as the second parameter, your function should raise a `ValueError` with a custom message.

### Find a subnet ID (Difficulty 7 out of 10)

Create a function that, given an IP address and subnet mask (in dotted decimal notation), can determine the subnet ID the IP address belongs to.

Examples:

| Input | Output |
| --- | --- |
| `'192.168.10.1', '255.255.255.0'` | `'192.168.10.0'` |
| `'10.10.1.1', '255.255.0.0'` | `'10.10.0.0'` |
| `'172.16.2.35', '255.255.255.248'` | `172.16.2.32'` |


