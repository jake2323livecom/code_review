from time import sleep

print('Hello World!')

def greeting():
    """Prints a generic greeting."""

    print('Good morning!')

def personal_greeting(name: str) -> str:
    """Prints a greeting for a personal name."""

    print(f'Good morning, {name}!')

def count_down():
    """Prints a space shuttle countdown"""

    for num in range(10, 0, -1):
        print(f'{num}...')
        sleep(1)

    print('Lift off!')

count_down()