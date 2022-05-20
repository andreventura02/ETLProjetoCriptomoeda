from contextlib import contextmanager
import psycopg2
import psycopg2.extras as p
   
class PostgreConnector:
    
    def __init__(self,user:str,password:str,host:str,database:str):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__database = database
    @contextmanager
    def cursor_manager(self,cursor_factory:False):
        self.__conn = psycopg2.connect(user = self.__user,password = self.__password,host=self.__host,database=self.__database)
        self.__conn.autocommit = True
        if cursor_factory == False:
            self.curr = self.__conn.cursor()
        else:
            self.curr = self.__conn.cursor(cursor_factory=p.RealDictCursor)
        try:
            yield self.curr
        finally:
            self.curr.close()
            self.__conn.close()

