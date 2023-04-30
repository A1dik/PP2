import psycopg2
from config import config
answer = input("Do you really want to delete your number?\n")
if answer == "yes" or answer == "Yes":
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    id = input("Write your id\n")
    cur.execute("DELETE FROM PhoneBook WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()