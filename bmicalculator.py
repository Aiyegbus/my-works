# BMI Calculator


name = input("Enter your name:")
height = float(input ("Enter your Height in meters:"))
age = int(input("Enter your age:"))
weight=int(input('enter your weight in kg'))

def bmi_calc_auto(name, height, weight, age):
    bmi_auto = round(float(weight)/ (height ** 2))
    if bmi_auto < 18.5:
        print(name + " is underweight, and is " + str(age) + " years old.")
    elif 18.5 >= bmi_auto <= 24.9:
        print(name + " is normal and healthy, and is " + str(age) + " years old.")
    elif 25 >= bmi_auto <= 29.9:
        print(name + " is overweight, and is " + str(age) + " years old.")
    else:
        print(name +" is obese, and is " + str(age) + " years old." )

result = bmi_calc_auto(name, height, weight, age)
print(result)