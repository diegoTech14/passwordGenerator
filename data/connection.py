import pymysql

class ConnectionDataBase(object):
       
    __host = ""
    __user = ""
    __password = ""
    __db = ""

    def __init__(self, host, user, password, db_name):
        self.__host, self.__user = host, user
        self.__password, self.__db = password, db_name

    def connection(self):
        
        self.response = None
        self.connect = None

        try:
            self.connect = pymysql.connect(host=self.__host, user=self.__user, 
            password=self.__password, db=self.__db)
            self.response = self.connect
            
        except Exception as error:
            self.response = error
            
        return self.response
