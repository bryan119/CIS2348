#Bryan Nguyen
#1855265

passw = input()
fpassw = ''

for i in range(len(passw)):
    if 'i' in passw[i]:
        fpassw += '!'
    elif 'a' in passw[i]:
        fpassw += '@'
    elif 'm' in passw[i]:
        fpassw += 'M'
    elif 'B' in passw[i]:
        fpassw += '8'
    elif 'o' in passw[i]:
        fpassw += '.'
    else:
        fpassw += passw[i]

fpassw += 'q*s'
print(fpassw)