import random

from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from typing import Optional

from models.buy_book import BuyBook
from models.database import DATABASE_URL
from models.genre import Genre
from models.author import Author
from models.city import City
from models.book import Book
from models.client import Client
from models.buy import Buy
from models.step import Step
from models.buy_step import BuyStep


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()


def create_data() -> None:
    """
    Создает и заполняет таблицы базы данных случайными данными.

    Заполняет таблицы:
    - Genre
    - Author
    - City
    - Book
    - Client
    - Buy
    - Step
    - BuyBook
    - BuyStep

    :raises Exception: Если возникает ошибка при добавлении данных в сессию.
    """
    # Количество записей для добавления
    num_genres: int = 10
    num_authors: int = 10
    num_cities: int = 5
    num_books: int = 50
    num_clients: int = 20
    num_buys: int = 30
    num_steps: int = 5

    try:
        # Заполнение таблицы genre
        genres = [Genre(name_genre=fake.word()) for _ in range(num_genres)]
        session.add_all(genres)

        # Заполнение таблицы author
        authors = [Author(name_author=fake.name()) for _ in range(num_authors)]
        session.add_all(authors)

        # Заполнение таблицы city
        cities = [City(name_city=fake.city(), days_delivery=random.randint(1, 10)) for _ in range(num_cities)]
        session.add_all(cities)

        # Заполнение таблицы book
        books = [
            Book(
                title=fake.sentence(nb_words=3),
                author_id=random.randint(1, num_authors),
                genre_id=random.randint(1, num_genres),
                price=round(random.uniform(5, 50), 2),
                amount=random.randint(1, 100)
            ) for _ in range(num_books)
        ]
        session.add_all(books)

        # Заполнение таблицы client
        clients = [
            Client(
                name_client=fake.name(),
                city_id=random.randint(1, num_cities),
                email=fake.email()
            ) for _ in range(num_clients)
        ]
        session.add_all(clients)

        # Заполнение таблицы buy
        buys = [Buy(buy_description=fake.sentence(), client_id=random.randint(1, num_clients)) for _ in range(num_buys)]
        session.add_all(buys)

        # Заполнение таблицы step
        steps = [Step(name_step=f"Step {step + 1}") for step in range(num_steps)]
        session.add_all(steps)

        # Заполнение таблицы buy_book
        buy_books = [
            BuyBook(
                buy_id=random.randint(1, num_buys),
                book_id=random.randint(1, num_books),
                amount=random.randint(1, 5)
            ) for _ in range(num_buys)
        ]
        session.add_all(buy_books)

        # Заполнение таблицы buy_step
        buy_steps = [
            BuyStep(
                buy_id=random.randint(1, num_buys),
                step_id=random.randint(1, num_steps),
                date_step_beg=fake.date_time_this_year(),
                date_step_end=fake.date_time_this_year()
            ) for _ in range(num_buys)
        ]
        session.add_all(buy_steps)

        # Сохранение всех изменений в базе данных
        session.commit()

    except Exception as e:
        print(f"Произошла ошибка при добавлении данных: {e}")
        session.rollback()  # Откатить изменения в случае ошибки

    finally:
        # Закрытие сессии
        session.close()
