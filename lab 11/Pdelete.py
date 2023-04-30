import psycopg2
from config import config
w_name = input("Write your name\n")
w_surname = input("Write your surname\n")
params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()
cur.execute('CALL delete(%s,%s)', (w_name, w_surname))
conn.commit()
cur.close()
conn.close()