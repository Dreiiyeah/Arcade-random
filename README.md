# Arcade-random

### About The Project

An arcade based project using keys from a random password generator. It focuses on playing games to earn points to be later used in purchasing prizes. The project helps aids having saftey handling data in arcades.

## Table of Contents

- [Technologies Used](#technologies-used)

- [Current Features](#current-features)

## Technologies Used

- Python
  - Python is the main coding language used.
    
- secrets library
  - Used to make random passwords and it to be more secure.
    
- string library
  - Used to get all available characters.

- random library
  - Used to generate random numbers.
    
- time library
  - Used to pause between program execution.

## Current Features

- starting(dic)
  - Lets user choose if they want to login, create account, or exit.

- generate_password()
  - Creates a randomly generated password.

- output_accs(Dict)
  - Outputs the information of all created accounts(username, password, and tickets).

- acc_creation(arr, dic)
  - Creates an account using users inputted username and a randomly generated password of the users inputted length.

- options(Dict)
  - Displays options and makes you input the desired option.

- log_in(Dict)
  - Logs into account based on inputted username and generated password.
 
- account(arr)
  - Displays account information.

- redeem(arr)

- games(arr, dic)
  - Allows user to pick a game of their choice.

- num_guess_game(arr, dic)
  - A number guessing game.

- output_board(arr)
  - Displays tictactoe board.
