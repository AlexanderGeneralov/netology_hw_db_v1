import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale

db = 'postgres'
db_password = 'dacent0000'
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
def select_query(user_input):

    q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale) \
        .select_from(Shop) \
        .join(Stock, Shop.id == Stock.id_shop) \
        .join(Book, Stock.id_book == Book.id) \
        .join(Publisher, Book.id_publisher == Publisher.id) \
        .join(Sale, Stock.id == Sale.id_stock)

    if user_input.isdigit():
        records = q.filter(Publisher.id == user_input).all()
    else:
        records = q.filter(Publisher.name == user_input).all()

    for book_title, shop_name, sale_price, date_sale in records:
        print(f"{book_title : <40} | {shop_name : <10} | {sale_price : <8} | {date_sale.strftime('%d-%m-%Y')}")


#    This query works as well, but i do not completely understand how to join table via backref...
#
#    q = session.query(Publisher).with_entities(Publisher.name, Book.title, Shop.name, Sale.price, Sale.date_sale) \
#        .join(Book.publisher) \
#        .join(Book.stocks) \
#        .join(Stock.sales) \
#        .join(Stock.shop) \
#        .filter(Publisher.name == publisher_name).all()
#    for s in q:
#        print(s.title, s.name, s.price, s.date_sale.strftime("%d-%m-%Y"))


if __name__ == '__main__':

    create_tables(engine)
    fill_tables(session)

    user_input = input('Input publisher name or ID: ')
    select_query(user_input)
