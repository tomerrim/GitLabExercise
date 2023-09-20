import sqlite3

DB_NAME = "gitlab_data.db"


# 3
def setup_database():
    """Set up the SQLite database with the necessary tables"""
    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()

    # Projects table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Projects (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    """)

    # Users table
    cursor.execute(""""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        UNIQUE(id)
    )
    """)

    # ProjectUsers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ProjectUsers (
        project_id INTEGER,
        user_id INTEGER,
        FOREIGN KEY (project_id) REFERENCES Projects(id),
        FOREIGN KEY (user_id) REFERENCES Users(id),
        UNIQUE(project_id, user_id)
    )
    """)

    con.commit()
    return con


def store_data_in_db(projects, users, project_users, con):
    """Store the extracted data into the database"""
    cursor = con.cursor()

    # Storing projects
    for project in projects:
        cursor.execute("")

    # Storing users
    for user in users:
        cursor.execute("")

    # Storing project users
    for project_user in project_users:
        cursor.execute("")

    con.commit()


def get_all_projects(con):
    """Retrieve all projects stored in the database."""
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Projects")
    return cursor.fetchall()


def get_all_users(con):
    """Retrieve all users stored in the database."""
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Users")
    return cursor.fetchall()


def get_users_for_project(con, project_id):
    """Retrieve all users associated with a specific project"""
    cursor = con.cursor()
    cursor.execute("""SELECT u.id, u.name
    FROM Users u
    JOIN ProjectUsers pu ON u.id = pu.user_id
    WHERE pu.project_id = ?
    """, (project_id,))
    return cursor.fetchall()
