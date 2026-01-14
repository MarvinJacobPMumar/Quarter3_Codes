import numpy as np
    
people = ["Me", "Lia", "Jake"]
totals = []
stepTable = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
    ])

for a in stepTable:
    totals.append(np.sum(a))

print(f"The person with the highest total steps is {people[totals.index(max(totals))]} with {max(totals)} steps. The difference between the steps of the people with the highest and lowest total is {max(totals)-min(totals)}.")
