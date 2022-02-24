import sys
import bcrypt
import os

sys.path.append(os.path.join(os.getcwd(), "logic", "validations"))
import validations

class HashedPassword(object):
    
    password_hashed = ""
    
    @classmethod
    def hashing_password(cls, password: str) -> str:
        
        response = None
        if not(validations.Validations.validating_only_int(password)):
            bytes_format_password = bytes(password, encoding="ascii")
            # bytes convierte en prefijo b con codificación ascii la cadena.
            salt = bcrypt.gensalt() 
            # sal generada
            hashed = bcrypt.hashpw(bytes_format_password, salt) 
            # hashing de la contraseña la sal
            response = cls.password_hashed = hashed.decode("utf-8") 
            
        return response


    @classmethod
    def shape_password(cls, password: str, hashed_password: str) -> bool:

        response = False
        if not(validations.Validations.validating_only_int(password)):
            password = bytes(password, encoding="ascii")
            hashed_password = bytes(hashed_password, encoding="ascii")
            
            if bcrypt.checkpw(password, hashed_password):
                response = True
            
        return response

    


