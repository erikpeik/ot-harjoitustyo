from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists results;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table results (
            id integer primary key autoincrement,
            time integer not null,
            difficulty integer not null,
            date text not null
        );
    ''')

    connection.commit()


def initialize_database():
    print("Initializing database...")
    connection = get_database_connection()

    print("Dropping tables...")
    drop_tables(connection)

    print("Creating tables...")
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
