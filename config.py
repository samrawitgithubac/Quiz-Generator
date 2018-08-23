# -*- coding: utf-8 -*-


import sqlite3 as lite

from clint.textui import colored


def readNames(dbName='radioDB.db'):
    """
       MISSING DESCRIPTION
    """
    pass


def addUser(name, tableName='USERS', dbName='radioDB.db'):
    """
       MISSING DESCRIPTION
    """
    pass
   

def delUser(name, tableName='USERS', dbName='radioDB.db'):
    """
       MISSING DESCRIPTION
    """
    pass


def updateUser(name, target, value, tableName='USERS', dbName='radioDB.db'):
    """
       MISSING DESCRIPTION
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