doors = [False] * 100
[print(item) for item in [f'Door {x+1} is closed' for x in range(0,100)]]
for x in range(1,101): 
    for i in range(x-1,100,x): doors[i] = not doors[i]
[print(item) for item in [f'Door {x+1} is {'open' if doors[x] else 'closed'}' for x in range(0,100)]]





"""
for x in range(0,len(doors)):
    if doors[x]:
        doors[x] = f'Door {x+1} is open'
    else:
        doors[x] = f"Door {x+1} is closed"
"""
