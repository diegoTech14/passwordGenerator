import pymysql
import sys
import os

from .connection import ConnectionDataBase
sys.path.append(os.path.join(os.getcwd(), "logic"))
import password_hash

class Queries:
    
    con = None
    
    def __init__(self):
        
        self.con = ConnectionDataBase("localhost", "diego", "diegoduarteslipknot", "generatordb")
        self.con = self.con.connection()
        
    @classmethod
    def insert_password(cls, password):
        response = False

        try:
            with cls.con.cursor() as cursor:
                query = "INSERT INTO `passwords` (`password`) VALUES (%s,)"
                cursor.execute(query, (password))
                cursor.commit()
                response = True
        except:
            response = False
            
    
    def insert_user(self, name: str, surnames: str, 
    age: str, email: str, password: str, user_name: str) -> bool:
        
        response = False

        try:
            with self.con.cursor() as cursor:            
                query = """INSERT INTO `users` (`name`, `surnames`, `age`, `email`, `password`, `user_name`) 
                VALUES (%s, %s, %s, %s, %s, %s)"""
                password = password_hash.HashedPassword.hashing_password(password)
                cursor.execute(query, (name, surnames, age, email, password, user_name))
                self.con.commit()
                response = True
            
        except Exception as error:
            response = False

        if self.con:
            print("open")    
        return response
    
    def verify_user(self, user_name: str, password: str) -> bool:

        response = False
        hashed_password = ''
        

        try:
            with self.con.cursor() as cursor:
                query = """ SELECT password FROM `users` WHERE `user_name` = %s"""
                cursor.execute(query, (user_name, ))
            
                if not(cursor.fetchone is None):
                    hashed_password = cursor.fetchone()[0]
                        
                    if password_hash.HashedPassword.shape_password(password, hashed_password):
                        response = True
                            
        except Exception as error:
            response = False

        return response

    