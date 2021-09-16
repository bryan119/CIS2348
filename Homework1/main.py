#Bryan Nguyen
#1855265
#print's of the birthday calculator
print('Birthday calculator')
print('Current day')
month = int(input('Month: '))
day = int(input('Day: '))
year = int(input('Year: '))
print('Birthday')
m = int(input('Month: '))
d = int(input('Day: '))
y = int(input('Year: '))
#year - y = current age
year_born = year - y
#if the current month and day equals the birthday, then a 'Happy Birthday!' will appear.
if month == m and day == d:
    print('Happy Birthday!')
print('You are', year_born, 'years old.')