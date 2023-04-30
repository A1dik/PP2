import psycopg2
from config import config
w_name = input("Write your name\n")
w_surname = input("Write your surname\n")
w_number = input("Write your number\n")
params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()
cur.callproc('checks', (w_name, w_surname))
if cur.fetchone()[0] == 0:
    cur.execute('CALL insert(%s,%s,%s)', (w_name, w_surname, w_number))
else: 
    cur.execute('CALL update(%s,%s,%s)', (w_name, w_surname, w_number))
conn.commit()
cur.close()
conn.close()