import numpy as np
    
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
totals = []
stepTablePeople = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
    ])

# Uses a special function in Numpy to turn columns into rows
stepTableDays = np.flip(np.rot90(stepTablePeople), axis = 0)

for i, v in enumerate(days):
    print(f"{v} total : {np.sum(stepTableDays[i])}")
    totals.append(sum(stepTableDays[i]))
    
mostActiveDay = days[totals.index(max(totals))]

print(f"\nThe most active day is {mostActiveDay}, with the total steps of {max(totals)}.")
