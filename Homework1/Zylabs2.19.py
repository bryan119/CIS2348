#Bryan Nguyen
#1855265
lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = int(input('How many servings does this make?\n'))

print()
print('Lemonade ingredients - yields {:.2f} servings' .format(servings))
print('{:.2f} cup(s) lemon juice' .format(lemon_juice))
print('{:.2f} cup(s) water' .format(water))
print('{:.2f} cup(s) agave nectar' .format(agave_nectar))
print()

many_servings = int(input('How many servings would you like to make?\n'))
lj = (lemon_juice / 6 * many_servings)
w = (water / 6 * many_servings)
an = (agave_nectar / 6 * many_servings)
print()
print('Lemonade ingredients - yields {:.2f} servings' .format(many_servings))
print('{:.2f} cup(s) lemon juice' .format(lj))
print('{:.2f} cup(s) water' .format(w))
print('{:.2f} cup(s) agave nectar\n' .format(an))

gallon_size = 2
gallon_lemon = lemon_juice / lemon_juice
gallon_water = water / gallon_size
gallon_agave = agave_nectar / gallon_size

print('Lemonade ingredients - yields {:.2f} servings' .format(many_servings))
print('{:.2f} gallon(s) lemon juice' .format(gallon_lemon))
print('{:.2f} gallon(s) water' .format(gallon_water))
print('{:.2f} gallon(s) agave nectar' .format(gallon_agave))