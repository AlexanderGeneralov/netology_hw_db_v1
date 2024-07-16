import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale

db = 'postgres'
db_password = 'secret'
host_type = 'localhost'
host = '5432'
db_name = 'test'

DSN = f"postgresql://{db}:{db_password}@{host_type}:{host}/{db_name}"
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

# function to fill tables in db from json file
def fill_tables(db_session):

    with open('tests_data.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        db_session.add(model(id=record.get('pk'), **record.get('fields')))
    db_session.commit()

# function to select informaton of book sale
def select_query(publisher_name='O’Reilly'):

    q = session.query(Book).with_entities(Book.title, Shop.name, Sale.price, Sale.date_sale) \
        .join(Publisher, Publisher.id == Book.id_publisher) \
        .join(Stock, Stock.id_book == Book.id) \
        .join(Sale, Sale.id_stock == Stock.id) \
        .join(Shop, Shop.id == Stock.id_shop) \
        .filter(Publisher.name == publisher_name).all()
    for s in q:
        print(s.title, s.name, s.price, s.date_sale.strftime("%d-%m-%Y"))


if __name__ == '__main__':

    create_tables(engine)
    fill_tables(session)
    select_query()
