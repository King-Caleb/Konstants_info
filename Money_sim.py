import tkinter as tk
from random import randint, choice
from tkinter import messagebox
import monry_sim_android

money = 20
businesses = []
HR_Capita = 0
password = "richie"
stocks = {"TechCorp": 100, "FoodInc": 50, "AutoMotive": 75}
portfolio = {"TechCorp": 0, "FoodInc": 0, "AutoMotive": 0}


def update_stocks():
    global stocks
    for stock in stocks:
        stocks[stock] += randint(-50, 50)  # Extreme fluctuations
        stocks[stock] = max(stocks[stock], -100)  # Allow negative values for chaos
    stock_label.config(text=stock_display())
    root.after(2000, update_stocks)


def stock_display():
    return "\n".join([f"{stock}: ${stocks[stock]}" for stock in stocks])


def buy_stock():
    global money
    stock_name = stock_entry.get()
    if stock_name in stocks:
        if money >= stocks[stock_name]:
            money -= stocks[stock_name]
            portfolio[stock_name] += 1
            label.config(text=f"You have ${money}")
            stock_portfolio_label.config(text=portfolio_display())

            # Prank: Make money randomly disappear
            if randint(1, 5) == 1:
                money = randint(-500, 5)
                label.config(text=f"You have ${money}")
        else:
            stock_portfolio_label.config(text="Not enough money!")


def sell_stock():
    global money
    stock_name = stock_entry.get()
    if stock_name in portfolio and portfolio[stock_name] > 0:
        money += stocks[stock_name]
        portfolio[stock_name] -= 1
        label.config(text=f"You have ${money}")
        stock_portfolio_label.config(text=portfolio_display())

        # Prank: Display fake hacking message
        if randint(1, 4) == 1:
            messagebox.showwarning("Security Alert", "Your password has been sent to hackers!")
    else:
        stock_portfolio_label.config(text="No stocks to sell!")


def portfolio_display():
    return "\n".join([f"{stock}: {portfolio[stock]} shares" for stock in portfolio])


def fake_virus():
    messages = [
        "Warning! Unusual Activity Detected!",
        "System Error: Self-Destruction in 10 seconds!",
        "Your bank account has been drained!",
        "Caleb Alamu hacked you"
    ]
    messagebox.showerror("System Alert", choice(messages))
    root.after(randint(5000, 15000), fake_virus)  # Trigger every 5-15 sec


def set_pass():
    global password
    x = pass_entry.get()
    password = x
    pass_label.config(text=f"Your password is {password}")

    # Prank: Randomly change the password on them
    if randint(1, 3) == 1:
        password = "hacked" + str(randint(100, 999))
        pass_label.config(text=f"Your password is {password}")


def hack():
    global money
    if randint(1, 5) == 1:
        money = randint(-999, 9999)
        label.config(text=f"You have ${money}")
    root.after(3000, hack)


root = tk.Tk()
root.title("ABI Money Sim()p")
root.geometry("350x300")

label = tk.Label(root, text=f"You have ${money}", font=("Arial", 14))
label.pack(pady=5)

stock_label = tk.Label(root, text=stock_display(), font=("Arial", 12))
stock_label.pack(pady=5)

stock_entry = tk.Entry(root, font=("Arial", 14))
stock_entry.pack(pady=5)

buy_button = tk.Button(root, text="Buy Stock", command=buy_stock)
buy_button.pack(pady=5)

sell_button = tk.Button(root, text="Sell Stock", command=sell_stock)
sell_button.pack(pady=5)

stock_portfolio_label = tk.Label(root, text=portfolio_display(), font=("Arial", 12))
stock_portfolio_label.pack(pady=5)

pass_entry = tk.Entry(root, font=("Arial", 14))
pass_entry.pack(pady=5)

pass_label = tk.Button(root, text=f"Your password is {password}")
pass_label.pack(pady=5)

pass_button = tk.Button(root, text="Set Password", command=set_pass)
pass_button.pack(pady=5)

update_stocks()
hack()
fake_virus()
root.mainloop()
