class Employee:

    def __init__(self, name, id_num, dep, title, m_salary):
        self.__name = name
        self.__id = id_num
        self.__dep = dep
        self.__title = title
        self.__m_salary = m_salary
    
    
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_dep(self):
        return self.__dep

    def get_title(self):
        return self.__title

    def get_m_salary(self):
        return self.__m_salary 

    def __str__(self):
        return '*** Employee Report *** \nName: ' + self.__name + '\nID Number: ' + str(self.__id) + '\nDepartment: ' + self.__dep + '\nGross Pay: ' + '$' + format(self.__m_salary, ',.2f')
    
    #def enter_name(self):
     #   self.__name = input("Enter Employee Name: ")
    
    #def enter_id(self):
    #    self.__id = input("Enter Employee ID Number: ")

#    def enter_dep(self):
 #       self.__dep = input("Enter Employee Departmet: ")
    
  #  def enter_title(self):
   #     self.__title = input("Enter Employee Job Title: ")
    
    #def enter_m_salary(self):
     #   self.__m_salary = input("Enter Employee Monthly Salary: ")
