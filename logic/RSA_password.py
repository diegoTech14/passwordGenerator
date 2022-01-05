from Crypto.PublicKey import RSA

class RSAPassword(object):

    __key_pair = RSA.generate(2048)
    __password_encrypted = ''

    @classmethod
    def __generate_keys(cls):
        
        
        with open("privateKey.pem", "wb") as private_key_file:
            private_key_file.write(cls.__key_pair.exportKey("PEM"))
        
        with open("publicKey.pem", "wb") as public_key_file:
            public_key_file.write(cls.__key_pair.public_key().exportKey("PEM"))

    def __init__(self):
        self.__generate_keys()

    @classmethod
    def encrypt(cls, password: str) -> str:
        
        response = None
        try:
            from Crypto.Cipher import PKCS1_OAEP
        
            public_key = RSA.import_key(open("publicKey.pem").read())
            encryptor = PKCS1_OAEP.new(public_key)
            password = password.encode('ASCII')
            cls.__password_encrypted = encryptor.encrypt(password)

            response = cls.__password_encrypted.hex()    
            
        except:
            response = False

        finally:
            return response

    @classmethod
    def decrypt(cls) -> str:
        
        response = None
        try:
            from Crypto.Cipher import PKCS1_OAEP

            with open("privateKey.pem", "rb") as private_key_file:
                private_key = RSA.importKey(private_key_file.read())
                
                decryptor = PKCS1_OAEP.new(private_key)
                password_decrypted = decryptor.decrypt(cls.__password_encrypted)
                
                response = password_decrypted.decode('ASCII')
                
        except:
            response = False

        finally:
            return response

            


