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


def readUserValue(name, target, tableName='USERS', dbName='radioDB.db'):
    """
       DEVELOPMENT
       
       takes a name and a target value as an input with the default values
        for tableName and dbName
       makes a query to the database to read only the specified value from
        the users information
       
       INPUT STRING:
        SELECT target FROM tableName WHERE Name=name
              
       input <string>
       output <string> || <False>
    """
    pass


def createTable(tableName, values, dbName='radioDB.db'):
    """
       DEVELOPMENT
       
       takes a table name and values with default name for dbName
       makes a request to the database to create a table with the given
        table name and associated values

       NOTE: values needs to have the following format
              (COLUMN_NAME DATA_TYPE)
       
       INPUT STRING:
        CREATE TABLE tableName values
       
       input <string>
       output <boolean>
    """
    pass


def insertToDB(tableName, values, dbName='radioDB.db'):
    """
       DEVELOPMENT
       
       takes a table name and values with the default value for dbName
       makes a request to the database to insert into the table with the given
        table name the values provided
       
       INPUT STRING:
        INSERT INTO tableName VALUES values
       
       input <string>
       output <boolean>
    """
    pass


def selectQuestion(groupID, subgroupID, questionNumber, dbName='radioDB.db'):
    """
       DEVELOPMENT
       
       takes a groupID, subgroupID, and questionNumber with default value for dbName
       makes a request to the database to pull the specified question
       NOTE: the output follows the following format
              { QID : [ Question, Answer, [ Incorrect Answers ] ] }
       
       INPUT STRING:
        SELECT * FROM QUESTIONS WHERE QID=QID
       
       input <string>
       output <dictionary> || <False>
    """
    pass

def selectRandomWithWeights(name, depreciator=0.2):
    """
       takes a name as input, with default value for depreciator
       
       first, pulls the full question Dictionary for the user
       then, breaks 
       
       input <string>
       output <list> || <False>
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