import numpy as np
import matplotlib.pyplot as plt

# Initialize parameters
beta = 0.3         # probability of infection
gamma = 0.05       # infection recovery rate
days = 30          # total simulation days

# population grid
population = np.zeros((100, 100), dtype=int)

# outbreak location
outbreak = np.random.randint(0, 100, size=(1, 2))  # 
x, y = outbreak[0]
population[x, y] = 1

# plot the initial state
plt.figure(figsize=(6, 4), dpi=150)
img = plt.imshow(population, cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
plt.colorbar(ticks=[0, 1, 2], label='status: 0=susceptible, 1=infectee, 2=recoverer')
plt.title("Day 0")

# Run the simulation
for day in range(1, days+1):
    # copy the population grid
    new_pop = population.copy()
    
    # Loop through each cell in the grid
    for i in range(100):
        for j in range(100):
            if population[i, j] == 1:
                # decide if the infectee recovers
                if np.random.rand() < gamma:
                    new_pop[i, j] = 2
                # infect the susceptible neighbors
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= i+dx < 100 and 0 <= j+dy < 100:
                            if population[i+dx, j+dy] == 0 and np.random.rand() < beta:
                                new_pop[i+dx, j+dy] = 1
    # update the population grid
    population = new_pop
    # update the plot
    img.set_data(population)
    plt.title(f"Day {day}")
    plt.pause(0.2)  # pause for 0.2 seconds