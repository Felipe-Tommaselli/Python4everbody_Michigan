# DATA MODELS AND RELATIONAL SQL

#! Data Modeling

# evitar repetir dados em linhas e colunas relacionando tabelas

#?                                          --------        ---------
#?  ------------------------------   ----> | Album | ----> | Artist |
#? | Traking, Rating, Len, Count | -|      ========        ---------
#? ------------------------------   ----> | Genre |
#?                                        --------

# the ---> means "belongs-to"
# Traking, Rating, Len, Count are attributes of the song title

#* when using databases and a lot of tables we use ids to identifie,
#* one id for the track, other for the  album, we now add a album_id in 
#* the track attributes that points to the album, we should also add 
#* one key to the genre table

#*          
#*     --------              --------
#*    | Track |             | Album |
#*    --------              --------                ---------
#*    [ id ]                [ id ]  -------------> | Artist |
#*    [ title ]          ->  [ title ]             ---------
#*    [ rating ]        |   [ artist_id ]          [ id ]
#*    [ len ]          |           --------        [ name ]
#*    [ count ]       |        -> | Genre |
#*    [ album_id ] ---o       |   --------
#*    [ genre_id ] ----------o    [ id ]
#*                                [ name ]

# CREATING TABLES WITH THE PRIMARY KEY (ID)

#? CREATE TABLE Genre(
#?       id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#?       name    TEXT
#? )

#* w/ the album we use de foreign key to be pointed by the track table

#? CREATE TABLE Album(
#?       id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#?       artist_id INTEGER,
#        title    TEXT
#? )

#* same w/ the track

#?  CREATE TABLE Track(
#?	    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#?	    title	TEXT,
#?	    artist_id INTEGER,
#?	    genre_id INTEGER,
#?	    len INTEGER, rating INTEGER, count INTEGER
#? )

# ! Inserindo informações

#? INSERT into Artist (name) values ('Mc Poze do rodo')

#? INSERT into Genre (name) values ('Rock');
#? INSERT into Genre (name) values ('Funk')

#? INSERT into Album (title, artist_id) values ('Who made Who', 1);
#? INSERT into Album (title, artist_id) values ('Pitbull do funk', 2)

#? INSERT into Track(title, rating, len, count, artist_id, genre_id) 
#?	values ('Black dog', 5, 297, 0, 1, 1);
#? INSERT into Track(title, rating, len, count, artist_id, genre_id) 
#?	values ('Stairway', 5, 482, 0, 1, 1);
#? INSERT into Track(title, rating, len, count, artist_id, genre_id) 
#?	values ('To voando alto', 5, 313, 0, 2, 2);
#? INSERT into Track(title, rating, len, count, artist_id, genre_id) 
#?	values ('Fica a vontade', 5, 207, 0, 2, 2)

#! Reconstructing data w/ JOIN

# JOIN links across several tables as part of a select operation

"""
SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id
#!     ----------v--------------     ----v-    -v-----    ---------------v-----------
          What we want to see    The tables that hold the data    How the tables are linked

"""
# pointing the artist id from album to the artist id himself

"""
SELECT Track.title, Genre.name FROM Track JOIN Genre ON Track.genre_id = Genre.id;

SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Artist
    ON Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id = Artist.id

"""
