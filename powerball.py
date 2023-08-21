import random


def generate_powerball_numbers():
    white_balls = random.sample(range(1, 70), 5)
    power_ball = random.randint(1, 26)
    return sorted(white_balls), power_ball


def is_valid_powerball_number(number):
    return 1 <= number <= 69


def is_valid_powerball_power_number(number):
    return 1 <= number <= 26


def get_valid_powerball_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if is_valid_powerball_number(number):
                return number
            else:
                print(
                    "Invalid number. Please enter a valid white ball number between 1 and 69."
                )
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_valid_powerball_power_number():
    while True:
        try:
            number = int(input("Enter your Powerball number (1 - 26): "))
            if is_valid_powerball_power_number(number):
                return number
            else:
                print(
                    "Invalid number. Please enter a valid Powerball number between 1 and 26."
                )
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def number_to_words(num):
    # Define dictionaries for number names
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = [
        "",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "ten",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    thousands = ["", "thousand", "million", "billion"]

    if num == 0:
        return "zero"

    parts = []
    part_index = 0

    while num > 0:
        part = num % 1000
        if part > 0:
            part_str = ""
            if part >= 100:
                part_str += ones[part // 100] + " hundred"
                part %= 100
                if part > 0:
                    part_str += " and "
            if 11 <= part <= 19:
                part_str += teens[part - 10]
                part = 0
            elif part >= 20:
                part_str += tens[part // 10]
                part %= 10
                if part > 0:
                    part_str += " " + ones[part]
            elif part > 0:
                part_str += ones[part]
            parts.append(part_str.strip() + " " + thousands[part_index])

        num //= 1000
        part_index += 1

    return " ".join(parts[::-1]).strip()


def simulate_powerball_jackpot(powerball_number):
    counter = 1
    while True:
        white_balls, power_ball = generate_powerball_numbers()

        print(
            f"Drawing {counter}: Powerball numbers: {white_balls}, Powerball: {power_ball}"
        )

        if white_balls == powerball_number:
            jackpot = (counter * 5) / 2
            cost = number_to_words(counter * 5)
            counter = number_to_words(counter)
            print(f"Congratulations! You've hit the jackpot!")
            print(f"{counter} drawings!")
            print(f"Estimated jackpot size is: ${jackpot}")
            break

        counter += 1


if __name__ == "__main__":
    print("Enter 5 unique white ball numbers between 1 and 69:")
    white_balls = [
        get_valid_powerball_number(f"White ball {i + 1}: ") for i in range(5)
    ]

    power_ball = get_valid_powerball_power_number()

    powerball_number = sorted(white_balls)

    print("Your Powerball numbers:", white_balls, "Powerball:", power_ball)

    simulate_powerball_jackpot(powerball_number)
