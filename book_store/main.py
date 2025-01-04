from models.database import create_db, drop_db
from create_data import create_data


print('Начинаем работу с базой данных book_store')
drop_db()
create_db()
print('Таблицы успешно созданы')
create_data()
print("Данные успешно добавлены во все таблицы.")
