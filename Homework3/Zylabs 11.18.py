#Bryan Nguyen
#1855265

numbers = input().split()
my_list = []

for i in numbers:
    if int(i) >= 0:
        my_list.append(int(i))
my_list.sort()

for y in my_list:
    print(y, end=' ')
