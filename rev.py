import sqlite3

con=sqlite3.connect("exp.db")

c=con.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
    title TEXT,
    amount REAL,
    date TEXT
    )

""")


def add_exp():
    n = input("title:")
    a = float(input("amount:"))
    d = input("date")

    c.execute("""
        INSERT INTO expenses(title,amount,date) 
        VALUES (?,?,?)
    """, (n, a, d))

    con.commit()


def view_exp():
    c.execute("SELECT * FROM expenses")

    data = c.fetchall()

    print("TITLE |AMOUNT |DATE")
    print("__________________")
    for i in data:
        print(i[0], i[1], i[2])


def tot_exp():
    c.execute("SELECT SUM(amount) FROM expenses")
    s = c.fetchone()
    print("total = ", s[0])





while True:
    print("1 = Add Expense")
    print("2 = view Expense")
    print("3 = total Expense")
    print("4 = exit")
    x=int(input("enter your choice(1/2/3/4)"))
    if x==1:
        add_exp()
    elif x==2:
        view_exp()
    elif x==3:
        tot_exp()
    elif x==4:
        break
    else:
        print("invalid choice")

    
