import psycopg2
from config import config
sql = "SELECT {0} FROM PhoneBook {1}"
what = input("What do you want to see?\n")
# id, name, surname, number
where = ""
answer = input("Do you want to add any filters?\n")
if answer == "yes" or answer == "Yes":
    case = input("Create your filter\n")
    # smth and smth or smth; names, surnames and numbers in ''
    where = "WHERE " + case
params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()
cur.execute(sql.format(what, where))
text = cur.fetchall()
print(text)
cur.close()
conn.close()