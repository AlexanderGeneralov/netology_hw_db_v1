import psycopg2


# decorator function to wrap sql query string with cursor context manager to implement sql query
def db_decorator_func(func):
    def wrapper():
        with psycopg2.connect(database="test", user="postgres", password="secret") as conn:
            with conn.cursor() as cur:
                cur.execute(func())
                conn.commit()

    return wrapper


# decorator function to wrap sql query string with cursor context manager to implement sql query, returns fetchall
def db_decorator_fetch_func(func):
    def wrapper():
        with psycopg2.connect(database="test", user="postgres", password="secret") as conn:
            with conn.cursor() as cur:
                cur.execute(func())
                print(cur.fetchall())

    return wrapper


# function returns sql query string to create table with client data
@db_decorator_func
def create_table_client():
    sql = (
        "CREATE TABLE IF NOT EXISTS client("
        "client_id SERIAL PRIMARY KEY, "
        "first_name VARCHAR(40) NOT NULL, "
        "second_name VARCHAR(40) NOT NULL, "
        "email VARCHAR(40) NOT NULL);"
    )
    return sql


# function returns sql query string to create cable with phone data
@db_decorator_func
def create_table_phone():
    sql = (
        "CREATE TABLE IF NOT EXISTS phone("
        "phone_id SERIAL PRIMARY KEY, "
        "phone_number INTEGER NOT NULL, "
        "client_id INTEGER REFERENCES client(client_id));"
    )
    return sql


# function returns sql query string to add client data
@db_decorator_func
def add_client_data():
    first_name = str(input('Input client first name: '))
    second_name = str(input('Input client second name: '))
    email = str(input('Input client email: '))
    sql = (
        "INSERT INTO client(first_name, second_name, email) "
        f"VALUES('{first_name}', '{second_name}', '{email}');"
    )
    return sql


# function returns sql query string to add phone number date
@db_decorator_func
def add_phone_number():
    client_id = int(input('Input client id: '))
    phone_number = int(input('Input phone number: '))
    sql = (
        "INSERT INTO phone (phone_number, client_id) "
        f"VALUES({phone_number}, {client_id});"
    )
    return sql


# function returns sql query string to change client data
@db_decorator_func
def change_client_data():
    client_id = int(input('Input client ID: '))
    first_name = str(input('Input new client first name: '))
    second_name = str(input('Input new client second name: '))
    email = str(input('Input new client email: '))
    sql = (
        "UPDATE client "
        "SET "
        f"first_name = '{first_name}', "
        f"second_name = '{second_name}', "
        f"email = '{email}' "
        f"WHERE client_id = {client_id};"
    )
    return sql


# function returns sql query string to delete phone number data by client ID
@db_decorator_func
def del_phone_number():
    client_id = int(input('Input client ID: '))
    sql = (
        "DELETE FROM phone "
        f"WHERE client_id = {client_id};"
    )
    return sql


# function returns sql query string to delete client data by client ID
@db_decorator_func
def del_client_data():
    client_id = int(input('Input client ID: '))
    sql = (
        "DELETE FROM client "
        f"WHERE client_id = {client_id};"
    )
    return sql


# function returns sql query string to search client information by client phone number
@db_decorator_fetch_func
def client_search():
    phone_number = int(input('Input client phone number for search: '))
    sql = (
        "SELECT * FROM client "
        "JOIN phone ON client.client_id = phone.client_id "
        f"WHERE phone_number = {phone_number};"
    )
    return sql

# create_table_client() # check+, work+
# create_table_phone() # check+, work+
# add_client_data() # check+, work+
# add_phone_number() # check+, work+
# change_client_data() # check+, work+
# client_search() # check+, work+
# del_phone_number() # check+, work+
# del_client_data() # check+, work+
