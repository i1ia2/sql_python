import psycopg2

with psycopg2.connect(database="postgres", user="postgres", password="153268425Zz", host='localhost') as conn:
    with conn.cursor() as cur:

            cur.execute("""
                    DROP TABLE info;
                        """)
            cur.execute('''
                    CREATE TABLE info(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(40),
                        surname VARCHAR(60),
                        email VARCHAR(120),
                        phone bigint);''')
            conn.commit()
            def creat_db(conn):
                cur.execute("""
                        INSERT INTO course(name, surname, email, phone) VALUES(f''{name}', '{surname}', '{email}','{phone}'');
                        """)
                conn.commit()

            def creat_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
                with conn.cursor() as cur:
                    name = input('Введите имя: ' )
                    surname = input('Введите фамилию: ')
                    email = input('Введите email: ')
                    print("хотите оставить свой номер телефона?")
                    otvet = input('Да/Нет: '.lower())
                    if otvet == ('да'):
                        phone = input('Введите номер телефона: ')
                        cur.execute(
                            f"INSERT INTO info(name, surname, email, phone) VALUES( '{name}', '{surname}', '{email}','{phone}');")
                        conn.commit()
                        return
                    cur.execute(
                        f"INSERT INTO info(name, surname, email) VALUES( '{name}', '{surname}', '{email}');")
                    conn.commit()


creat_db(conn)
conn.close()

