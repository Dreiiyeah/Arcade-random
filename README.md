# Secure Ticket Redemption System with Random Password Generator

## Overview
This is a Python-based arcade system that allows users to:
- Create secure accounts with randomly generated passwords
- Log in and manage tickets
- Play mini-games to earn tickets
- Redeem tickets for prizes

The system simulates a simple arcade experience with account handling and rewards.

---

## Features

### Account Management
- Create a new account with a secure random password
- Login system with username and password verification
- View account details (username, password, tickets)

### Ticket System
- Users start with 20 tickets
- Earn tickets by playing games
- Spend tickets to redeem prizes

### Redemption System
Users can exchange tickets for rewards:
- Stuffed Toy → 15 tickets  
- Keychain → 5 tickets  
- Candy → 2 tickets  

---

## Games Available

### 1. Number Guessing Game
- Guess a number between 1–10
- You have 3 attempts
- Reward: +5 tickets if correct

### 2. Tic Tac Toe
- Play against a bot
- Random turn order (player or bot starts)
- Reward: +5 tickets if you win

---

## Password Generator
- Uses `secrets` module for strong randomness
- Password length: 8–15 characters
- Includes:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters

---

## How It Works

### Program Flow
1. Start menu:
   - Create account
   - Log in
2. After login:
   - Account info
   - Redeem tickets
   - Play games
   - Log out

---

## Data Structure

User data is stored in a dictionary:

```python
users = {
    "Username": {
        "Password": "password",
        "Tickets": 20
    }
}
```

