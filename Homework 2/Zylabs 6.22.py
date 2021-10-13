#Bryan Nguyen
#1855265

x = int(input())
y = int(input())
z = int(input())

x1 = int(input())
y1 = int(input())
z1 = int(input())
solution = False

for x2 in range (-10, 10):
    for y2 in range (-10, 10):
        if (x * x2 + y * y2 == z) and (x1 * x2 + y1 * y2 == z1):
            print(x2, y2)
            solution = True

if not solution:
    print('No solution')