import psycopg2
from config import config
params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()
cur.execute("CREATE TABLE Snake(name VARCHAR(20) NOT NULL, score INTEGER NOT NULL, level INTEGER NOT NULL)""")
cur.close()
conn.commit()
conn.close()