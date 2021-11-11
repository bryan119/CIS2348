# Bryan Nguyen
# 1855265

class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = 'none'

    def print_item_cost(self):
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(self.item_price)
              + ' = $' + str(self.item_price * self.item_quantity))

    def print_item_description(self):
        print(self.item_name + ':' + self.item_description)


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


class ShoppingCart:
    def __init__(self):
        self.customer_name = 'none'
        self.current_date = 'January 1, 2016'
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        print('ADD ITEM TO CART')
        name = str(input('Enter the item name:\n'))
        description = str(input('Enter the item description:\n'))
        price = int(input('Enter the item price:\n'))
        quantity = int(input('Enter the item quantity:\n'))
        self.cart_items.append(ItemToPurchase(name, description, price, quantity))

    def remove_item(self, itemname):
        print('REMOVE ITEM FROM CART')
        r = str(input('Enter name of item to remove:\n'))
        remove1 = False
        for item in self.cart_items:
            if (item.item_name == itemname):
                self.cart_items.remove(item)
                remove1 = True
            if not remove1:
                print('Item not found in cart. Nothing modified.')


    def modify_item(self, ItemToPurchase):
        print('CHANGE ITEM QUANTITY')
        name = str(input('Enter the item name:\n'))
        quantity = int(input('Enter the new quantity:\n'))
        modify = False


    def get_num_items_in_cart(self):
        num = 0
        for i in self.cart_items:
            num = i.item_quantity
        return num

    def get_cost_of_cart(self):
        cost = 0
        for i in self.cart_items:
            cost += i.item_quantity & i.item_price
        return cost

    def print_total(self):
        total = self.get_cost_of_cart()
        if total == 0:
            print('SHOPPING CART IS EMPTY')

    def print_descriptions(self):
        print(self.customer_name + 'Shopping Cart -' + self.current_date)
        print('\nItem Descriptions')
        for i in self.cart_items:
            i.print_item_description()