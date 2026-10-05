# Lab 01: Setting Up the AI-Augmented Development Environment
# Scenario: the same Celsius-to-Fahrenheit converter, built once by hand
# and once with an AI assistant, then compared.


# Activity 1: Build it by hand first
# My first draft used integer-style division and gave wrong answers, it was
# caught by testing a known value (100C should be 212F). Fixed version:
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

print(celsius_to_fahrenheit(100)) 


# Activity 2: Build it again with AI assistance
def celsius_to_fahrenheit_ai(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


def read_celsius():
    try:
        return float(input("Celsius: "))
    except ValueError:
        print("Please enter a number.")
        return None


# Activity 3: Compare
# The AI version didn't get lucky, it defaulted to float division and input
# checking. The hand-written bug was a common mistake, not carelessness.

# Activity 4: Commit both, clearly labelled
# $ git init cse325-lab01 && cd cse325-lab01
# $ git add hand_written.py && git commit -m "Hand-written converter (found and fixed integer-division bug)"
# $ git add ai_assisted.py && git commit -m "AI-assisted converter (float division and input validation from first draft)"

if __name__ == "__main__":
    value = read_celsius()
    if value is not None:
        print(f"{value}C = {celsius_to_fahrenheit_ai(value)}F")


# Task 4: Defend one difference
# Biggest difference: the AI version validates input with try/except (see
# read_celsius in this file, the try block), the hand-written one does not.
# I think it is a real improvement, not just a different habit, because a
# non-numeric input would crash the hand-written program with a ValueError.
# It costs only a few lines. The catch is that it only handles ValueError,
# so something like an EOF error on input() would still crash it.


# Lab Assignment
# Small utility built twice: tip splitter
def split_tip(bill, tip_percent, people):
    total = bill * (1 + tip_percent / 100)
    return total / people


# Give the AI version to a classmate for five minutes and note what they
# broke (e.g. people = 0 gives ZeroDivisionError, negative bill accepted).
def split_tip_safe(bill, tip_percent, people):
    if bill < 0 or tip_percent < 0:
        raise ValueError("bill and tip must not be negative")
    if people < 1:
        raise ValueError("people must be at least 1")
    return bill * (1 + tip_percent / 100) / people

