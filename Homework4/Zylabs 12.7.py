# Bryan Nguyen
# 1855265
#Used Lab 12.6 as reference.
def get_age():
    age = int(input())
    if 18 <= age <= 75:
        return age
    raise ValueError ('Invalid age.')

def fat_burning_heart_rate(age):
    return 0.70 * (220 - age)

if __name__ == '__main__':
    try:
        age = get_age()
        print('Fat burning heart rate for a', age, 'year-old:', fat_burning_heart_rate(age), 'bpm')
    except ValueError as x:
        print(x)
        print('Could not calculate heart rate info.')
        print()
