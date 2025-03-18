sum = 0                                         #Initialize the sum of the series
for a in range (1,11):                          
    sum = 0.5*a*(a+1)                           #Calculate the sum of the series,using formula
    print(sum)                                  #Print the sum of the series
#This one is for 10 rows

a = int(input("Enter the number of rows: "))    #Get the number of rows from user
sum = 0                                         #Initialize the sum of the series
for i in range(1, a+1):                         #Iterate through the number of rows
    sum = 0.5 * i * (i + 1)                     #Calculate the sum of the series,using formula
    print(sum)                                  #Print the sum of the series
#This one is for unlimited number of rows
    