# heros = ["Superman","hanu-man","batman","ironman","spiderman","captain america"]
# print(heros)

# def print_heros(list):
#     print(len(list))       ----> lenght find using function


#------------factorial----------
# i=1
# n=4
# while i<=10:
#     # mul = n*i
#     # print(n,"*",i,"=",mul)
#     i+=1

# n=5
# fact =1
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)
# n=int(input("Enter a number: "))

# def cal_fact(n):
#     fact = 1

#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

# cal_fact(5)       -------> using funtion 

#----------- Curency converter ------

# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val,"USD =",inr_val,"INR")

# converter(2)       --------> using function


#------------ even , odd using function --------
# n = int(input("Enter a number: "))

# def cal_num(num):
#     if num %2==0:
#         print(num,"is even")
#     else:
#         print(num,"is odd")
# cal_num(n)


#---------------------------------- Student name and mark ( constructor , method and staticmethod ) ------------------------


# class Student():
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("Hello Student")

#     def get_avg(self):
#         sum = 0 
#         for val in self.marks:
#             sum += val
#         print("HI", self.name , "your avarage marks is :", sum/len(self.marks))    

# s1 = Student("Raju",[80,98,88,92])
# s1.get_avg()
# s1.hello()  


#--------------------------------------- Bank account , debit and  credit ( constructor & method ) -----------------------------

# class Bank:
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc
    
#     #Debit Method
#     def debit(self,amount):
#         self.balance -= amount
#         print("Your amount", amount , "has debited.")
#         print("Total balance is :",self.get_balance())

#     #Credit Method
#     def credit(self,amount):
#         self.balance += amount
#         print("Your amount", amount , "has credited.")
#         print("Total balance is :",self.get_balance())

#     def get_balance(self):
#         return self.balance

# acc1 = Bank(1000,"SBI95723")
# acc1.debit(100)
# acc1.credit(50)




#--------------------------- Area and Perimeter -----------------
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
    
#     def area(self):
#         return (22/7) * self.radius ** 2 #PI * r^2 
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius #2 * PI * r
    


# c1 = Circle(21)
# print("Area =", c1.area())
# print("Perimeter = ", c1.perimeter())


#---------------------- Define employe class with attribute role , department , slary its have the showDetails() method -------------

# class Employee:
#     def __init__(self, role , dept , salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
    
#     def showDetails(self):
#         print("Role =",self.role)
#         print("Department = ",self.dept)
#         print("Salary =",self.salary)

# e1 = Employee("accountatant","Finance","60,000")
# e1.showDetails()       


#----- after this complete you just add on this , Create Engineer class that inherits properties from Employee & has addditional attributes : name & age ------

# class Employee:
#     def __init__(self, role , dept , salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
    
#     def showDetails(self):
#         print("Role =",self.role)
#         print("Department = ",self.dept)
#         print("Salary =",self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 
#         super().__init__("Engineer","IT","75,000")


# en1 = Engineer("Elun Musk",40)
# en1.showDetails()


#----------------------------- Create class Order which stores items & its price , use Dunder dunction __gt__() to convey that: order1 > order2 .......
#if price of order1> price of order2

# class Order:
#     def __init__(self,item , price):
#         self.item = item
#         self.price = price

#     def __gt__(self,ord2):
#         return self.price > ord2.price

# ord1 = Order("chips =",20)
# ord2 = Order("tea =",10)
# print(ord1 > ord2) #true


