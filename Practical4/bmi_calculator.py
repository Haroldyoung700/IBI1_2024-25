weight = float (input ("Enter your weight in kg: "))      #Get weight from user
height = float (input ("Enter your height in meters: "))  #Get height from user
bmi = weight / (height ** 2)                              #Calculate BMI
print ("Your BMI is: ", bmi)                              #Print BMI
if bmi < 18.5:
    print ("You are underweight")
elif bmi >= 18.5 and bmi <= 30:
    print ("You are normal weight")
else:
    print ("You are obese")                               #Print the BMi condition