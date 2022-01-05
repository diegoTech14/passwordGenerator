class Validations(object):
    
    @classmethod
    def validating_int(cls, n):
        response = False

        if isinstance(n, int):
            response = True
        
        return response
    
    @classmethod
    def validating_str(cls, _str):
        response = False
        
        if isinstance(_str, str):
            response = True

        return response
    
    @classmethod
    def validating_only_int(cls, _str):
        response = False
        
        if _str.isnumeric():
            response = True
            
        return response
    