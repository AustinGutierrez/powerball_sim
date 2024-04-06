import random
from typing import Tuple, List

def generate_powerball_numbers() -> Tuple[List[int], int]:
    """
    Generate a set of Powerball numbers consisting of 5 unique white balls and 1 power ball.

    Returns:
        Tuple[List[int], int]: A tuple containing a list of 5 sorted unique white balls and 1 power ball.
    """
    white_balls = random.sample(range(1, 70), 5)
    power_ball = random.randint(1, 26)
    return sorted(white_balls), power_ball

def get_valid_number(prompt: str, min_val: int, max_val: int) -> int:
    """
    Request a valid number from the user within a specified range.

    Args:
        prompt (str): The message displayed to the user.
        min_val (int): The minimum valid value.
        max_val (int): The maximum valid value.

    Returns:
        int: A valid number entered by the user.
    """
    while True:
        try:
            number = int(input(prompt))
            if min_val <= number <= max_val:
                return number
            else:
                print(f"Invalid number. Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_user_or_auto_input() -> Tuple[List[int], int]:
    """
    Allow the user to choose between manually entering Powerball numbers or generating them automatically.

    Returns:
        Tuple[List[int], int]: A tuple containing a list of 5 sorted white balls and 1 power ball.
    """
    while True:
        choice = input("Do you want to enter your numbers (enter '1') or generate them automatically (enter '2')? ")
        if choice == '1':
            white_balls = [get_valid_number(f"White ball {i + 1} (1-69): ", 1, 69) for i in range(5)]
            power_ball = get_valid_number("Enter your Powerball number (1-26): ", 1, 26)
            return sorted(white_balls), power_ball
        elif choice == '2':
            return generate_powerball_numbers()
        else:
            print("Invalid choice. Please enter '1' or '2'.")

def simulate_powerball_jackpot(target_white_balls: List[int]) -> None:
    """
    Simulate Powerball jackpot draws until the target white balls are drawn, displaying the number of attempts and total cost.

    Args:
        target_white_balls (List[int]): The list of white balls to match for winning the jackpot.
    """
    counter = 1
    ticket_price = 5  # Ticket price in dollars
    while True:
        white_balls, power_ball = generate_powerball_numbers()
        if counter % 10000 == 0:
            print(f"Attempt {counter}: Still trying to win...")
        if white_balls == target_white_balls:
            total_spent = counter * ticket_price
            print(f"\nCongratulations! You've hit the jackpot on drawing {counter}!")
            print(f"Your numbers: {target_white_balls}, Powerball: {power_ball}")
            print(f"Total amount spent on tickets: ${total_spent:,}")
            break
        counter += 1

if __name__ == "__main__":
    print("Powerball Number Generator")
    user_white_balls, user_power_ball = get_user_or_auto_input()
    
    print(f"\nYour Powerball numbers: {user_white_balls}, Powerball: {user_power_ball}")
    simulate_powerball_jackpot(user_white_balls)
