# Description: SIR model for the spread of a disease
#import necessary libraries
import matplotlib.pyplot as plt
import numpy as np  
#initializing the variables
N = 10000                 
S = N - 1                 
I = 1                    
R = 0                     
beta = 0.3                
gamma = 0.05    
timesteps = 1000        
#creating arrays to store the values of S, I, R
S_array = [S]             
I_array = [I]             
R_array = [R]          
#looping through the timesteps      
for _ in range(timesteps):
    S_prev, I_prev, R_prev = S_array[-1], I_array[-1], R_array[-1]
    #calculating the probability of infection
    p_infection = beta * I_prev / N
    #calculating the number of people who got infected
    delta_S_to_I = np.random.binomial(S_prev, p_infection)
    #calculating the number of people who recovered
    delta_I_to_R = np.random.binomial(I_prev, gamma)
    #updating the values of S, I, R
    S_new = S_prev - delta_S_to_I
    I_new = I_prev + delta_S_to_I - delta_I_to_R
    R_new = R_prev + delta_I_to_R
    #checking if the sum of S, I, R is constant
    assert S_new + I_new + R_new == N, 'The sum of S, I, R should be a constant'
    #appending the new values to the arrays
    S_array.append(S_new)
    I_array.append(I_new)
    R_array.append(R_new)
#plotting the graph
plt.figure(figsize =(6,4),dpi=150)
plt.plot(S_array, label='Susceptible', color='blue')
plt.plot(I_array, label='Infected', color='red')
plt.plot(R_array, label='Recovered', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('SIR Model Simulation')
plt.legend()
plt.show()
plt . figure ( figsize =(6,4),dpi=150)
plt.savefig('SIR_figure.png', format='png')