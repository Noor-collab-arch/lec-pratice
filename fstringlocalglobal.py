u'''ser_name:str = 'Noor hussain'
#user_name :str = 'Noor's phone' error 
#user_name : str= 'Noor"s phone' correct
languae_learning = "Python"
#concet
#user_bio :str = user_name +" is a "+languae_learning+" developer "
#f string use instead of concat
user_bio =f"{user_name} is a {languae_learning} developer"
print(user_bio)'''
# function
'''def greeting(name:str):
    output= f"Hello {name}"
    print(output)
greeting("jon")    
greeting("ALi")'''

# function that add two number and add 50 in the sum and print sum
'''def Add_num(num1:int, num2:int):
    sumoftwonumber = num1+num2
    return sumoftwonumber
firstsum = Add_num(10,20)
finalsum = Add_num(50, firstsum)
print(finalsum)'''


# percenateg function
def percentage(obt:int , ttl:int):
    perc = obt/ttl *100
    print(perc)
ob = int(input("Enter marks"))
tt = int(input("Enter total marks"))
percentage(ob,tt)
#percentage(850,1100)    