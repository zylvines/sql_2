import psycopg2

connection = psycopg2.connect(
    database = 'sql_1',
    user = 'postgres',
    password = 123,
    host = 'localhost',
    port = 5432
)

cursor = connection.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS person(
#         id serial primary key,
#         full_name varchar(100)
#
# );
# """)

# cursor.execute("""INSERT INTO person(full_name)
# values('john doe')
# """)
#
# connection.commit()
# cursor.close()
# connection.close()
# print("brat ishlab ketti")




def create_tables():
    """Creates User and Message tables in the database."""
    conn = psycopg2.connect("example.db")
    cursor = conn.cursor()

    # Create User table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')

    # Create Message table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Message (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES User (id)
        )
    ''')

    conn.commit()
    conn.close()

def create_user(name, email):
    """Inserts a new user into the User table."""
    conn = psycopg2.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO User (name, email) VALUES (?, ?)", (name, email))

    conn.commit()
    conn.close()

def get_users():
    """Fetches all users from the User table."""
    conn = psycopg2.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()

    conn.close()
    return users

def update_user(user_id, name=None, email=None):
    """Updates a user's information."""
    conn = psycopg2.connect("example.db")
    cursor = conn.cursor()

    if name:
        cursor.execute("UPDATE User SET name = ? WHERE id = ?", (name, user_id))
    if email:
        cursor.execute("UPDATE User SET email = ? WHERE id = ?", (email, user_id))

    conn.commit()
    conn.close()

def delete_user(user_id):
    """Deletes a user from the User table."""
    conn = psycopg2.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM User WHERE id = ?", (user_id,))

    conn.commit()
    conn.close()

def create_message(user_id, content):
    """Inserts a new message into the Message table."""
    conn = psycopg2.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Message (user_id, content) VALUES (?, ?)", (user_id, content))

    conn.commit()
    conn.close()

def get_messages():
    """Fetches all messages from the Message table."""
    conn = psycopg2.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Message")
    messages = cursor.fetchall()

    conn.close()
    return messages

def update_message(message_id, content):
    """Updates a message's content."""
    conn = psycopg2.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Message SET content = ? WHERE id = ?", (content, message_id))

    conn.commit()
    conn.close()

def delete_message(message_id):
    """Deletes a message from the Message table."""
    conn = psycopg2.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Message WHERE id = ?", (message_id,))

    conn.commit()
    conn.close()

# Example usage
if __name__ == "__main__":
    create_tables()
    create_user("John Doe", "john.doe@example.com")
    create_user("Jane Smith", "jane.smith@example.com")

    users = get_users()
    print("Users:", users)

    create_message(1, "Hello, world!")
    create_message(2, "Hi there!")

    messages = get_messages()
    print("Messages:", messages)

    update_user(1, name="John Updated")
    update_message(1, "Updated content")

    print("Updated Users:", get_users())
    print("Updated Messages:", get_messages())

    delete_message(2)
    delete_user(2)

    print("After Deletions - Users:", get_users())
    print("After Deletions - Messages:", get_messages())
