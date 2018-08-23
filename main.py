# -*- coding: utf-8 -*-


import os, re, inflect
from config import *

def startUp(dbName = 'radioDB.db'):
    """
       takes a dbname with default value
       checks if a database already exists.
       if no database is available, creates one.
       populates the global variable 'users' for future use
       
       NOTE: The database has two tables (users, questions)
               USERS:
                uid:string name:string questionDict:string scores:string
               QUESTIONS:
                qid:string question:string answer:string jsonOptions:string
       
       input <string>
       output <boolean>
    """
    global users
    if os.path.isfile(dbName):
        if VERBOSE:
            print colorGREEN("[+]") + " Conecting to DataBase..."
        users = readNames()
    else:
        if VERBOSE:
            print colorYELLOW("[!]") + " No DataBase Found!"
            print colorYELLOW("[!]") + " Creating DataBase 'RadioDB.db' Now..."
        try:
            users = []
            f = open(dbName, 'w+')
            f.close()
            tables_values = {'USERS': '(UID TEXT, Name TEXT, QuestionDict TEXT, Scores TEXT)', 'QUESTIONS' : '(QID TEXT, Question TEXT, Answer TEXT, Options TEXT)'}
            for tableName, values in tables_values.items():
                createTable(tableName, values, dbName)


            conn = lite.connect(dbName)
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO USERS VALUES('00000000', 'admin', 'None', 'None');")
            
            if VERBOSE:
                print colorGREEN("[+]") + " Created DataBase :)"
                print colorYELLOW("[.]") + " Loading Questions into DataBase..."
            loadedDB = parseQPoolandInsert()
            if VERBOSE:
                if loadedDB:
                    print colorGREEN('[+]') + " Successfully Loaded Questions!"
                else:
                    print colorRED('[-]') + " Unable to Load Questions into DataBase"
        except:
            if VERBOSE:
                print colorRED("[-]") + " SOMETHING WENT WRONG! QUITTING..."
            return False
        finally:
            return users

def parseQPoolandInsert(fName='TechQPool.txt', dbName='radioDB.db', tableName='QUESTIONS'):
    """
       takes default values for file name, dbName, and tableName
       parses the question pool file and stores the result into the database
       
       NOTE: iterates over the entire file and collects
              the following information
              
             [+] Question Section
             [+] Question Subsection
             [+] Question Number
             [+] Question Posed
             [+] Correct Answer
             [+] All Possible Answers
       
       input <string>
       output <boolean>
    """
    pattern = '^T\d[ABCDEFGHIJ]\d\d'
    f = open(fName, 'r')
    while True:
        try:
            line = f.readline().strip()
            if len(line) == 0:
                continue
            if line == "ENDOFTRANSMISSION":
                return True
            doesMatch = re.match(pattern, line)
            if doesMatch:
                QID = doesMatch.group(0)
                answerLetter = line.split()[1][1]
                question = f.readline().strip()
                if "'" in question:
                    question = question.replace("'", 'Jw==')
                if '"' in question:
                    question = option.replace('"', 'lg==')
                options = []
                temp = []
                temp.append(f.readline().strip())
                temp.append(f.readline().strip())
                temp.append(f.readline().strip())
                temp.append(f.readline().strip())
                for option in temp:
                    if "'" in option:
                        option = option.replace("'", 'Jw==')
                    if '"' in option:
                        option = option.replace('"', 'lg==')
                    if option[0] == answerLetter:
                        answer = option[3:]
                    else:
                        options.append(option[3:])
                jsonOptions = json.dumps(options)
                values = (QID, question, answer, jsonOptions)
                values = str(values)
                insertToDB(tableName, values)
        except Exception as e:
            if VERBOSE:
                print 'error:', e
            f.close()
            return False


def processUser():
    """
       MISSING DESCRIPTION
       
       input <None>
       output <boolean>
    """
    def invalidCharacters(test_name):
        """
           Takes test_name as input
           checks if input has been given
            if so, checks the value for the use of approprate characters only
           returns boolean, True if all characters are valid
        """
        try:
            if len(test_name) == 0:
                return True
            allowed = string.ascii_letters
            return not (set(test_name) <= allowed) or len(test_name.split(' ')) > 1
        except:
            return False
    
    def validName(test_name):
        """
           Takes test_name as input
           checks if input has been given
            if so, check the value fot all test involving valid names
           returns boolean, True if all check pass
        """
        conditions = []
        if invalidCharacters(test_name):
            conditions.append('The name chosen contains invalid characters. Must contain only letters.')
        if name.lower() in users:
            conditions.append('The name chosen is already taken')
        return conditions

    doesPass = False
    isUser = raw_input("Are you a returning user: (y/N) ")
    if len(isUser) > 1:
        isUser = isUser[0]
    if isUser.lower() == 'y':
        name = raw_input("Please enter your name: ")
        name = name.replace(' ', '')
        if invalidCharacters(name):
            print colorYELLOW("[!]") + " Name contains invalid characters. Letters only."
            name = raw_input("Please enter your name: ")
            name = name.replace(' ', '')
            if invalidCharacters(name):
                print colorRED("[-]") + " Exiting from processUser..."
                return False
            
        if name.lower() in users:
            return name
        else:
            message = "The name '%s' is not in the current users. Would you like to continue as '%s': (y/N) " % (name, name)
            keepName = raw_input(message)
            if len(keepName) > 1:
                keepName = keepName[0]
            if keepName == 'y':
                doesPass = True
    
    error_count = 0

    while error_count < 3 and not doesPass:
        name = raw_input("Pleae enter your name: ")
        name = name.replace(' ', '')
    
        problems = validName(name)
        problem_count =  len(problems)
        p = inflect.engine()
    
        if problem_count != 0:
            error_count += 1
            print "Found", str(problem_count), p.plural("error",problem_count)
            for e in problems:
                print colorYELLOW("[!]") + " %s" % e
        else:
            break
    if error_count == 3:
        if VERBOSE:
            print colorRED("[-]") + " Exiting from processUser..."
        return False

    correct = addUser(name.lower())
    if correct:
        return name
    else:
        return False

def main():
    """
       MISSING DESCRIPTION
       
       input <None>
       output <boolean>
    """
    startUp()
    processUser()


if __name__ == "__main__":
#    global VERBOSE
#    VERBOSE = True
    main()
