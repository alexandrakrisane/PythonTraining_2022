# 15. 13.04.2022

import sqlite3
from sqlite3 import Error


dbpath = "C:\Temp\chinook.db"


def create_connection(dbpath):
    try:
        conn = sqlite3.connect(dbpath)
        # print("sqlite3 version: {}".format(sqlite3.version))
        # print("Connected to database: {}".format(dbpath))
        return conn
    except Error as e:
        print(e)
        return None


connection = create_connection(dbpath)


def create_artist(conn, artist_name):
    sql = ''' INSERT INTO artists(name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (artist_name,))
    conn.commit()
    cur.close()
    return cur.lastrowid


# create_connection(dbpath)

def read_artists(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM artists ORDER BY ArtistId DESC")  # added DESC for testing purpose
    artists = cur.fetchall()
    cur.close()
    return artists


# print(read_artists(conn=create_connection(dbpath)))

def update_artist(id, new_name):
    conn = create_connection(dbpath)
    cur = conn.cursor()
    if id not in read_artists(conn):
        print("Artist with id {} does not exist".format(id))
        return cur.close()
    else:
        cur.execute("UPDATE artists SET name = ? WHERE ArtistId = ?", (new_name, id))
        conn.commit()
    cur.close()
    return cur.rowcount  # return number of rows updated


def delete_artist(id=None, name=""):
    conn = create_connection(dbpath)
    cur = conn.cursor()
    if id:
        cur.execute("DELETE FROM artists WHERE ArtistId = ?", (id,))
        conn.commit()
    elif name:
        cur.execute("DELETE FROM artists WHERE name = ?", (name,))
        conn.commit()
    elif id and name:
        cur.execute("DELETE FROM artists WHERE name = ? and ArtistID = id", (name,id))
        conn.commit()
    else:
        print("No id or name provided")
        return cur.close()
    cur.close()
    return cur.rowcount


create_connection(dbpath)


print(read_artists(connection))
#
# create_artist(connection, artist_name="test")
# print(read_artists(connection))
#
# print(update_artist(id=288, new_name="New Name1"))
# print(read_artists(connection))

# print(delete_artist(id=288))
# print(read_artists(connection))

# print(delete_artist(name="New Name1"))
# print(read_artists(connection))

print(delete_artist(id=288, name="test"))
print(read_artists(connection))

connection.close()