import psycopg2
from config import config
params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()
cur.execute("""CREATE TABLE PhoneBook(
    id SERIAL PRIMARY KEY, name VARCHAR(20) NOT NULL, surname VARCHAR(20) NOT NULL, number VARCHAR(20) NOT NULL)""")
cur.close()
conn.commit()
conn.close()