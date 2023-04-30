import psycopg2
from config import config
params = config()
n = int(input("Enter the number of people you want to add\n"))
for x in range(n):
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    name = input("Enter name {}\n".format(x+1))
    surname = input("Enter surname {}\n".format(x+1))
    number = input("Enter telephone number {}\n".format(x+1))
    cur.execute("INSERT INTO PhoneBook(name, surname, number) VALUES(%s,%s,%s) RETURNING id;", (name, surname, number))
    print("Your ID is", cur.fetchone()[0])
    cur.close()
    conn.commit()
    conn.close()