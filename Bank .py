import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Customers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    address TEXT
)
""")

# Accounts Table
cursor.execute("""'
CREATE TABLE IF NOT EXISTS accounts (
    account_no INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    account_type TEXT,
    balance REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

conn.commit()

# Add Customer
def add_customer():
    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    cursor.execute(
        "INSERT INTO customers(name, phone, address) VALUES (?, ?, ?)",
        (name, phone, address)
    )

    conn.commit()
    print("Customer Added Successfully!")

# Create Account
def create_account():
    customer_id = int(input("Enter Customer ID: "))
    account_type = input("Enter Account Type (Savings/Current): ")
    balance = float(input("Enter Initial Balance: "))

    cursor.execute(
        "INSERT INTO accounts(customer_id, account_type, balance) VALUES (?, ?, ?)",
        (customer_id, account_type, balance)
    )

    conn.commit()
    print("Account Created Successfully!")

# View Customers
def view_customers():
    cursor.execute("SELECT * FROM customers")
    data = cursor.fetchall()

    print("\n----- CUSTOMER DETAILS -----")
    for row in data:
        print(row)

# View Accounts
def view_accounts():
    cursor.execute("""
    SELECT accounts.account_no,
           customers.name,
           accounts.account_type,
           accounts.balance
    FROM accounts
    JOIN customers
    ON accounts.customer_id = customers.customer_id
    """)

    data = cursor.fetchall()

    print("\n----- ACCOUNT DETAILS -----")
    for row in data:
        print(row)

# Deposit
def deposit():
    account_no = int(input("Enter Account Number: "))
    amount = float(input("Enter Amount to Deposit: "))

    cursor.execute(
        "UPDATE accounts SET balance = balance + ? WHERE account_no = ?",
        (amount, account_no)
    )

    conn.commit()
    print("Amount Deposited Successfully!")

# Withdraw
def withdraw():
    account_no = int(input("Enter Account Number: "))

    cursor.execute(
        "SELECT balance FROM accounts WHERE account_no = ?",
        (account_no,)
    )

    result = cursor.fetchone()

    if result:
        balance = result[0]

        amount = float(input("Enter Amount to Withdraw: "))

        if amount <= balance:
            cursor.execute(
                "UPDATE accounts SET balance = balance - ? WHERE account_no = ?",
                (amount, account_no)
            )

            conn.commit()
            print("Withdrawal Successful!")
        else:
            print("Insufficient Balance!")
    else:
        print("Account Not Found!")

# Delete Account
def delete_account():
    account_no = int(input("Enter Account Number to Delete: "))

    cursor.execute(
        "DELETE FROM accounts WHERE account_no = ?",
        (account_no,)
    )

    conn.commit()
    print("Account Deleted Successfully!")

# Main Menu
while True:
    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Add Customer")
    print("2. Create Account")
    print("3. View Customers")
    print("4. View Accounts")
    print("5. Deposit Money")
    print("6. Withdraw Money")
    print("7. Delete Account")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_customer()

    elif choice == "2":
        create_account()

    elif choice == "3":
        view_customers()

    elif choice == "4":
        view_accounts()

    elif choice == "5":
        deposit()

    elif choice == "6":
        withdraw()

    elif choice == "7":
        delete_account()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")

conn.close()