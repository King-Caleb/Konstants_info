from mpmath import mp


def calculate_pi(digits):
    mp.dps = digits + 2  # Set precision (extra digits to reduce rounding errors)
    return str(mp.pi)[:digits + 2]  # Return π as a string with desired precision


if __name__ == "__main__":
    try:
        digits = int(input("Enter the number of digits of π to calculate: "))
        if digits <= 0:
            print("Please enter a positive integer.")
        else:
            print(f"π to {digits} digits: {calculate_pi(digits)}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
