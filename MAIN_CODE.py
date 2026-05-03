# Secure Ticket Redemption System with Random Password Generator

import string
import secrets
import random
import time
import json

# PASSWORD GENERATOR FUNCTION

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

DATA_FILE = "users.json"

# ---------- JSON LOAD / SAVE ----------

def load_users():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "Jeremy" : {
              "Password" : '677777',
              "Tickets" : 676767
            }
        }

def save_users(dic):
    with open(DATA_FILE, "w") as f:
        json.dump(dic, f, indent=4)

users = load_users()

board = ['-','-','-','-','-','-','-','-','-']

winner = None

# ---------------- MAIN ----------------

def main(dic):
  while True:
    user = starting(dic)
    options(user,dic)

# ---------------- ACC DISPLAY ----------------

def output_accs(Dict):

  print('')
  print('='*39)
  print(f'Username {'|':>8}Password{'|':>3}Tickets{'|':>4}')
  print('-'*39)

  for key in Dict:
    if len(key) >= 8:
        print(f'{key}', end = '\t|')
    else:
        print(key, end = '\t\t|')

    for nestKeys in Dict[key]:
        print(f"{Dict[key][nestKeys]:<10}|", end = '')

    print('')

  print('='*39)

# ---------------- PASSWORD ----------------

def generate_password():
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

# ---------------- ACCOUNT ----------------

def acc_creation(Dict):
  print("===== CREATE ACCOUNT =====")
  while True:
    username = input("Enter a username: ")

    if username in Dict:
      print("\nUsername already exists. Try another.")
    else:
      break

  password = generate_password()

  tickets = 20

  print("\nAccount created successfully!")
  print("Username:", username)
  print(f'Password: {password}')
  print("Starting Tickets:", tickets,'\n')

  Dict[username] = {
    "Password" : password,
    "Tickets" : tickets
  }

  save_users(Dict)

# ---------------- OPTIONS ----------------

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

# ---------------- LOGIN ----------------

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

# ---------------- ACCOUNT ----------------

def account(arr):
  print('\n===============ACCOUNT===============')
  print(f'Username {'|':>5}Password{'|':>5}Tickets{'|':>5}')
  print('-'*39)
  for i in range(len(arr)):
    print(f'{arr[i]:<12}|', end = '')
  print('')
  print('='*39)

# ---------------- REDEEM ----------------

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
        dic[arr[0]] = {"Password":arr[1],"Tickets":arr[2]}
        save_users(dic)
        print("You redeemed a Stuffed Toy!")
      else:
        print("Not enough tickets.")

    elif choice == "2":
      if arr[2] >= 5:
        arr[2] -= 5
        dic[arr[0]] = {"Password":arr[1],"Tickets":arr[2]}
        save_users(dic)
        print("You redeemed a Keychain!")
      else:
        print("Not enough tickets.")

    elif choice == "3":
      if arr[2] >= 2:
        arr[2] -= 2
        dic[arr[0]] = {"Password":arr[1],"Tickets":arr[2]}
        save_users(dic)
        print("You have redeemed Candy!")
      else:
        print("Not enough tickets.")

    elif choice == "4":
      break

    else:
      print("Invalid input.")

# ---------------- LOG OUT ----------------

def log_out():
  print("Successfully logged out")

# ---------------- START ----------------

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

# ---------------- GAMES ----------------

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

# ---------------- GUESS GAME ----------------

def num_guess_game(arr,dic):

  guess = random.randint(1,10)

  print('\n=====GUESSING GAME=====')

  for i in range(3):
    try:
      user = int(input('\nEnter your guess (1-10):'))
    except ValueError:
      continue

    if user == guess:
      print('\nCorrect! Here is your reward (5 tickets)')
      arr[2] += 5
      dic[arr[0]] = {"Password":arr[1],"Tickets":arr[2]}
      save_users(dic)
      return

# ---------------- TIC TAC TOE ----------------

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

  board = ['-']*9
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
    try:
      user = int(input('Enter a number from 1-9: '))
      if 1 <= user <= 9 and arr[user-1] == '-':
        arr[user-1] = 'O'
        output_board(arr)
        break
    except ValueError:
      print('Please enter a valid number.')


def bot_change(arr):
  while True:
    pick = random.randint(0,8)
    if arr[pick] == '-':
      arr[pick] = 'X'
      output_board(arr)
      break


def checkHorizontal(arr):
  global winner
  if arr[0] == arr[1] == arr[2] != '-':
    winner = 'human' if arr[0]=='O' else 'bot'
  elif arr[3] == arr[4] == arr[5] != '-':
    winner = 'human' if arr[3]=='O' else 'bot'
  elif arr[6] == arr[7] == arr[8] != '-':
    winner = 'human' if arr[6]=='O' else 'bot'


def checkVertical(arr):
  global winner
  if arr[0] == arr[3] == arr[6] != '-':
    winner = 'human' if arr[0]=='O' else 'bot'
  elif arr[1] == arr[4] == arr[7] != '-':
    winner = 'human' if arr[1]=='O' else 'bot'
  elif arr[2] == arr[5] == arr[8] != '-':
    winner = 'human' if arr[2]=='O' else 'bot'


def checkDiagonal(arr):
  global winner
  if arr[0] == arr[4] == arr[8] != '-':
    winner = 'human' if arr[0]=='O' else 'bot'
  elif arr[2] == arr[4] == arr[6] != '-':
    winner = 'human' if arr[2]=='O' else 'bot'


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
        save_users(dic)
        break

      elif winner == 'bot':
        print("Oops. You lost.")
        break

      elif '-' not in arr:
        print("It's a draw! No points awarded.")
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
        save_users(dic)
        break

      elif winner == 'bot':
        print("Oops. You lost.")
        break

      elif '-' not in arr:
        print("It's a draw! No points awarded.")
        break

main(users)
