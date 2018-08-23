# -*- coding: utf-8 -*-


import sqlite3 as lite

from clint.textui import colored


def readNames(tableName='USERS', dbName='radioDB.db'):
    """
       DEVELOPMENT
       
       take a table and database name with default settings
       makes a query to the database for only the name option
       
       INPUT STRING:
        SELECT Name from USERS
       
       input <string>
       output <list> || <False>
    """
    pass


def addUser(name, tableName='USERS', dbName='radioDB.db'):
    """
       DEVELOPMENT
       
       takes a name as an input with the default values for tableName and dbName
       makes a request to the database to create a new user
       
       INPUT STRING:
        INSERT INTO tableName VALUES (uid, name, questions, scores)
       
       input <string>
       output <boolean>
    """
    pass
   

def delUser(name, tableName='USERS', dbName='radioDB.db'):
    """
       DEVELOPMENT
       
       takes a name as an input with default values for tableName and dbName
       makes a request to the database to delete a user
       
       INPUT STRING:
        DELETE FROM USERS WHERE Name=name
       
       input <string>
       output <boolean>

    """
    pass


def updateUser(name, target, value, tableName='USERS', dbName='radioDB.db'):
    """
       DEVELOPMENT
       
       takes a name, target and value as an input with the default values
        for tableName and dbName
       makes a request to the database to update a users target value to
        the new value
       
       INPUT STRING:
        UPDATE tableName SET target=value WHERE Name=name
              
       input <string>
       output <boolean>
    """
    pass


def colorRED(text):
    """
       returns the string of text in the color RED

       input <string>
       output <string>
    """
    return colored.red(text)


def colorGREEN(text):
    """
       returns the string of text in the color GREEN

       input <string>
       output <string>
    """
    return colored.green(text)


def colorYELLOW(text):
    """
       returns the string of text in the color YELLOW

       input <string>
       output <string>
    """
    return colored.yellow(text)