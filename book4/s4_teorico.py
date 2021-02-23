# MANY-TO-MANY RELATIONSHIPS IN SQL

#! MANY-TO-MANY

# até agr só vimos one-to-many ou many-to-one relationships
#* um exemplo são diferentes livros que são escritos por diferentes autores

#*   --------       ----------
#*  | BOOKS | <==> | AUTHORS |
#*  --------       ----------

#* Nesse caso adicionamos um tabela de conecção com 2 diferetnes foreign keys

#*   --------      ----------
#*  | BOOKS | ==> | AUTHORS |
#*  --------      ==========       ----------
#*               |  BOOKS  | <== | AUTHORS |
#*               ----------       ----------

# exemplo com User e Courses, sendo member a tabela de conecção

"""
 CREATE TABLE User(
       id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
       name    TEXT,
       email    TEXT
)"""

"""
 CREATE TABLE Course(
       id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
       title    TEXT
)"""

"""
 CREATE TABLE Member(
       user_id      INTEGER, 
       course_id    INTEGER,
        role    INTEGER,
        PRIMARY KEY (user_id, course_id)
)"""

"""
    INSERT INTO User (name, email) VALUES ('Jane',
    'jane@tsui.org');
    INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsui.org');
    INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsui.org');
    
    INSERT INTO Course (title) VALUES ('Python');
    INSERT INTO Course (title) VALUES ('SQL');
    INSERT INTO Course (title) VALUES ('PHP');
"""

"""
    INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
    INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
    INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);
    
    INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
    INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

    INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
    INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);
"""

# Agora começamos a conectar os dados

"""
    SELECT User.name, Member.role, Course.title
    FROM User JOIN Member JOIN Course
    ON Member.user_id = User.id AND Member.course_id = Course.id
    ORDER BY Course.title, Member.role DESC, User.name
"""
