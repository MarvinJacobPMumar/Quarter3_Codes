import numpy as np
    
people = ["Me", "Lia", "Jake"]

stepTable = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
    ])
print("      MON  TUE  WED  THU  FRI")
for i, v in enumerate(people):
    print(f"{v} : {stepTable[i]}")
