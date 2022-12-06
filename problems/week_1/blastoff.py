from os import system       # Used to send commands to terminal
from time import sleep      # Used to pause the program

def main():
  blast_off(10, 1, "Doge to the moon!")

# region supporting functions
def blast_off(_count: int, _interval: int, _message: str):
  '''Performs countdown and blastoff message
  - _count: total countdown seconds
  - _interval: pause between countdown numbers
  - _message: blast off message to display
  '''

  while _count:             # While loop that runs until '_count' reaches zero
    clear_screen()          # Clears the screen
    print(_count)           # Prints the countdown number
    sleep(_interval)        # Pauses the program for 1 second
    _count -= 1             # Reduces '_count' by one
  
  clear_screen()            # Clears the screen
  
  doge ="─────────▄──────────────▄────\n────────▌▒█───────────▄▀▒▌───\n────────▌▒▒▀▄───────▄▀▒▒▒▐───\n───────▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐───\n─────▄▄▀▒▒▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐───\n───▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀██▀▒▌───\n──▐▒▒▒▄▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄▒▒▌──\n──▌▒▒▐▄█▀▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐──\n─▐▒▒▒▒▒▒▒▒▒▒▒▌██▀▒▒▒▒▒▒▒▒▀▄▌─\n─▌▒▀▄██▄▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌─\n─▌▀▐▄█▄█▌▄▒▀▒▒▒▒▒▒░░░░░░▒▒▒▐─\n▐▒▀▐▀▐▀▒▒▄▄▒▄▒▒▒▒▒░░░░░░▒▒▒▒▌\n▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒░░░░░░▒▒▒▐─\n─▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌─\n─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──\n──▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▌──\n────▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀───\n───▐▀▒▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀─────\n──▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀────────"
  
  print(doge)
  print(_message)


def clear_screen():
  ''' Clears the screen on Windows systems'''
  system("cls")
# endregion

if __name__ == "__main__":
  main()