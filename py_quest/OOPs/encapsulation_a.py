
class BankAccount:
    def __init__(self, name, account_num, account_t, balance, overdraft_limit):
        self.__name = name
        self.__account_num = account_num
        self._account_t = account_t
        self.__balance = balance
        self.__overdraft_limit = overdraft_limit
    
    @property
    def name_func(self):
        return self.__name
    
    @name_func.setter
    def name_func(self, new_n):
        if new_n == "Nizar":
            pass
        else:
            self.__name = new_n
        print("setting new name....")
    
    @property
    def acc_t(self):
        return self.acc_t


acc1 = BankAccount("Niya", 1, "saving", 100000, -1000)

# PRIVATE ATTRIBUTES:
# ------------------------------

'''
- naming : __varName
- Only accessible within the class. 
- Can be accessed from methods inside the class
- _class__attribute : private methods are name mangled
- Isn't inherited, can't get or set. (but child's instances do have those attributes)
- No direct access
'''
# normal methods: useless
try:
    print("Initial name : "+acc1.__name)
    acc1.__name = "Nizar"
    print("Changed name : "+acc1.__name)
except:
    print("can't access private attributes")

# Workarounds:
try:
    print("Get private attri. thorugh methods: "+acc1.name_func)
    acc1.name_func = "Nizar"
    print("New name : "+acc1.name_func)
except:
    print("can't access private attributes through functions")

# PROTECTED ATTRIBUTE:
# ------------------------------
""" a convention than a rule
- naming : _varName
- Only accessible within the class and chlid class
- Can be accessed from methods inside the class
- Is inherited, can't get or set. (but child's instances do have those attributes)
- Direct access possible; Discouraged
"""
print(acc1._account_t)
acc1._account_t = 'joint'
print(acc1._account_t)
