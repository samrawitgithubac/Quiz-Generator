# -*- coding: utf-8 -*-

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
    pass


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
    pass


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
        pass
    
    def validName(test_name):
        """
           Takes test_name as input
           checks if input has been given
            if so, check the value fot all test involving valid names
           returns boolean, True if all check pass
        """
        pass

    pass


def main():
    """
       MISSING DESCRIPTION
       
       input <None>
       output <boolean>
    """
    pass    