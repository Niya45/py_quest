# private classes and public classes are not as strictly enforced 

# PRIVATE CLASSES:
# -------------------------------

""" 
- naming : __classname
- _module__classname : private classes are name mangled.
- Python don't have a private class system; name mangling exist.
- Harder to manage outside the native module
- Not really pythonic
- Can't be imported : 'import __PrivateBank from encapsulation_c.py'; worng due to name mangling
"""

class __PrivateBank:  # "Private" class (convention)
    def __init__(self):
        self.__secret = "Confidential data"

    def __hidden_method(self):
        print("Top-secret banking logic!")


class PublicBank:
    def get_private_bank(self):
        return __PrivateBank()  # Only accessible inside the module
    
# PUBLIC CLASSES:
# -------------------------------

""" Conventional
- Meant for subclassing and internal use
- naming : _classname
- Can be improted; Not recomended
"""

class _PrivateAccount:
    def __init__(self, secret):
        self._secret = secret
    
    def _get_secret(self):
        return self._secret
    

class PublicAccount(_PrivateAccount):
    def __init__(self, secret, id):
        super().__inti__(secret)
        self.id = id


acc = PublicAccount("Do not peek", 23003)
acc._get_secret() # possible but bad!