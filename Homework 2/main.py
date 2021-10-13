#Bryan Nguyen
#1855265

#Part a
#I used def find(): to find the months and convert it into an integer.
def find(datetime):
    months = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9,
              'October':10, 'November':11, 'December':12}

#Month, Day, and Year are converted into integers.
    month = datetime.split()[0].split()[0]
    m1 = months[month]
    day = datetime.split(',')[0].split()[-1]
    year = datetime.split()[-1]
    return format(m1) + str('/') + day + str('/') + year

#Used an if statement to run the code.
if True:
    date = input()
    print(find (date))