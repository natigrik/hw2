import csv
import json

from csv import DictReader

with open('users.json', "r") as u:
    users = json.loads(u.read())
users_list = users

books = []
readers = []

with open('books.csv', "r") as reader_with_max_book_count:
    books_list = DictReader(reader_with_max_book_count)
    total_rows = 0

    for row in books_list:
        book = {x: row.get(x) for x in ('Title', 'Author', 'Pages', 'Genre')}
        books.append(book)
        total_rows += 1

    reader_min_book_count = int(total_rows / len(users))
    reader_with_max_book_count = total_rows % len(users)

    i = 0
    book_number = 0
    for user in users_list:
        reader = {x: users[i].get(x) for x in ('name', 'gender', 'address', 'age')}
        reader['books'] = []

        if i < reader_with_max_book_count:
            for j in range(reader_min_book_count + 1):
                reader['books'].append(books[book_number])
                book_number += 1

        elif reader_with_max_book_count <= i < len(users):
            for j in range(reader_min_book_count):
                reader['books'].append(books[book_number])
                book_number += 1

        else:
            print("что-то пошло не так!")
            break

        readers.append(reader)
        i += 1

print(readers)
with open("result.json", "w") as r:
    json.dump(readers, r)
