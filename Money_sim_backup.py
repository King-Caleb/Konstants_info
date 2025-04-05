import tkinter as tk
from random import randint

money = 20
businesses = []
HR_Capita = 0
password = "richie"
let = ""
stocks = {"TechCorp": 100, "FoodInc": 50, "AutoMotive": 75}  # Initial stock prices
portfolio = {"TechCorp": 0, "FoodInc": 0, "AutoMotive": 0}  # Owned stocks


# Function to update stock prices
def update_stocks():
    global stocks
    for stock in stocks:
        stocks[stock] += randint(-10, 10)  # Fluctuate prices randomly
        stocks[stock] = max(stocks[stock], 1)  # Ensure price never drops to 0
    stock_label.config(text=stock_display())
    root.after(100, update_stocks)  # Repeat every 5 seconds


# Function to display stock prices
def stock_display():
    return "\n".join([f"{stock}: ${stocks[stock]}" for stock in stocks])


# Function to buy stocks
def buy_stock():
    global money
    stock_name = stock_entry.get()
    if stock_name in stocks:
        if money >= stocks[stock_name]:
            money -= stocks[stock_name]
            portfolio[stock_name] += 1
            label.config(text=f"You have ${money}")
            stock_portfolio_label.config(text=portfolio_display())
        else:
            stock_portfolio_label.config(text="Not enough money!")


# Function to sell stocks
def sell_stock():
    global money
    stock_name = stock_entry.get()
    if stock_name in portfolio and portfolio[stock_name] > 0:
        money += stocks[stock_name]
        portfolio[stock_name] -= 1
        label.config(text=f"You have ${money}")
        stock_portfolio_label.config(text=portfolio_display())
    else:
        stock_portfolio_label.config(text="No stocks to sell!")


# Function to display owned stocks
def portfolio_display():
    return "\n".join([f"{stock}: {portfolio[stock]} shares" for stock in portfolio])


def make_business():
    global money
    business_name = business_naming.get()  # Get input from the entry field
    if business_name and money >= 20:  # Ensure it's not empty and money is enough
        businesses.append(business_name)
        business_naming.delete(0, tk.END)  # Clear entry field
        money -= 20  # Deduct $20
        # Update labels
        label.config(text=f"You have ${money}")
        business_shown.config(text="Businesses: " + ", ".join(businesses))
    elif money < 20:
        business_shown.config(text="Not enough money!")
        root.after(5000, lambda: business_shown.config(text="Businesses: " + ", ".join(businesses)))


def increase_money_norm():
    global money
    g = len(businesses)
    for i in range(0, g):
        x = randint(1, 20)
        money += x  # Increase money
        label.config(text=f"Money: ${money}")
    root.after(1000, increase_money_norm)  # Call function every second


def inc_m(l, h):
    global money
    x = randint(l, h)
    money += x  # Increase money
    label.config(text=f"Money: ${money}")
    root.after(5000, lambda: inc_m(l, h))  # Call again in 5 seconds with correct arguments


def HRI():
    """Updates HR_Capita with random fluctuations every second."""
    global HR_Capita
    if HR_Capita != 0:  # Only fluctuate if there’s money in High Risk
        fluctuations = randint(-50, 50)
        HR_Capita += fluctuations
        label_HRI.config(text=f"You have ${HR_Capita} in High Risk")

    root.after(1000, HRI)  # Ensures function keeps running even if HR_Capita is 0


def HR_Input():
    """Transfers money into High Risk Investment."""
    global HR_Capita, money
    try:
        HRI_button = int(Invest_HRI.get())
        if money >= HRI_button > 0:  # Prevent negative investments
            HR_Capita += HRI_button
            money -= HRI_button  # Deduct investment amount, not total capital
            label_HRI.config(text=f"You have ${HR_Capita} in High Risk")
            label.config(text=f"You have ${money}")
        else:
            label_HRI.config(text="Not enough money!")
    except ValueError:
        label_HRI.config(text="Invalid Input!")

    Invest_HRI.delete(0, tk.END)  # Clear input field after investing


def HR_Output():
    """Withdraws all money from High Risk Investment back to money balance."""
    global HR_Capita, money
    money += HR_Capita
    HR_Capita = 0
    label_HRI.config(text="You have $0 in High Risk")
    label.config(text=f"You have ${money}")


def set_pass():
    global password
    x = pass_entry.get()
    password = x
    pass_label.config(text=f"your password is{password}")


def random_letters(g):
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # String of letters
    if 1 <= g <= 26:  # Ensure g is within range
        return alphabet[g - 1]  # Return the correct letter
    return None  # Return None if out of range


def hack():
    global money
    x = len(password)  # Get length of password
    g = []  # List to store generated letters

    for i in range(x):  # Loop correct number of times
        letter = random_letters(randint(1, 26))  # Get a random letter
        g.append(letter)
    hacked_password = ''.join(g)  # Convert list to a string
    d = randint(1, 5)
    if d == 1:
        if hacked_password == password:  # Compare properly
            money -= money / 10  # Deduct 10% of money
            label.config(text=f"You have ${money}", font=("Arial", 14))

    root.after(1000, hack)  # Repeat every second


root = tk.Tk()
root.title("ABI Money Sim")
root.geometry("350x300")

# Money Label
label = tk.Label(root, text=f"You have ${money}", font=("Arial", 14))
label.pack(pady=5)

# Entry Field for Business Name
business_naming = tk.Entry(root, font=("Arial", 14))
business_naming.pack(pady=5)

# Button to Create Business
button = tk.Button(root, text="Make a Business (-$20)", command=make_business)
button.pack(pady=5)

# Label to Display Businesses
business_shown = tk.Label(root, text="No businesses yet", font=("Arial", 12))
business_shown.pack(pady=5)

# Investment Section
label_HRI = tk.Label(root, text=f"You have ${HR_Capita} in High Risk", font=("Arial", 12))
label_HRI.pack(pady=5)

Invest_HRI = tk.Entry(root, font=("Arial", 14))
Invest_HRI.pack(pady=5)

button_HRI = tk.Button(root, text="Invest", command=HR_Input)
button_HRI.pack(pady=5)

button_HRW = tk.Button(root, text="Withdraw", command=HR_Output)  # Fixed duplicate button text
button_HRW.pack(pady=5)

button_pass = tk.Button(root, text="Set password", command=set_pass)
button_pass.pack(pady=5)

pass_entry = tk.Entry(root, font=("Arial", 14))
pass_entry.pack(pady=5)

pass_label = tk.Button(root, text=f"your password is {password}")
pass_label.pack(pady=5)
stock_label = tk.Label(root, text=stock_display(), font=("Arial", 12))
stock_label.pack(pady=5)

# Stock Input Entry
stock_entry = tk.Entry(root, font=("Arial", 14))
stock_entry.pack(pady=5)

# Buy and Sell Buttons
buy_button = tk.Button(root, text="Buy Stock", command=buy_stock)
buy_button.pack(pady=5)

sell_button = tk.Button(root, text="Sell Stock", command=sell_stock)
sell_button.pack(pady=5)

# Portfolio Display
stock_portfolio_label = tk.Label(root, text=portfolio_display(), font=("Arial", 12))
stock_portfolio_label.pack(pady=5)

# Start stock fluctuations
update_stocks()
increase_money_norm()
hack()
HRI()  # Start the high-risk fluctuation cycle
root.mainloop()
