dList = ['A', 'B', 'C', 'D']

for i in range(0,len(dList)):
    try: dList[i+1]
    except: print(f"You're a run {dList[i]}")
