#Bryan Nguyen
#1855265
import math
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
print('Wall area:', wall_height * wall_width, 'square feet')

paint_needed = (wall_height * wall_width / 350)

print('Paint needed: {:.2f} gallons'.format(wall_height * wall_width/ 350))
print('Cans needed:', math.ceil(paint_needed), 'can(s)\n')

paint = {'red': 35, 'blue': 75, 'green': 23}
choose_color = input('Choose a color to paint the wall:\n')
print('Cost of purchasing',choose_color, 'paint:', '$' + str(paint[choose_color]))