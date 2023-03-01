import Running as Run
from Running import *
import random
MAX_LINES = 3
MAX_BET =100
MIN_BET = 1

def deposit():
    while True:
        amount = input("Enter the amount to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
               print ("Entered amount should be greater than zero!")
        else:
            print("Enter a valid amount!!")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter th number of lines to bet (1 - "+ str(MAX_LINES)+"):")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
               print("number of lines should be greater than zero!")
        else:
            print("Enter a valid amount!!")
    return lines
       
def get_bet():
    while True:
        amount = input("Enter the amount to bet on each line ? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
               print(f"Amount must be between ${MIN_BET} - ${MAX_BET} ")
        else:
            print("Enter a valid amount!!")
    return amount


def spin(balance):

    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You do not have enough balance as your current balance is ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines and Total bet is ${total_bet} ")

    slots = Run.get_slot_machine_spin(ROWS, COLS, symbol_count)
    Run.print_machine(slots)
    winnings, winning_lines = Run.check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines : ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit ).")
        if answer == "q":
            break
        balance +=spin(balance)
    print(f"You left with ${balance}")
    
main()
    
