#importing the required libraries
import numpy as np
import matplotlib.pyplot as plt
def SIR_vaccination(vaccinated_ratio, N=10000, beta=0.3, gamma=0.05, days=1000):
#   initializing the variables
    V = int(N * vaccinated_ratio)
    I, R = 1, 0
    S = max(0, N - I - V)
#   creating arrays to store the values of S, I, R
    S_hist, I_hist, R_hist = [S], [I], [R]
    effective_S = max(0, S_hist[-1])
    p_infection = beta * I_hist[-1] / N
    for _ in range(days):
     #calculate the probability of infection
        p_infection = beta * I_hist[-1] / N
        new_infected = np.random.binomial(S_hist[-1], beta * I_hist[-1]/N)
        new_recovered = np.random.binomial(I_hist[-1], gamma)
 
        S_new = S_hist[-1] - new_infected
        I_new = I_hist[-1] + new_infected - new_recovered
        R_new = R_hist[-1] + new_recovered + V  
        
        S_hist.append(S_new)
        I_hist.append(I_new)
        R_hist.append(R_new)
    
    return I_hist 

#plotting the graph under different vaccination circumstances
ratios = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
results = {f"{int(r*100)}%": SIR_vaccination(r) for r in ratios}

plt.figure(figsize=(10, 6))
for label, data in results.items():
    plt.plot(data, label=label, linewidth=2)

plt.title("SR Model with Varied Vaccination")
plt.xlabel("time")
plt.ylabel("infected population")
plt.legend()
plt.grid(alpha=0.3)
plt.show()