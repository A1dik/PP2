import psycopg2
from config import config
w_name = input("Write the pattern of the required name\n")
# _smth%; % if any
w_surname = input("Write the pattern of the required surname\n")
w_number = input("Write the pattern of the required number\n")
params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()
cur.callproc('pattern', (w_name, w_surname, w_number))
text = cur.fetchall()
print(text)
cur.close()
conn.close()