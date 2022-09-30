# Each instance should have the 
# description, date, charge amount and 
# employee ID as attributes
import EmployeeClass as ec

class PayrollDeduction:

    def __init__(self, desc, date, charge_amt, emp_id):
        self.__desc = desc
        self.__date = date
        self.__charge_amt = charge_amt
        self.__emp_id = emp_id
    
    
    def get_name(self):
        return self.__desc

    def get_id(self):
        return self.__date

    def get_title(self):
        return self.__emp_id

    
    def charge(self, charge, emp_id):
        if self.__emp_id == emp_id:
            self.__charge_amt = charge
        else:
            self.__charge_amt = 0
        
    def get_charge(self):
        return float(self.__charge_amt)       
    
    
    '''       
    def __str__(self, gross_sal, deduction):
        net_sal = gross_sal - deduction
        return '\nNet Pay: ' + '$' + net_sal
    '''