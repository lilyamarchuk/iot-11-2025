import logging
import csv
import os
from functools import wraps
import locale


class FileNotFound(Exception):
    pass


class FileCorrupted(Exception):
    pass


def logged(exception_type, mode="console"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if mode == "file":
                logging.basicConfig(
                    filename='operations.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s'
                )
            else:
                logging.basicConfig(
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s'
                )

            try:
                return func(*args, **kwargs)
            except exception_type as e:
                logging.error(f"Exception in {func.__name__}: {str(e)}")
                raise

        return wrapper

    return decorator


class CSVFileHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(filepath):
            raise FileNotFound(f"Файл {filepath} не знайдено")
        try:
            locale.setlocale(locale.LC_COLLATE, 'uk_UA.UTF-8')
        except:
            try:
                locale.setlocale(locale.LC_COLLATE, 'Ukrainian_Ukraine.1251')
            except:
                pass

    @logged(FileCorrupted, mode="console")
    def read(self):
        try:
            with open(self.filepath, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                return list(reader)
        except (IOError, csv.Error) as e:
            raise FileCorrupted(f"Файл пошкоджено або неможливо прочитати: {str(e)}")

    @logged(FileCorrupted, mode="console")
    def write(self, data):
        try:
            with open(self.filepath, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
        except (IOError, csv.Error) as e:
            raise FileCorrupted(f"Неможливо записати у файл: {str(e)}")

    @logged(FileCorrupted, mode="console")
    def append(self, data):
        try:
            with open(self.filepath, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
        except (IOError, csv.Error) as e:
            raise FileCorrupted(f"Неможливо дописати у файл: {str(e)}")

    def sort_by_name(self):
        data = self.read()
        if len(data) <= 1:
            return
        header = data[0]
        rows = data[1:]
        rows.sort(key=lambda x: locale.strxfrm(x[0].lower()))
        self.write([header] + rows)

    def calculate_average_age(self):
        data = self.read()
        if len(data) <= 1:
            return 0
        ages = [int(row[1]) for row in data[1:]]
        return sum(ages) / len(ages)

    def add_person(self, name, age):
        self.append([[name, age]])
        self.sort_by_name()


if __name__ == "__main__":
    with open('test.csv', 'w', encoding='utf-8') as f:
        f.write('Ім\'я,Вік\nІван,25\n')

    handler = CSVFileHandler('test.csv')

    content = handler.read()
    print(f"Початковий вміст: {content}")

    handler.add_person('Марія', '30')
    handler.add_person('Петро', '28')
    handler.add_person('Анна', '22')


    content = handler.read()
    print(f"Відсортований список: {content}")

    avg_age = handler.calculate_average_age()
    print(f"Середній вік: {avg_age:.2f}")

    try:
        bad_handler = CSVFileHandler('неіснуючий.csv')
    except FileNotFound as e:
        print(f"Помилка: {e}")