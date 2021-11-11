#Bryan Nguyen
#1855265

class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(self.item_price)
              + ' = $' + str(self.item_price * self.item_quantity))

if __name__ == '__main__':
    print('Item 1')

    itp1 = ItemToPurchase()
    itp2 = ItemToPurchase()

    name = input('Enter the item name:\n', )
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    itp1.item_name = name
    itp1.item_price = price
    itp1.item_quantity = quantity

    print('\nItem 2')
    name1 = input('Enter the item name:\n')
    price1 = int(input('Enter the item price:\n'))
    quantity1 = int(input('Enter the item quantity:\n'))
    itp2.item_name = name1
    itp2.item_price = price1
    itp2.item_quantity = quantity1

    print('\nTOTAL COST')
    itp1.print_item_cost()
    itp2.print_item_cost()
    total = (itp1.item_price * itp1.item_quantity) + (itp2.item_price * itp2.item_quantity)

    print('\nTotal: $' + str(total))