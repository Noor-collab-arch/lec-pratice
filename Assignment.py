#BMI
user_height = input("enter your height in meter:")
user_weight = input("enter your weight in kilograms:")
BMI = float(user_weight)/(float(user_height)**2)
print("your bmi is " , BMI)

#volume Volume=π×r^2 ×h


height_cylinder:float = input("enter height of the cylinder:")
radius_cylinder:float = input("enter radius of cylinder:")
pi: float = 3.14159

V = float(pi) * float(radius_cylinder)**2 * float(height_cylinder)
print("volume of cylinder is" , V)