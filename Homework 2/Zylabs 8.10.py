#Bryan Nguyen
#1855265
name = input()
forward = ""
reverse = ""

for i in range(len(name)):
   if name[i].islower():
       forward += name[i]
       reverse = name[i] + reverse

if forward == reverse:
   print(name, 'is a palindrome')
else:
   print(name, 'is not a palindrome')