# This application will read the mailbox data (mbox.txt)
# and count the number of email messages per organization using a database

import sqlite3


conn = sqlite3.connect("SQLMi.SQLMi.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (email TEXT, count INTERGER)")

fname = input("Enter File Name:")

if len(fname) < 1: fname = "mbox-short.txt"

fh = open(fname)

for line in fh:
    if "From: " not in line: continue
    items = line.split()
    emails = items[1]
    cur.execute("SELECT count FROM Counts WHERE email = ?", (emails,))
    row = cur.fetchone()
    # Fetchone() method is used when you want to select only the first row from the table.
    # This method only returns the first row from the SQL table.

    if row is None:
        cur.execute("INSERT INTO Counts (email, count) VALUES (?, 1)", (emails,))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ?", (emails,))
    
conn.commit()

sqlstr = cur.execute("SELECT * FROM Counts ORDER BY count DESC LIMIT 10")
# each row is a Python tuple

for row in sqlstr:
    print(str(row[0]), row[1])

cur.close()


##################################################################################

import sqlite3
import re

conn = sqlite3.connect("sql.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

fname = input("Enter Your File Name:")

if len(fname) < 1: fname = "mbox.txt"

fh = open(fname)

for line in fh:
    line = line.rstrip()
    orgs = re.findall("[a-zA-Z0-9]\S*@\S*[a-zA-Z]", line)

    for org in orgs:
        if org is None: continue

        organitations = re.findall("@(\S+)", org)

        cur.execute("SELECT count FROM Counts WHERE org = ? ", (organitations[0],))

        row = cur.fetchone()

    if row is None:
        cur.execute("INSERT INTO Counts (org, count) Values (?, 1)", (organitations[0],))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ? ", (organitations[0],))
conn.commit()

sqlstr = cur.execute("SELECT * FROM Counts ORDER BY count")

for r in sqlstr:
    print(str(r[0]), ":", r[1])

cur.close()

##################################################################################

import sqlite3

conn = sqlite3.connect('sql.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')

if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if "From: " not in line: continue

    pieces = line.split()
    org = pieces[1].split("@")[1]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES ( ?, 1 )', ( org,))
    else :
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()

sqlstr = cur.execute('SELECT * FROM Counts ORDER BY count DESC')


for row in sqlstr :
    print(str(row[0]), row[1])

cur.close()


# This application will read an iTunes export file in XML
# and produce a properly normalized database


import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        artist_id INTEGER
    );

    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Track (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        length INTEGER, rating INTEGER, count INTEGER
    );

''')

fname = input("Enter File Name: ")

if len(fname) < 1: fname = 'Library.xml'

def lookup(entry, key):
    found = False

    for child in entry:
        if found: return child.text

        if child.tag == 'key' and child.text == key:
            found = True
    return None


stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')

print('Dict count:', len(all))

for entry in all:

    if(lookup(entry, 'Track ID') is None): continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None or genre is None: 
        continue

    # print(name, artist, album, genre, count, rating, length)


    cur.execute('''
            INSERT OR IGNORE INTO Artist (name) VALUES (?)
    ''', (artist,))
    cur.execute('''
            SELECT id FROM Artist WHERE name = ?
    ''', (artist,))
    artist_id = cur.fetchone()[0]


    cur.execute('''
            INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)
    ''', (album, artist_id,))
    cur.execute('''
            SELECT id FROM Album WHERE title = ?
    ''', (album,))
    album_id = cur.fetchone()[0]


    cur.execute('''
            INSERT OR IGNORE INTO Genre (name) VALUES(?)
    ''', (genre,))
    cur.execute('''
            SELECT id FROM Genre WHERE name = ?
    ''', (genre,))
    genre_id = cur.fetchone()[0]


    cur.execute('''
            INSERT OR REPLACE  INTO Track (title, album_id, genre_id, length, rating, count) VALUES 
            (?, ?, ?, ?, ?, ?)
    ''', (name, album_id, genre_id, length, rating, count,))

conn.commit()
cur.close()



# This application will read roster data in JSON format,
# parse the file, and then produce an SQLite database that contains a
# User, Course, and Member table and populate the tables from the data file.

import json
import sqlite3

conn = sqlite3.connect("rosterdb.db")
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
        );

    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY(user_id, course_id)
    );

''')

fname = input("Enter File Name: ")
if len(fname) < 1: fname = 'roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    print(name, title)


    cur.execute('''
        INSERT OR IGNORE INTO User (name) VALUES ( ? )
    ''',(name,))
    cur.execute('''
        SELECT id FROM User WHERE name = ?
    ''', (name,))
    user_id = cur.fetchone()[0]



    cur.execute('''
        INSERT OR IGNORE INTO Course (title) VALUES ( ? )
    ''', (title,))
    cur.execute('''
        SELECT id FROM Course WHERE title = ?
    ''', (title,))
    course_id = cur.fetchone()[0]



    cur.execute('''
        INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)
    ''', (user_id, course_id, role,))


conn.commit()
cur.close()