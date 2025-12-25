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
