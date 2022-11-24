import math

def add_zero(string: str, num: int) -> str:
    """Adds a certain number of zeros to the beginning of a string."""

    return num * '0' + string


def average(nums: list) -> int:
    """Finds the average expressed as an integer."""

    average =  sum(nums) / len(nums)

    return math.ceil(average)

print(average([1, 2, 3, 4, 5]))
print(average([3, 4, 5, 6]))
print(average([1, 2, 5, 10]))

def two_powers(degree: int) -> list:
    """Returns a list of the powers of two up to a given degree."""

    powers = [2**power for power in range(1, degree + 1)]

    return powers

print(two_powers(5))
print(two_powers(12))
print(two_powers(13))

def sort_names(names: list, method: str) -> list:
    """
    Sorts a list of names based on the method specified.
    Must be either length or alphabetic
    """

    METHOD_CHOICES = [
        'length',
        'alphabetic'
    ]

    if method not in METHOD_CHOICES:
        raise ValueError(f'The method specified ({method}) is not one of the valid choices.  Please select from: {METHOD_CHOICES}')
    elif method == 'length':
        return sorted(names)
    else:
        return sorted(names, key=len)

names = [
    'dwight',
    'jim',
    'pamela',
    'creed',
    'andy'
]

print(sort_names(names, 'length'))
print(sort_names(names, 'alphabetic'))
# print(sort_names(names, 'alpha'))

def subnet_id(ip: str, mask: str) -> str:
    """Finds the subnet ID of an IP address and mask."""
    ip_octets = ip.split('.')
    mask_octets = mask.split('.')
    subnet_octets = []

    for ip_octet, mask_octet in zip(ip_octets, mask_octets):

        ip_octet = int(ip_octet)
        mask_octet = int(mask_octet)
        
        subnet_octet = str(ip_octet & mask_octet)

        subnet_octets.append(subnet_octet)

    return '.'.join(subnet_octets)

print(subnet_id('192.168.10.1', '255.255.255.0'))
print(subnet_id('10.10.1.1', '255.255.0.0'))
print(subnet_id('172.16.2.35', '255.255.255.248'))

