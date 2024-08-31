'''def percentage(obt:int , ttl:int):
    perc = obt/ttl *100
    print(perc)
    print(type(perc))
ob = int(input("Enter marks"))
tt = int(input("Enter total marks"))
percentage(ob,tt)'''


# min to sec sec = min * 60
'''def mintosec(min:int):
    sec = min * 60
    print(sec)
user_min = int(input("Enter seconds:"))
mintosec(user_min)'''


# F to C  Celsius(°C)=5/9×(Fahrenheit(°F)−32)
'''def farntocel(temp:int):
    temp_cel = 5/9 *(temp-32)
    print(temp_cel)
user_tempv=int(input("Enter temprature in Farnhite"))
farntocel(user_tempv)'''


#Surface Area of a Cube: Formula: Surface Area = 6 × side²
'''def areaofcube(lenOfSide:float):
    areaofcube = 6 * lenOfSide**2
    print(areaofcube) 
user_lenside = float(input("Enter the lenght of side"))
areaofcube(user_lenside)'''

#Area of a Circle: Formula: Area = π × radius²
'''def areaofcircle(radcircle:float):
    pi:float =3.14
    area_circ : float = pi * radcircle**2
    print(area_circ)
user_rad = float(input("Enter the radius of circle"))
areaofcircle(user_rad)'''


# Area of a Rectangle: Formula: Area = length × width
'''def rect(lenght:float, width:float):
    area = lenght * width
    print(area)
user_len =float(input("Enter lenght"))
user_wid= float(input("Enter width"))
rect(user_len,user_wid)'''


#volume Volume=π×r^2 ×h'''
'''def volume(rad:float, hei:float):
    pi =3.14
    vol = pi * rad**2 *hei
    print(vol)
user_rad = float(input("Enter radius:"))
user_heigh = float(input("Enter height"))
volume(user_rad, user_heigh)'''

#BMI weight/height**2
def BMI(weig:float, heig:float):
    bmi = weig/heig**2
    print(bmi)
user_w =float(input("Enter weight"))
user_h= float(input("Enter height"))
BMI(user_w, user_h)    
