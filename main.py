import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute('''
                     CREATE TABLE info(
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(40),
                            surname VARCHAR(60),
                            email VARCHAR(120),
                            phone text);''')

def creat_client(conn, id, name=None, surname=None, email=None, phones=None):
    with conn.cursor() as cur:
        name = "Aex"
        surname = "pai"
        email = "2"
        phone = "+79995999444"
        cur.execute(
            f"INSERT INTO info( name, surname, email, phone) VALUES('{name}', '{surname}', '{email}',"
            f"'{phone}');")


def add_phone(conn, id, phone=None):
    with conn.cursor() as cur:
        cur.execute("""
            UPDATE info 
                SET phone = CONCAT(phone, '+89 96 345')
                WHERE id = 1
        """)

def change_client(conn, id, name=None, surname=None, email=None, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
               UPDATE info 
                   SET name = 'pasdkol', surname = 'hopsin', email = 'leps@mail.ru', phone = '' 
                   WHERE id = 1
           """)

def delete_client(conn):
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM info WHERE ID = 1;
        """)

def find_client(conn, name=None, surname=None, email=None, phone=None):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, name, surname, email, phone FROM info 
            WHERE name LIKE '%pasdkol%'
            """)
        print(cur.fetchone())

#Удаление телефона
def delete_phone(conn, id, phone=None):
    with conn.cursor() as cur:
        cur.execute("""
            UPDATE info 
                SET phone = ''
                WHERE id = '1'
        """)

def drop_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
                    DROP TABLE info;
                    """)

with psycopg2.connect(database="postgres", user="postgres", password="", host='localhost') as conn:
    # create_db(conn)
    # creat_client(conn, id, name=None, surname=None, email=None, phones=None)
    # find_client(conn, name=None, surname=None, email=None, phone=None)
    # change_client(conn, id, name=None, surname=None, email=None, phones=None)
    # delete_client(conn)
    # delete_phone(conn, id, phone=None)
    # add_phone(conn, id, phone=None)
    # drop_table(conn)

conn.close()



