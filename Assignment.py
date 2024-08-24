#BMI
'''user_height = input("enter your height in meter:")
user_weight = input("enter your weight in kilograms:")
BMI = float(user_weight)/(float(user_height)**2)
print("your bmi is " , BMI)

#volume Volume=π×r^2 ×h'''


''''height_cylinder:float = input("enter height of the cylinder:")
radius_cylinder:float = input("enter radius of cylinder:")
pi: float = 3.14159

V = float(pi) * float(radius_cylinder)**2 * float(height_cylinder)
print("volume of cylinder is" , V)'''

#age calculate
'''current_year : int = input("Enter current year:")
birth_year: int = input("Enteryour birth year")

age : int = int(current_year) - int(birth_year)
print("Your age is :"  , age)'''



# Area of a Rectangle: Formula: Area = length × width
'''len : float = float(input("Enter the lenght"))
wid: float = float(input("Enter width"))
area_rect = float(len) * float(wid)
print("The area of rectangle is:" , area_rect)'''


#Area of a Circle: Formula: Area = π × radius²
'''rad_cir = float(input("Enter the radius of circle:"))
Pi = 3.14 
area_circ = Pi*float(rad_cir) **2
print("The area of circle is: ", area_circ)'''


#Surface Area of a Cube: Formula: Surface Area = 6 × side²
'''len_side = float(input("Enter the lenght of side of cube:"))
Surf_area = 6 * float(len_side)**2
print("The area of cube is " , Surf_area)'''


# F to C  Celsius(°C)=5/9×(Fahrenheit(°F)−32)
'''Far_temp = float(input("Enter temprature in Fahrenheit:"))
Cel_temp = 5/9 * (Far_temp-32)
print("tempraure in Celcius is", Cel_temp , "C")'''

# sec to min   min = sec/60

'''time_sec = float(input("enter time in seconds :"))
time_min = time_sec/60
print("time in minutes is ", time_min, "minutes")'''

#min to sec sec = min * 60
'''time_min = float(input("enter time in min :"))
time_sec = time_min*60
print("time in seconds is ", time_sec, "sec")'''

#percentage obt/total * 100
obt_mar = int(input("Enter Obtained marks :"))
ttl_mar = int(input("Enter total marks :"))
perct_mar = obt_mar/ttl_mar * 100
print("Your Percentage is... ", perct_mar, "%")
