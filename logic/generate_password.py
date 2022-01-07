from string import ascii_lowercase, ascii_uppercase, punctuation
from random import randint

from .validations.validations import Validations

class PasswordGenerator(object):
    
    new_password = ""
    
    def generate_password(self, len_pass):
        chars = ascii_lowercase + ascii_uppercase + punctuation
        response = False

        if Validations.validating_int(len_pass):
            while(len(self.new_password) < len_pass):
                random_number = randint(0, len(chars)-1)
                self.new_password += chars[random_number]
            response = self.new_password

        return response 
