from random import randint as r      # Used to get a random number

# region stacic vars
GREETINGS = [
  ["Hey there","!"],
  ["Good morning","!"],
  ["Howdy","!"],
  ["G-day","!"],
  ["Hiya","!"],
  ["What up","?"],
  ["Sup","?"],
  ["Whazzup","?"],
  ["How do you do","?"],
  ["How have you been","?"],
  ["How is everything","?"],
  ["How are things","?"],
  ["How's it hanging","?"],
  ["How's life","?"],
  ["What's new","?"]
]
# endregion


def main():
  name = str(input(("Enter your name: ")))
  print(greetings(name))


# region supporting functions
def get_greeting_int() -> int:
  '''
  Returns a random int based on
  the length of the greeting list
  '''
  return r(0,len(GREETINGS)-1)


def greetings(_name: str) -> str :
  ''' Returns a greeting '''
  greet = GREETINGS[get_greeting_int()]
  return f"{greet[0]} {_name}{greet[1]}"
# endregion


if __name__ == "__main__":
  main()