from string import ascii_lowercase, ascii_uppercase, punctuation
from random import randint

from .validations.validations import Validations

class PasswordGenerator(object):
    
    new_password = ""
    
    def generate_password(self, len_pass, numbers, lower, upper, punct):
        chars = ""
        response = False
        if lower and upper and punct:
            chars = ascii_lowercase + ascii_uppercase + punctuation
                
        elif lower and upper:
                chars = ascii_lowercase + ascii_uppercase

        elif lower and punct:
            chars = ascii_lowercase + punctuation
                
        elif upper and punct:
            chars = ascii_uppercase + punctuation
                
        elif upper:
            chars = ascii_uppercase
        
        elif lower:
            chars = ascii_lowercase
        
        elif punct:
            chars = punctuation

        # validates if the len_pass variable contains a number
        if Validations.validating_int(len_pass):
            while(len(self.new_password) < len_pass):
                random_number_setter = randint(0, 1)

                if random_number_setter == 1 and numbers:
                    self.new_password += str(randint(0, 9))

                if chars != "":
                    # random_number contains a random number between 
                    # 0 and the lenght of the chars variable 
                    random_number = randint(0, len(chars)-1)
                    # set a new character in the new_password variable
                    self.new_password += chars[random_number]

            response = self.new_password

        return response 
