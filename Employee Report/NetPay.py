import PayrollDeductionClass as py
import EmployeeClass as ec

def main():

    name = 'Jimmy Smith' #input("Please enter employee first and last name: ")
    id_num = 58475 #input("Please enter employee ID number: ")
    dep = 'Information Systems' #input("Please enter employee department: ")
    title = 'Developer' #input("Please enter employee job title: ")
    m_salary = 6800.00 #int(input("Please enter employee monthly salary: "))
    
    expenses = {'expense1':
                {'description':'food court', 'date':'8/14/2022','charge':22.50,'id_num': 39119},
               'expense2': 
                {'description':'gift contribution', 'date':'8/12/2022','charge':25.00,'id_num': 58475},
               'expense3': 
                {'description':'food court', 'date':'8/17/2022','charge':15.25,'id_num': 21547},
               'expense4': 
                {'description':'vending machine', 'date':'8/22/2022','charge':3.00,'id_num': 58475},
               'expense5': 
                {'description':'vending machine', 'date':'8/5/2022','charge':2.75,'id_num': 58475}}
    
    
    emp_info = ec.Employee(name,id_num, dep, title, m_salary)
    #employee = [emp_info.get_name(),emp_info.get_id(),emp_info.get_dep(),emp_info.get_title(), emp_info.get_m_salary()]
    print(emp_info)
    
    total_charge = 0
    for expense in expenses:
        payroll_ded = py.PayrollDeduction(expenses[expense]['description'],expenses[expense]['date'],expenses[expense]['charge'], expenses[expense]['id_num'])
        payroll_ded.charge(expenses[expense]['charge'], id_num)
        total_charge += payroll_ded.get_charge()
    

    print('Net Pay: ','$',emp_info.get_m_salary() - total_charge, sep = '')

main()

    #total_charge = payroll_ded.get_charge()
        #if expenses[expense]['id_num'] == employee[1]:
        #    print(expenses[expense]['charge'])
    
    #print(payroll_ded.get_charge())  


'''
    #title   = [desc, date, charge_amt, emp_id]
    expense1 = ['food court', '8/14/2022', 22.50, 39119]
    expense2 = ['gift contribution', '8/12/2022', 25.00, 58475]
    expense3 = ['food court', '8/17/2022', 15.25, 21547]
    expense4 = ['vending machine', '8/22/2022', 3.00, 58475]
    expense5 = ['vending machine', '8/5/2022', 2.75, 58475]

        for charge in expense:
            print(deduction['description'])
            print(deduction['date'])
        '''
        #net_salary = py.PayrollDeduction(expense)
    #print ("{:<18} {:<15} {:<25} {:<15} {:<15}".format('Employee Name','ID Number','Department','Job Title','Monthly Salary'))
    #print ("{:<20} {:<10} {:<28} {:<15} {:<0} {:<1}".format(emp_info.get_name(),emp_info.get_id(),emp_info.get_dep(),emp_info.get_title(), '$', emp_info.get_m_salary(), sep = ''))


