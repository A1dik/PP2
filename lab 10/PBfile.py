import psycopg2
from config import config
params = config()
f = open("data.csv", "r")
while True:
    line = f.readline()
    if line == "":
        break
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    p_list = line.split()
    cur.execute("INSERT INTO PhoneBook(name, surname, number) VALUES(%s,%s,%s) RETURNING id;", (p_list[0], p_list[1], p_list[2]))
    print(p_list[0], p_list[1], "- your ID is", cur.fetchone()[0])
    cur.close()
    conn.commit()
    conn.close()