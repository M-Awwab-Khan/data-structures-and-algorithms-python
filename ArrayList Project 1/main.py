import numpy as np

n = int(input('How many day\'s temperature? '))

temps = np.zeros(n)
for i in range(n):
    print(f"Day {i+1}'s high temperature: ", end='')
    temps[i] = float(input())

average = temps.mean()
above_average = (temps > temps.mean()).sum()
print(f"Average: {average}")
print(f"{above_average} day(s) above average.")
