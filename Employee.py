class Employee():
    
    def __init__(self, name, number, department, job):

        self.name = name
        self.number = number
        self.department = department
        self.job = job
    def set_name(self, name):
        self.name = name
    def set_number(self, number):
        self.number = number
    def set_department (self, department):
        self.department = department
    def set_job (self, job):
        self.job = job
    def get_name(self):
        return self.name
    def get_number(self):
        return self.number
    def get_department(self):
        return self.department
    def get_job(self):
        return self.job
    def __str__(self):
        return "Name: " +self.name+ "\nID Number "+self.number+"\nDepartment "+self.department+"\nJob "+self.job

import pickle
def main():
  emp_dic = load_emp()
  menu()
  choice = input('Enter your choice:')
  choice=int(choice)
  while choice!=5:
    if choice == 1:
        lookup(emp_dic)
    elif choice == 2:
        add_(emp_dic)
    elif choice == 3:
        change(emp_dic)
    elif choice ==4:
        delete_(emp_dic)
    elif choice == 0 or  choice > 5:
        print ('You made a wrong selection')
    elif choice == 5:
        print ("The program would quit now...")
    print('')
    print('')
    menu()
    choice = float(input('Enter your choice:'))
    choice=int(choice)
    save_emp(emp_dic)        

def load_emp():
        try:


            load_dic = open('employee.dat' , 'rb')
            emp_details = pickle.load(load_dic)
            load_dic.close()
        except IOError:
            emp_details = {}
        return emp_details
def save_emp(emp_dic):
        save_file = open('employee.dat','wb')
        pickle.dump(emp_dic , save_file)
        save_file.close()

def lookup(emp_dic):
        
       search = input("Enter your search query")
       search_result = emp_dic.get(search, "Entry not found")
       print(" search_result")

def add_(emp_dic):
        again='y'
        while again.lower() == 'y':
        
            name_ = input("Enter employee name:")
            number =input("Enter the ID number:")
            depart = input("Enter Department:")
            job = input("Enter Job title:")
            if name_ not in emp_dic:
                entry = Employee(name_ ,number, depart, job)
                emp_dic[name_]  = entry
                print (name_, "has been successfully added")
            else:
                print (name_, "already exists!")
            again = input("Enter 'y' to continue or any other alphabet to quit")

def change(emp_dic):
    
    search = input("Enter the Employee ID you want to change the details")
    if search in emp_dic:
        
        name_ = input("Enter new employee name:")
        number = input("Enter new the ID number:")
        depart = input("Enter new Department:")
        job = input("Enter new Job title:")
        entry = Employee(name_,number, depart, job)
        emp_dic[name_]  = entry
        print (name_, "has been successfully updated")
    else:
        print ("Entry not found")

def delete_ (emp_dic):

    search = input("Enter the Employee ID you want to change the details")
    if search in emp_dic:
        del emp_dic[search]
        print (search, " has been deleted successfully")
    else:
        print ("Entry not found")


def menu():
  print ('Choose your Option below:')
  print ("Look-up Employee Details = 1")
  print ('Add new Employee Details = 2')
  print ('Change an existing Employee Details = 3')
  print ('Delete an Employee Details = 4')
  print ('Quit the program = 5')


main()
import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'root@localhost' 
password = 'Dharam@3840' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()