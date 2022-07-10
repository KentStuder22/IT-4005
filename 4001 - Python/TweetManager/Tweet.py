import time

class Tweet:
    #Initializing the attributes

    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = time.time()

    def get_author( self ):
        return self.__author

    def get_text( self ):
        return self.__text

    def get_age( self ):
        current = time.time()
        difference = int(current - self.__age)
        #case for under a minute
        if(difference >= 0 and difference < 60):
            return str(difference) + "s"
        #case for under an hour
        elif(difference >= 60 and difference < 3600):
            difference = int(difference / 60)
            return str(difference) + "m"
        #case for over an hour and under a day
        elif(difference >= 3600 and difference < 86,400):
            difference = int(difference / 3600);
            return str(difference) + "h"
        
    #defining string because author is private
    def __str__( self ):
        return self.__author + " - " + self.get_age() + '\n' + self.__text + '\n'
