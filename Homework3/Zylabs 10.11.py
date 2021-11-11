#Bryan Nguyen
#1855265

#Created FoodItem class to initiate a constructor
class FoodItem:
    def __init__(self, name = 'None', fat = 0.0, carbs = 0.0, protein = 0.0, servings = 0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.servings = servings

#Parameters to initalize attributes and calculate calories      
    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories
    
#Prints the food item
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':
#User input   
    food_name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    servings = float(input())

    food1 = FoodItem()
    food2 = FoodItem(food_name, fat, carbs, protein)

    food1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings, food1.get_calories(servings)))
    print()

    food2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings, food2.get_calories(servings)))
