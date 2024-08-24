'''# string var
Name = "Jon doe n/ male"
#int
age = 24
#float
height = 165.5
#bool
have_sugar = False
print(Name)
print(age)
print(height)
print(have_sugar)
print(Name ,age ,height , have_sugar )
# assigning values in one line
name, age, location= "jon" , 29, "usa"
num1 :str ="10"
num2 :str ="20"
# this line will give error because integer cant concatinate with string num3 = num1 + num2 + Name + age
num3 = num1 + num2 + Name 
print(num3)
bol = 2>5
print(bol)'''

'''# del keyword used to delete something
greeting : str = "Hi everyone"
#del greeting
print(greeting)
print(id(greeting))
#type() tell us the datatype of var
print(type(greeting))'''

# arithmetic operator
num1 : int = 100
num2 : int = 50
num3: float =10.4
# adding or multiplying int with float will result float
'''num4 = num1 + num3 
num4 = int(num1 + num3)  # convert into int
print(num4)'''

'''num4 =3
num7 =5
num5 = num4 ** 2
print(num5)
num6 = num4 % num7
print(num6)
num8 = num7 % num4
print(num8)
num9 = num7 // num4
num9 += 5
print(num9)
print(2 <= 5 and 4==4)
print(2 <= 5 or 9!=4)
print(2 <= 5 and 9!=4)'''
#input to take inpt from user
user_age :int  = input("Enter your age:")
result = 10 + int(user_age)
print(result)