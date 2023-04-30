import psycopg2
from config import config
how_many = input("Write how many records you want to see\n")
how_far = input("Write how many records you want to skip (from which to start)\n")
params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()
cur.callproc('query', (how_many, how_far))
text = cur.fetchall()
print(text)
cur.close()
conn.close()
