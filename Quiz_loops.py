# WAP to find minimum and maximum element from a list without using min() and max () using loops 

# Program to find max & min item in a list

ls = [10,1,0,10,10,20,30,40,40,50,60,70,80,80,90]

max = ls[0]
min = ls[0]
for i in ls :
    if i<=min :
        min = i
    if i>=max :
        max = i
    
print('max item:', max, 'present at index:', ls.index(max))
print('min item:', min, 'present at index:', ls.index(min))




# *
# **
# ***
# ****
# *****
# ******

for i in range(7):
    print("*"*i)

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4

n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
