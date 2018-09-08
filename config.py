# -*- coding: utf-8 -*-


import json
import sqlite3 as lite

from clint.textui import colored
from numpy.random import choice

global VERBOSE
VERBOSE = False#True

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
    conn = lite.connect(dbName)
    names = []
    error = False
    try:
        cur = conn.cursor()
        statement = "SELECT Name FROM USERS;"
        response = cur.execute(statement)
        getNames = response.fetchall()
        names = [getNames[i][0] for i in xrange(len(getNames))]
    except Exception as e:
        if VERBOSE:
            print colorRED("[-]") + " Something went wrong: %s" % e
        error = True
    finally:
        if conn:
            conn.close()
        if error:
            return False
        else:
            if VERBOSE:
                print colorGREEN("[+]") + " Successfully Retrieved Names"
            return names


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
    conn = None
    error = False
    name = name.replace(' ', '')
    try:
        if VERBOSE:
            print colorYELLOW("[.]") + " Adding User " + name + " to DataBase ..."
        conn = lite.connect(dbName)
        cur = conn.cursor()
        names = readNames()
        if name in names:
            if VERBOSE:
                print colorYELLOW("[!]") + " That Name is Already Taken"
            error = True
            raise Exception, "Name already in database"
        getMaxUIDs = cur.execute("SELECT MAX(UID) FROM USERS;")
        maxUIDs = getMaxUIDs.fetchone()
        maxUID = int(maxUIDs[0])
        
        UID = maxUID + 1
        UID = '%08d' % UID
        
        testTemplate = getQIDs()
        testTemplate = json.dumps(testTemplate)

        values = (UID, name, testTemplate, '[]')
        values = str(values)
        statement = "INSERT INTO " + tableName + " VALUES" + values
        cur.execute(statement)
    except Exception as e:
        if VERBOSE:
            print colorRED("[-]") + " Something went wrong: %s" % e
        error = True
    finally:
        if conn:
            conn.commit()
            conn.close()
        if not error:
            if VERBOSE:
                print colorGREEN("[+]") + " Inserted Values Successfully"
            return True
        else:
            return False   


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
    conn = None
    error = False
    try:
        names = readNames()
        if name not in names:
            if VERBOSE:
                print colorYELLOW("[!]") + " That Name is Not Taken"
            error = True
            raise Exception, "Name not in database"
        conn = lite.connect(dbName)
        cur = conn.cursor()
        statement = "DELETE FROM USERS WHERE Name='" + name + "';"
        cur.execute(statement)
    except Exception as e:
        if VERBOSE:
            print colorRED('[-]') + " Something went wrong: %s" % e
        error = True
    finally:
        if conn:
            conn.commit()
            conn.close()
        if error:
            return False
        else:
            if VERBOSE:
                print colorGREEN("[+]") + " Succussefully Deleted User"
            return True


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
    conn = None
    error = False
    try:
        conn = lite.connect(dbName)
        cur = conn.cursor()
        statement = "UPDATE " + tableName + " SET " + target + "=? WHERE Name=?"
        cur.execute(statement, (value, name))
    except Exception as e:
        error = True
        if VERBOSE:
            print colorRED("[-]") + " Something went wrong: %s" % e
    finally:
        if conn:
            conn.commit()
            conn.close()
        if error:
            return False
        else:
            if VERBOSE:
                print colorGREEN("[+]") + " Successfully Updated User"
            return True



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
    conn = None
    error = False
    data = []
    try:
        conn = lite.connect(dbName)
        cur = conn.cursor()
        statement = "SELECT " + target + " FROM " + tableName + " WHERE Name='" + name + "';"
        cur.execute(statement)
        response = cur.fetchall()
        ### HERE ###
        data = response[0][0]
    except Exception as e:
        error = True
        if VERBOSE:
            print colorRED("[-]") + " Something went wrong: %s" % e
    finally:
        if conn:
            conn.close()
        if error:
            return False
        else:
            return data

def getQIDs(dbName='radioDB.db'):
    """
       DEVELOPMENT
       
       takes a database name as a default setting
       makes a query to the database to create the original question template
       
       INPUT STRING:
        SELECT QID from QUESTIONS
       
       input <string>
       output <list> || <False>
    """
    conn = lite.connect(dbName)
    testTemplate = {}
    error = False
    try:
        cur = conn.cursor()
        statement = "SELECT QID FROM QUESTIONS;"
        response = cur.execute(statement)
        getTemplate = response.fetchall()
        for i in xrange(len(getTemplate)):
            testTemplate[getTemplate[i][0]] = 0
    except Exception as e:
        if VERBOSE:
            print colorRED("[-]") + " Something went wrong: %s" % e
        error = True
    finally:
        if conn:
            conn.close()
        if error:
            return False
        else:
            if VERBOSE:
                print colorGREEN("[+]") + " Successfully Retrieved Test Template"
            return testTemplate


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
    conn = None
    error = False
    try:
        if VERBOSE:
            print colorYELLOW("[.]") + " Creating Table " + tableName + " ..."
        conn = lite.connect(dbName)
        cur = conn.cursor()
        statement = "CREATE TABLE " + tableName + str(values)
        cur.execute(statement)
    except Exception as e:
        if VERBOSE:
            print colorRED("[-]") + " Something went wrong: %s" % e
        error = True
    finally:
        if conn:
            conn.close()
        if not error:
            if VERBOSE:
                print colorGREEN("[+]") + " Created Table Successfully"
            return True
        else:
            return False



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
    conn = None
    error = False
    try:
        if VERBOSE:
            print colorYELLOW("[.]") + " Adding Values to " + tableName + " ..."
        conn = lite.connect(dbName)
        cur = conn.cursor()
        statement = "INSERT INTO " + tableName + " VALUES" + values
        cur.execute(statement)
    except Exception as e:
        if VERBOSE:
            print colorRED("[-]") + " Something went wrong: %s" % e
        error = True
    finally:
        if conn:
            conn.commit()
            conn.close()
        if not error:
            if VERBOSE:
                print colorGREEN("[+]") + " Inserted Values Successfully"
            return True
        else:
            return False


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
    conn = None
    error = False
    result = ''
    try:
        if VERBOSE:
            print colorYELLOW("[.]") + " Selecting Question Number " + questionNumber + " from " + groupID + subgroupID + " ..."
        conn = lite.connect(dbName)
        cur = conn.cursor()
        QID = 'T' + groupID + subgroupID + questionNumber
        statement = 'SELECT * FROM QUESTIONS WHERE QID="' + QID + '";'
        cur.execute(statement)
        row = cur.fetchone()
        result = row
        if result == None:
            if VERBOSE:
                print colorRED("[-]") + " Query Returned No Results"
            error = True
    except Exception as e:
        if VERBOSE:
            print colorRED("[-]") + " Something went wrong: %s" % e
        error = True
    finally:
        if conn:
            conn.close()
        if not error:
            if VERBOSE:
                print colorGREEN("[+]") + " Selected Question Successfully"
            return result
        else:
            return False


def selectRandomWithWeights(name, depreciator=0.2):
    """
       takes a name as input, with default value for depreciator
       
       first, pulls the full question Dictionary for the user
       then, breaks 
       
       input <string>
       output <list> || <False>
    """
    choices = []
    
    userData = json.loads(readUserValue(name, "questionDict"))

    subgroupIDs = 'ABCDEF'
    
    for i in xrange(10):
        groupID = str(i)
        for subgroupID in subgroupIDs:
            questionRange = getQuestionRange(groupID, subgroupID)
            temp = []
            for e in questionRange:
                temp.append(userData[e])
            if temp == []:
                break
            else:
                probabilities = [j * depreciator for j in temp]
                keys = range(1,len(probabilities)+1)
                keys = [str(e).zfill(2) for e in keys]
                current = choice(keys, 1, probabilities)[0]
                choices.append((groupID, subgroupID, current))
    return choices


def getQuestionRange(groupID, subgroupID, dbName='radioDB.db'):
    """
       DEVELOPMENT
       
       takes groupID and subgroupID as input with a database name with default settings
       makes a query to the database to get the question range for the given 
        group and subgroup
       
       INPUT STRING:
        SELECT QID FROM QUESTIONS WHERE QID LIKE "groupID+subgroupID%"
       
       input <string>
       output <list> || <False>
    """
    conn = None
    error = False
    result = ''
    try:
        if VERBOSE:
            print colorYELLOW("[.]") + " Selecting Question List from " + groupID + subgroupID + " ..."
        conn = lite.connect(dbName)
        cur = conn.cursor()
        statement = 'SELECT QID FROM QUESTIONS WHERE QID LIKE "T' + groupID + subgroupID + '%";'
        cur.execute(statement)
        row = cur.fetchall()
        result = row
        result = [result[i][0] for i in xrange(len(result))]
        if result == None:
            if VERBOSE:
                print colorRED("[-]") + " Query Returned No Results"
            error = True
    except Exception as e:
        if VERBOSE:
            print colorRED("[-]") + " Something went wrong: %s" % e
        error = True
    finally:
        if conn:
            conn.close()
        if not error:
            if VERBOSE:
                print colorGREEN("[+]") + " Selected Question List Successfully"
            return result
        else:
            return False


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