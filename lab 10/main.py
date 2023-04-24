import psycopg2
import csv

contacts = []


def display_contacts_list():
    if len(contacts) > 0:
        with open('output.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(contacts)

        print('Contacts: ')

        for c in contacts:
            print(f'{c[0]}. {c[1]} {c[2]}, {c[3]}')

        print('-' * 100)
        print('You can also see list of contacts in output.csv file')
    else:
        print('Contacts not found!')


def list_contacts():
    global contacts
    sql = 'select * from contacts order by id asc'

    cursor.execute(sql)
    contacts = cursor.fetchall()

    display_contacts_list()


connection = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='46390',
    database='phone_book'
)

cursor = connection.cursor()
choice = None


def find_contact_by_id(id: int):
    global contacts

    for contact in contacts:
        if contact[0] == id:
            return contact


while True:
    choice = input('1 list all cont\n'
                   '2 import cont from input.csv \n'
                   '3 add new contact\n'
                   '4 update info\n'
                   '5 search contact\n'
                   '6 delete contact\n'
                   '0 exit\n')

    if choice == '1':
        list_contacts()

    elif choice == '2':

        sql = 'insert into contacts (name, surname, phone_number) values '
        with open('input.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')

        counter = 0

        for row in reader:
            counter += 1
            sql += f'(\'{row[0]}\', \'{row[1]}\', \'{row[2]}\'),'  # (name, surname, phone_number)

        sql = sql[:-1]  # we need to delete last , from sql syntax
        sql += ';'  # we add ; to the end of sql syntax

        cursor.execute(sql)
        connection.commit()

        print(f'{counter} contacts have successfully been saved!')

    elif choice == '3':
        name = input('name: ')
        surname = input('surname: ')
        phone_number = input('phone_number: ')

        sql = f'insert into contacts (name, surname, phone_number) values (\'{name}\', \'{surname}\', \'{phone_number}\');'

        cursor.execute(sql)
        connection.commit()

        print('Contact has been successfully be saved!')

    elif choice == '4':
        list_contacts()

        id = int(input('Write id of contact which you you to change: '))
        chosen_contact = find_contact_by_id(id)
        name = chosen_contact[1]
        surname = chosen_contact[2]
        phone_number = chosen_contact[3]

        if input('Do you want to change name? [y/n]\n') == 'y':
            name = input('new name: ')
        if input('Do you want to change surname? [y/n]\n') == 'y':
            surname = input('new surname: ')

        if input('Do you want to change phone number? [y/n]\n') == 'y':
            phone_number = input('new phone number: ')

        sql = f'update contacts set name=\'{name}\', surname=\'{surname}\', phone_number=\'{phone_number}\' where id={id}'
        cursor.execute(sql)
        connection.commit()
        print('Contact info has successfully been updated!')

    elif choice == '5':
        choice_1 = input('1 TO SEARCH CONTACT BY NAME\n'
                         '2 TO SEARCH CONTACT BY SURNAME\n')

        part_of_statement = f'{"sur" if choice_1 == "2" else ""}name'

        parameter = input(f'Insert {part_of_statement}: ')

        sql = f'select * from contacts where {part_of_statement}=\'{parameter}\''

        cursor.execute(sql)
        contacts = cursor.fetchall()

        display_contacts_list()

    elif choice == '6':
        choice_1 = input('1 TO SEARCH CONTACT BY NAME\n'
                         '2 TO SEARCH CONTACT BY SURNAME\n'
                         '3 TO SEARCH CONTACT BY PHONE NUMBER\n')

        part_of_statement = "phone_number" if choice_1 == "3" else "surname" if choice_1 == "2" else "name"
        parameter = input(f'Insert {part_of_statement}: ')

        sql = f'select * from contacts where {part_of_statement}=\'{parameter}\''

        cursor.execute(sql)
        contacts = cursor.fetchall()

        id = None

        if len(contacts) == 0:
            print('Contact not found!')
        else:
            if len(contacts) > 1:
                display_contacts_list()
                id = int(input(f'Insert the id of contact which you are planning to delete: '))

            else:
                if input(f'Are you sure to delete {contacts[0][1]} {contacts[0][1]}?[y/n]') == 'y':
                    id = contacts[0][0]
            sql = f'delete from contacts where id={id}'
            cursor.execute(sql)
            connection.commit()
            print('Contact has successfully been deleted!')


    elif choice == '0':
        break

    print('=' * 120)


cursor.close()
connection.close()