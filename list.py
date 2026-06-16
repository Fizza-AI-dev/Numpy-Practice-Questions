temperatures=[32.5,56.8,45.4,56.7]
total=0

for i in temperatures:
    total=total+i

average=total/len(temperatures)
print(average)