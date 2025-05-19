# PRIVATE METHODS
# ---------------------------------------------

""" 
- naming : __methodname
- Only accessible within the class. 
- Not inherited due to name mangling
- Used for internal logic that shouldn't be exposed outside the class.
"""

class BankAccount:
    def __init__(self, name, balance):
        self.name  = name
        self.balance  = balance

    def __deduction_amt(self):
        self.balance -=10
    
    def _check_name(self, name):
        if self.name == name:
            return True
        else:
            return False

    def withdraw(self, name, amt):
        if amt > self.balance:
            print("Balance is insufficient.")
        elif self._check_name(name) == True:
            print(f"Withdrawing {amt}...")
            self.balance -= amt
            self.__deduction_amt()

acc_1 = BankAccount("Niya", 100000)

# normal method : 
acc_1.withdraw("Niya", 10000)
print(acc_1.balance)

# private method : can't be called
# acc_1.__deduction_amt()

# PROTECTED METHODS
# ---------------------------------------------

""" a convention than a rule
- naming : _methodname
- Only accessible within the class and child classes
- Inherited
- Can access directly; Discouraged
- Used for methods that child classes might need to modify or extend.
"""
