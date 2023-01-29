import psycopg2
def create_db(cur):

        cur.execute('''
                        CREATE TABLE info(
                               PersonId SERIAL PRIMARY KEY,
                               name VARCHAR(40),
                               surname VARCHAR(60),
                               email VARCHAR(120)
                               );''')
        cur.execute('''
                        CREATE TABLE phone_client( 
                            PersonId SERIAL ,
                            Foreign key (PersonId) references info(PersonId),
                            phone TEXT
                            );''')

def creat_client(cur, name=None, surname=None, email=None, phone=None):

        cur.execute("""INSERT INTO info(name, surname, email) VALUES(%s,%s,%s);""",
                    (name, surname, email,))

        cur.execute("""INSERT INTO phone_client(phone) VALUES(%s);""",
                    (phone,))

def add_phone(cur, PersonId, phone=None):
        cur.execute("""INSERT INTO phone_client(PersonId,phone) VALUES(%s,%s);""",
                    (PersonId, phone,))


def change_client(cur, PersonId, name=None, surname=None, email=None, phone=None):
    cur.execute("""
           UPDATE info
               SET name=%s, surname=%s, email=%s
               WHERE (PersonId=%s) 
       """, (name, surname, email, PersonId,))
    cur.execute("""
            UPDATE phone_client
                SET phone=%s
                WHERE PersonId=%s 
        """, (PersonId, phone))

def change_client_name(cur, PersonId, name=None):
    cur.execute("""
           UPDATE info
               SET name=%s
               WHERE (PersonId=%s) 
       """, (name, PersonId,))
def change_client_surname(cur, PersonId, surname=None):
    cur.execute("""
           UPDATE info
               SET surname=%s
               WHERE (PersonId=%s) 
       """, (surname, PersonId,))

def change_client_email(cur, PersonId, email=None):
        cur.execute("""
            UPDATE info
               SET email=%s
               WHERE (PersonId=%s) 
           """, (email, PersonId,))
def change_client_phone(cur, PersonId, phone=None):
    cur.execute("""
                UPDATE phone_client
                    SET phone=%s
                    WHERE PersonId=%s 
            """, (PersonId, phone))


def delete_client(cur, PersonId):
        cur.execute("""
            DELETE FROM info WHERE PersonId=%s;
        """, (PersonId,))

def find_client(cur, **kwargs):
    str = ' or '.join([f"{x} = '{y}'" for x, y in kwargs.items() if y])
    cur.execute("""
        SELECT name, surname, email, phone FROM info i
        JOIN phone_client p on i.PersonId = p.PersonId
        WHERE """ + str)
    print(f"Информация о клиенте {cur.fetchall()}")
# def find_client(cur, name=None, surname=None, email=None, phone=None):
#     cur.execute("""
#             SELECT name, surname, email, phone FROM info i
#             JOIN phone_client p on i.PersonId = p.PersonId
#             WHERE name  IN (%s)
#             """, (name, ))
#     print(cur.fetchone())


#Удаление телефона
def delete_phone(cur, PersonId, phone=None):
        cur.execute("""
            DELETE FROM phone_client
            WHERE (personId=%s) and (phone=%s)
        """, (PersonId, phone, ))

def drop_table(cur):
        cur.execute("""
         DROP TABLE phone_client;
                    DROP TABLE info;
                    """)
if __name__ == "__main__":
    with psycopg2.connect(database="postgres", user="postgres", password="153268425Zz", host='localhost') as conn:
            print('''Вы можете: 
                Функция 1 создающая структуру БД (таблицы)
                Функция 2 позволяющая добавить нового клиента
                Функция 3 позволяющая добавить телефон для существующего клиента
                Функция 4 позволяющая изменить данные о клиенте
                Функция 5 позволяющая удалить телефон для существующего клиента
                Функция 6 позволяющая удалить существующего клиента
                Функция 7 позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
                Функция 8 позволяющая удалить БД (таблицы)''')

            comanda = int(input("Выберите функцию: "))
            with conn.cursor() as cur:
                if comanda == 1:
                    create_db(cur)

                elif comanda == 2:
                    creat_client(cur, name=input("Введите имя: "), surname=input("Введите Фамилию: ")
                                 , email=input("Введите емайл: "), phone=input("Введите телефон: "))

                elif comanda == 3:
                    add_phone(cur, PersonId=input('Введите номер клиента: '), phone=input('Введите номер: '))

                elif comanda == 7:
                    find_client(cur, name=input("Введите имя: ").title(), surname=input("Введите Фамилию: "),
                                  email=input("Введите емайл: "), phone=input("Введите Телефон: "))

                elif comanda == 4:
                    print("Какое поле вы хотите изменить ?")
                    pole = input("Имя/Фамилию/Емаил/Телефон или все?").lower()
                    if pole == ("все"):
                        change_client(cur, PersonId=input("id: "), name=input("Введите имя: "),
                                           surname=input("Введите Фамилию: "), email=input("Введите емайл: ")
                                           , phone=input("Введите Телефон: "))
                    if pole == ("имя"):
                        change_client_name(cur, PersonId=input("id: "), name=input("Введите имя: "))
                    if pole == ("фамилию"):
                        change_client_surname(cur, PersonId=input("id: "),surname=input("Введите Фамилию: "))
                    if pole == ("email"):
                        change_client_email(cur, PersonId=input("id: "), email=input("Введите емайл: "))

                elif comanda == 6:
                    delete_client(cur, PersonId=input("Введите id клиента"))

                elif comanda == 5:
                    delete_phone(cur, PersonId=input("Введите id клиента телефон которого хотите "
                                                      " которого хотите удалить "),
                                 phone=str(input("Введите телефон который хотите удалить")))

                elif comanda == 8:
                    drop_table(cur)


conn.close()



