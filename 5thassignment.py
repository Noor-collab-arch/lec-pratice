'''Create a function* that takes an array, an index, and a value as parameters. 
Inside the function, use the insert method to insert the value at the specified index in the array. 
Return the modified array.'''

'''def fruits(old_li:list, ind:int, new_val:str):
    old_li.insert(ind,new_val)
    return old_li
old_list:list = ["apple","banana","orange"]
spec_ind: int = 2
new_item = "kiwi"
print("Old list ", old_list)
newlist=fruits(old_list,spec_ind,new_item)
#newlist=fruits(["apple","banana","orange"], 2, "kiwi")

print("updated list " , newlist)'''

'''2. *Implement a simple shopping cart program* using an array.
Create functions to add items, remove items, and update quantities using array methods.
Print the cart's contents after each operation.
'''


#shopping cart
'''
def shoppingcart_apending(fruitsList:list, item:str):
    fruitsList.append(item)
    return fruitsList



old_list:list = ["apple","banana","orange"]
print(old_list)
new_item:str = "watermelon"
apended_list=shoppingcart_apending(old_list,new_item)    
print(apended_list)
#remove 
def shoppingcart_remove(fruitsList:list, item:str):
    fruitsList.remove(item)
    return fruitsList

remove_item:str = "watermelon"
removed_list=shoppingcart_remove(apended_list,remove_item)    
print(removed_list)'''

3. #*Write a program* that uses a while loop to print the first 25 integer
'''integ:int =1
while integ<=25:
    print(integ)
    integ +=1 '''


#4. *Write a program* that uses a while loop to print the first 10 even numbers.
'''count =0
even_num = 0
while count < 10:
    print(even_num)
    even_num +=2
    count +=1
print(count) ''' 
#6. *Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.
'''number_list: list = [1,2,3,4,5,-7,-3,-8,0.6]
i = 0
while i < len(number_list):
    if number_list[i]<0:
        number_list.pop(i)
    else:
            
        i += 1
print(number_list)  '''


#7. *Create a function* that takes an array of numbers as a parameter.  Use a while loop to calculate and return the sum of all the numbers in the array.
'''
def sum_of_all(number_li:list):
    i : int=  0
    sum : int=0  
    while i <=len(number_li):
        sum += i
        i = i+1
    return sum
num : list= [1,2,3,4]
sum=sum_of_all(num)    
print(sum)'''
    
'''' 8*Implement a program* that takes a list of temperatures in Celsius as input 
from the user. Convert each temperature to Fahrenheit using the
formula F = (C * 9/5) + 32 and store the converted temperatures in an array.
Use a while loop to perform the conversion for each temperature.'''
'''def farn_temp(temp:list):
    templi:list =[] 
    i =0
    while i< len(temp):
        ftemp = (temp[i] * 9/5) + 32
        templi.append(ftemp)
        i= i+1
    return templi

user_temp_cel:int = input("enter tempratrue")
celsius_list = list(map(float, user_temp_cel.split()))
conv_tmp:list = farn_temp(celsius_list)
print(conv_tmp)'''

#9. *Write a program* to remove all the odd numbers from an array.
numbrer_list =[12,14,13,11,4,8,9]
i = 0
while i<len(numbrer_list):
    if numbrer_list[i]%2 !=0:
        numbrer_list.pop(i)
    else:
        i +=1   
print(numbrer_list)         