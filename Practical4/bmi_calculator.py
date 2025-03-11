weight = float (input ("Enter your weight in kg: "))
height = float (input ("Enter your height in meters: "))
bmi = weight / (height ** 2)
print ("Your BMI is: ", bmi)
if bmi < 18.5:
    print ("You are underweight")
elif bmi >= 18.5 and bmi <= 30:
    print ("You are normal weight")
else:
    print ("You are obese")
