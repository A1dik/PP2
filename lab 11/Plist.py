import psycopg2
from config import config
f = open('data.txt', 'r')
line = f.readline()
while line != "":
    data = line.split()
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.callproc('checks', (data[0], data[1]))
        if cur.fetchone()[0] == 0:
            cur.execute('CALL insert(%s,%s,%s)', (data[0], data[1], data[2]))
        else: 
            cur.execute('CALL update(%s,%s,%s)', (data[0], data[1], data[2]))
        conn.commit()
        cur.close()
        conn.close()
    except:
        print(data, "has incorrect format")
    line = f.readline()