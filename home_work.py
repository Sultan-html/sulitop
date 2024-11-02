import sqlite3


def create_database():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_book(title, author, year):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (title, author, year)
        VALUES (?, ?, ?)
    ''', (title, author, year))
    conn.commit()
    conn.close()


create_database()

add_book("История Кыргызстана", "К.М. Мырзамидинович", 1980)
add_book("География","В.И. Михайлович",2012)
add_book("Всемирная история", "И.М. Сергеевич", 1923)



def find_book_by_title(title):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM books WHERE title = ?
    ''', (title,))
    book = cursor.fetchone()
    conn.close()
    
    if book:
        return book 
    else:
        return None


result = find_book_by_title("UFC")
if result:
    print(f"Книга найдена: {result}")
else:
    print("Книга не найдена.")
    
    
def update_book_year(title, new_year):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE books
        SET year = ?
        WHERE title = ?
    ''', (new_year, title))
    conn.commit()
    conn.close()
update_book_year("История Кыргызстана",
                 1980)




def delete_book_by_id(book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM books
        WHERE id = ?
    ''', (book_id,))
    conn.commit()
    conn.close()

delete_book_by_id(1)
