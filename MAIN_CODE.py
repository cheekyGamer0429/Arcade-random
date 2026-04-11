
# Secure Ticket Redemption System with Random Password Generator

import string
import secrets
import random
import time

# PASSWORD GENERATOR FUNCTION

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

users = {
    "Jeremy" : {
      "Password" : '677777',
      "Tickets" : 676767
      }
    }

board = ['-','-','-',
         '-','-','-',
         '-','-','-']

winner = None

def main(dic):
  while True:
    user = starting(dic)
    options(user,dic)

def output_accs(Dict):

  print('')
  print('='*39)
  print(f'Username {'|':>8}Password{'|':>3}Tickets{'|':>4}')
  print('-'*39)

  for key in Dict: # Gets the key
    if len(key) >= 8: # Checks the length of key for cleanliness
        print(f'{key}', end = '\t|')
    else:
        print(key, end = '\t\t|')

    for nestKeys in Dict[key]: # Gets the nested keys.
        print(f"{Dict[key][nestKeys]:<10}|", end = '') # Outputs the values of the nested dictionary.

    print('')

  print('='*39)

def generate_password():
    """Generates a secure password (minimum 8 characters)."""
    while True:
        try:
            length = int(input("Enter Desired Password Length (must be >= 8 and <= 15): "))
            if length < 8 or length >15:
                print("Password length must be 8 characters and less then or equal to 15 characters. Please try again.")
            else:
                password = "".join(secrets.choice(characters) for i in range(length))
                print("\nYour generated password is:", password)
                return password
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def acc_creation(Dict):
  print("===== CREATE ACCOUNT =====")
  while True:
    username = input("Enter a username: ")

    if username in Dict:
      print("\nUsername already exists. Try another.")
    else:
      break

  password = generate_password()


  # Starting tickets
  tickets = 20

  print("\nAccount created successfully!")
  print("Username:", username)
  print(f'Password: {password}')
  print("Starting Tickets:", tickets,'\n')

  Dict[username] = {
    "Password" : password,
    "Tickets" : tickets
    }

def options(arr,dic):
  while True:
    print('\n')
    print("="*40)
    print("\t\tOptions")
    print("-"*40)
    print(f"Account   Redeem    Games   Log out")

    command = input('\nPlease enter the option that you want to do: ').lower()

    if command == 'account':
      account(arr)

    elif command == 'redeem':
      redeem(arr,dic)

    elif command == 'games':
      games(arr,dic)

    elif command == 'log out':
      log_out()
      break


def log_in(Dict):
  while True:
    output_accs(Dict)
    print("\n===== LOGIN =====")
    login_user = input("Enter username: ")
    login_pass = input("Enter password: ")

    for key in Dict:
      if login_user == key:
        if login_pass == Dict[key]['Password']:
          tickets = Dict[key]['Tickets']
          return [login_user,login_pass,tickets]
    print('Login Failed. Please try again.')

def account(arr):
  print('\n===============ACCOUNT===============')
  print(f'Username {'|':>5}Password{'|':>5}Tickets{'|':>5}')
  print('-'*39)
  for i in range(len(arr)):
    print(f'{arr[i]:<12}|', end = '')
  print('')
  print('='*39)

def redeem(arr,dic):

  print("\nAvailable Prizes:")
  print("1. Stuffed Toy - 15 tickets")
  print("2. Keychain - 5 tickets")
  print("3. Candy - 2 tickets")
  print("4. Exit.")

  while True:
    choice = input("Choose a prize (1-3): ")
    if choice == "1":
      if arr[2] >= 15:
        arr[2] -= 15
        dic[arr[0]] = {
    "Password" : arr[1],
    "Tickets" : arr[2]
    }
        print("You redeemed a Stuffed Toy!")
      else:
        print("Not enough tickets.")
    elif choice == "2":
      if arr[2] >= 5:
        arr[2] -= 5
        dic[arr[0]] = {
    "Password" : arr[1],
    "Tickets" : arr[2]
    }
        print("You redeemed a Keychain!")
      else:
        print("Not enough tickets.")
    elif choice == "3":
      if arr[2] >= 2:
        arr[2] -= 2
        dic[arr[0]] = {
    "Password" : arr[1],
    "Tickets" : arr[2]
    }
        print("You have redeemed Candy!")
      else:
        print("Not enough tickets.")
    elif choice == "4":
      break
    else:
      print("Invalid input.")

def log_out():
  print("Successfully logged out")

def starting(dic):
  while True:
    print('\n=====ARCADE=====')
    choice = input('Enter "1" to create an account \nEnter "2" to Log in\nEnter option: ')
    if choice == '1':
      acc_creation(dic)
    elif choice == '2':
      return log_in(dic)
    else:
      print('Invalid input.')

def games(arr,dic):
  global board
  while True:
    print('\n======GAMES=====')
    print('1. Number guessing game (5 tickets per win) \n2. Tic Tac Toe (5 tickets per win) \n3. Exit')
    while True:
      try:
        game = int(input('Enter number of game to play: '))
        break
      except ValueError:
        print('Enter valid number.')
    if game == 1:
      num_guess_game(arr,dic)
    elif game == 2:
      player_decision(board,arr,dic)
    elif game == 3:
      break
    else:
      print('Please enter a valid number')

def num_guess_game(arr,dic):

  guess = random.randint(1,10)

  print('\n=====GUESSING GAME=====')
  print('Im thinking of a number from 1-10. Can you guess it?')
  print('Reminder...')
  time.sleep(2)
  print('Only 3 guesses')

  for i in range(3):
    while True:
      while True:
        try:
          user = int(input('\nEnter your guess (1-10):'))
          break
        except ValueError:
          print('Enter a valid Number.')

      if i == 2:
        if user <= 10 and user >= 1:
          if user > guess:
            print('FAILED')
            return
          elif user < guess:
            print('FAILED')
            return
          elif user == guess:
            print('\nCorrect! Here is your reward (5 tickets)')
            arr[2] += 5
            dic[arr[0]] = {
      "Password" : arr[1],
      "Tickets" : arr[2]
      }
            return
        else:
          print('Enter a valid number.')

      elif user <= 10 and user >= 1:
        if user > guess:
          print('Lower. Try again')
          break
        elif user < guess:
          print('Higher. Try again')
          break
        elif user == guess:
          print('Correct! Here is your reward (5 tickets)')
          arr[2] += 5
          dic[arr[0]] = {
      "Password" : arr[1],
      "Tickets" : arr[2]
      }
          return 
      else:
        print('Enter a valid number.')

def output_board(arr):
  print('=====TIC TAC TOE=====\n')
  print(f' {arr[0]} | {arr[1]} | {arr[2]} ')
  print('-'*11)
  print(f' {arr[3]} | {arr[4]} | {arr[5]} ')
  print('-'*11)
  print(f' {arr[6]} | {arr[7]} | {arr[8]} ')

def player_decision(arr,acc_values,dic):
  global board
  global winner
  board = ['-','-','-',
         '-','-','-',
         '-','-','-']
  winner = None
  currentPlayer = random.randint(0,1)
  if currentPlayer == 0:
    output_board(arr)
    print('You make the first move.')
    upd_board(arr,0,acc_values,dic)
  else:
    print('I make the first move...')
    upd_board(arr,1,acc_values,dic)

def user_change(arr):
  while True:
    while True:
      try:
        user = int(input('Enter a number from 1-9: '))
        break
      except ValueError:
        print('Please enter a valid number.')
    if user >= 1 and user <= 9 and arr[user - 1] == '-':
      arr[user - 1] = 'O'
      output_board(arr)
      break
    elif user < 1 or user > 9:
      print('Please enter a valid number')
    else:
      print('Oops player is already in that spot!')

def bot_change(arr):
  while True:
    pick = random.randint(0,8)
    if arr[pick] == '-':
      arr[pick] = 'X'
      output_board(arr)
      break

def upd_board(arr,value,acc_values,dic):
  global winner
  if value == 1:
    while True:
      bot_change(arr)
      user_change(arr)
      checkHorizontal(arr)
      checkVertical(arr)
      checkDiagonal(arr)
      if winner == 'human':
        print("Congratulations! You win!")
        acc_values[2] += 5
        dic[acc_values[0]]["Tickets"] = acc_values[2]
        break
      elif winner == 'bot':
        print("Oops. You lost.")
        break
      elif '-' not in arr:
        print("It's a draw!")
        break

  elif value == 0:
    while True:
      user_change(arr)
      bot_change(arr)
      checkHorizontal(arr)
      checkVertical(arr)
      checkDiagonal(arr)
      if winner == 'human':
        print("Congratulations! You win!")
        acc_values[2] += 5
        dic[acc_values[0]]["Tickets"] = acc_values[2]
        break
      elif winner == 'bot':
        print("Oops. You lost.")
        break
      elif '-' not in arr:
        print("It's a draw!")
        break


def checkVertical(arr):
  global winner
  if arr[0] == arr[3] == arr[6] and arr[0] != '-':
    if arr[0] == 'O':
      winner = 'human'
      return
    else:
      winner = 'bot'
      return

  elif arr[1] == arr[4] == arr[7] and arr[1] != '-':
    if arr[1] == 'O':
      winner = 'human'
      return
    else:
      winner = 'bot'
      return

  elif arr[2] == arr[5] == arr[8] and arr[2] != '-':
    if arr[2] == 'O':
      winner = 'human'
      return
    else:
      winner = 'bot'
      return

def checkHorizontal(arr):
  global winner

  if arr[0] == arr[1] == arr[2] and arr[0] != '-':
    if arr[0] == 'O':
      winner = 'human'
      return
    else:
      winner = 'bot'
      return

  elif arr[3] == arr[4] == arr[5] and arr[3] != '-':
    if arr[3] == 'O':
      winner = 'human'
      return
    else:
      winner = 'bot'
      return

  elif arr[6] == arr[7] == arr[8] and arr[6] != '-':
    if arr[6] == 'O':
      winner = 'human'
      return
    else:
      winner = 'bot'
      return

def checkDiagonal(arr):
  global winner

  if arr[0] == arr[4] == arr[8] and arr[0] != '-':
    if arr[0] == 'O':
      winner = 'human'
      return
    else:
      winner = 'bot'
      return

  elif arr[2] == arr[4] == arr[6] and arr[2] != '-':
    if arr[2] == 'O':
      winner = 'human'
      return
    else:
      winner = 'bot'
      return

main(users)