
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount =int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of line to bet on (1-3)? ")
        if lines.isdigit():
            lines =int(lines)
            if lines <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount =int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between 1 - 100")
        else:
            print("Please enter a number.")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficent Funds Current Balance is {balance}")
        else:
            break

    
    print(f"You are betteing ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    


main()