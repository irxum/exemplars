import logging

logging.basicConfig(level=logging.INFO)

COINS = {
    "quarter": 25,
    "dime": 10,
    "nickel": 5,
    "penny": 1
}


def calculate_change(dollar_amount):
    cents = int(dollar_amount * 100)

    def calculate_coins(cents, denomination):
        count = cents // denomination
        return count, cents % denomination

    quarters, cents = calculate_coins(cents, COINS.get("quarter"))
    dimes, cents = calculate_coins(cents, COINS.get("dime"))
    nickels, cents = calculate_coins(cents, COINS.get("nickel"))

    return quarters, dimes, nickels, cents


def display_change(quarters, dimes, nickels, pennies):
    logging.info(f"Quarters: {quarters}")
    logging.info(f"Dimes: {dimes}")
    logging.info(f"Nickels: {nickels}")
    logging.info(f"Pennies: {pennies}")


# Example usage:
dollar_amount = float(input("Enter a dollar amount: "))
quarters, dimes, nickels, pennies = calculate_change(dollar_amount)
display_change(quarters, dimes, nickels, pennies)
