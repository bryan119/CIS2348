# Bryan Nguyen
# 1855265

import csv
from operator import itemgetter

#Creating List
electronic_list = []

#Opening file and adding to electronic_list
with open('ManufacturerList.csv', 'r') as mlist:
    manufacturer = csv.reader(mlist)
    for i in manufacturer:
        electronic_list.append(i)

#Appending PriceList and ServiceDatesList to continue the loop
with open('PriceList(1).csv', 'r') as plist:
    price = csv.reader(plist)
    for i in price:
        for x in range(len(electronic_list)):
            if electronic_list[x][0] == i[0]:
                electronic_list[x].append(i[1])
            continue

with open('ServiceDatesList.csv', 'r') as slist:
    service = csv.reader(slist)
    for i in service:
        for x in range(len(electronic_list)):
            if electronic_list[x][0] == i[0]:
                electronic_list[x].append(i[1])
            continue


#Sorting the contents
updated_electronic = sorted(electronic_list, key = itemgetter(1))
fi = []

#Writing the FullInventory file and CORRECTING THE SORTING FROM PART 1
with open('FullInventory.csv', 'w', newline='') as ffile:
    fwrite = csv.writer(ffile)
    for x in range(len(updated_electronic)):
        fi.append([updated_electronic[x][0], updated_electronic[x][1], updated_electronic[x][2], updated_electronic[x][4],
                   updated_electronic[x][5], updated_electronic[x][3]])
    fwrite.writerows(fi)

#Creating lists for item type
laptop_Inventory = []
tower_inventory = []
phone_inventory = []

updated_laptop_inventory = sorted(laptop_Inventory, key = itemgetter(1))
updated_tower_inventory = sorted(tower_inventory, key = itemgetter(1))
updated_phone_inventory = sorted(phone_inventory, key = itemgetter(1))

#Sorting and Writing the item list content
with open('LaptopInventory.csv', 'w', newline= '') as laptop:
    lwrite = csv.writer(laptop)
    for x in range(len(fi)):
        if fi[x][2] == 'laptop':
            updated_laptop_inventory.append([fi[x][0], fi[x][1], fi[x][3], fi[x][4], fi[x][5]])
    lwrite.writerows(updated_laptop_inventory)

with open('TowerInventory.csv', 'w', newline= '') as tower:
    lwrite = csv.writer(tower)
    for x in range(len(fi)):
        if fi[x][2] == 'tower':
            updated_tower_inventory.append([fi[x][0], fi[x][1], fi[x][3], fi[x][4], fi[x][5]])
    lwrite.writerows(updated_tower_inventory)

with open('PowerInventory.csv', 'w', newline= '') as phone:
    lwrite = csv.writer(phone)
    for x in range(len(fi)):
        if fi[x][2] == 'phone':
            updated_phone_inventory.append([fi[x][0], fi[x][1], fi[x][3], fi[x][4], fi[x][5]])
    lwrite.writerows(updated_phone_inventory)

#Creating a list for PastServiceDateInventory
psd = []

with open('PastServiceDateInventory.csv', 'w', newline= '') as psdfile:
    p = csv.writer(psdfile)
    p.writerows(psd)

#Creating a list for DamagedInvetory
dlist = []
updated_dlist = sorted(dlist, key = itemgetter(1))

#Writing DamagedInventory file
with open('DamagedInventory.csv', 'w', newline= '') as dfile:
    p = csv.writer(dfile)
    for x in range(len(fi)):
        if fi[x][5] == 'damaged':
            updated_dlist.append([fi[x][0], fi[x][1], fi[x][2], fi[x][3], fi[x][4]])
    p.writerows(updated_dlist)

#FINAL PROJECT PART 2 HERE
#Ask user for manufacturer and item type
product = []
manu = str(input('Enter the manufacturer name or enter "q" to exit: '))
item = str(input('Enter the item name or enter "q" to exit: '))

#Creating an exit value using 'q'
while manu and item != 'q':
    if manu and item == 'q':
        break
    else:
#manu will display the manufacturer column and item will display the item type from the
#FullInventory.csv file.
        for x in range(len(fi)):
            if manu in fi[x][1] and item in fi[x][2]:
                product.append(fi[x])

#Product variable will display the item ID, manufacturer, item type, price, and service date.
#If the input does not match the content in the FullInventory.csv file,
        # then 'No such item in inventory; will be outputed.
        if len(product) != 0:
            product = sorted(product, key=itemgetter(1), reverse = True)
            print('Your item is: ', product[0])
        else:
            print('No such item in inventory')

#Using Item Type column [2] from the FullInventory.csv file to recommend other products.
        if item in fi[x][2]:
            product.append(fi[x])
            print('You may, also, consider:', product[1])

        manu = str(input('Enter the manufacturer name or enter "q" to exit: '))
        item = str(input('Enter the item name or enter "q" to exit: '))
