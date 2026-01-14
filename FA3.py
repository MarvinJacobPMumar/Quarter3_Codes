people = ["Me", "Lia", "Jake"]

stepTable = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
    ])

for i, v in enumerate(people):
    total = np.sum(stepTable[i])
    avg = np.mean(stepTable[i])
    minSteps = np.min(stepTable[i])
    maxSteps = np.max(stepTable[i])
    print(f"{v} - Total Steps: {total} | Average: {avg} | Min: {minSteps} | Max: {maxSteps}")
