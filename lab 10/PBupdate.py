import psycopg2
from config import config
params = config()
sql1 = "UPDATE PhoneBook SET name = %s WHERE id = %s"
sql2 = "UPDATE PhoneBook SET surname = %s WHERE id = %s"
sql3 = "UPDATE PhoneBook SET number = %s WHERE id = %s"
id = int(input("Enter your ID\n"))
conn = psycopg2.connect(**params)
cur = conn.cursor()
answer = input("Do you want to change your name?\n")
if answer == "yes" or answer == "Yes":
    name = input("Write your name\n")
    cur.execute(sql1, (name, id))
answer = input("Do you want to change your surname?\n")
if answer == "yes" or answer == "Yes":
    surname = input("Write your surname\n")
    cur.execute(sql2, (surname, id))
answer = input("Do you want to change your telephone number?\n")
if answer == "yes" or answer == "Yes":
    number = input("Write your number\n")
    cur.execute(sql3, (number, id))
cur.close()
conn.commit()
conn.close()