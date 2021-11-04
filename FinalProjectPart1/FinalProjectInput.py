#Bryan Nguyen
#1855265

import csv
from operator import itemgetter

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

#Sorting the data alphabetically
new_list = sorted(electronic_list, key=itemgetter(1))
complete_list = new_list

#Writing to FullInventory file
with open('FullInventory.csv', 'w', newline='') as ffile:
    fwrite = csv.writer(ffile)
    fwrite.writerows(complete_list)

#Creating lists for Item Type
items = complete_list
#Phone List
Plist = []
for x in range(len(items)):
    if items[x][2] == 'phone':
        Plist.append(items)

#Laptop List
Llist = []
for x in range(len(items)):
    if items[x][2] == 'laptop':
        Llist.append(items)

#Tower List
Tlist = []
for x in range(len(items)):
    if items[x][2] == 'tower':
        Tlist.append(items)

#Writing to LaptopInventory file
with open('LaptopInventory.csv', 'w') as laptop:
    Lfile = csv.writer(laptop)
    Lfile.writerows(Llist)

#Writing to PhoneInvetory file
with open('PhoneInventory.csv', 'w') as phone:
    Pfile = csv.writer(phone)
    Pfile.writerows(Plist)

#Writing to TowerInventory file
with open('TowerInventory.csv', 'w') as tower:
    Tfile = csv.writer(tower)
    Tfile.writerows(Tlist)

#Creating PastServiceDateInventory file
psd = []

with open('PastServiceDateInventory.csv', 'w') as psdfile:
    p = csv.writer(psdfile)
    p.writerows(psd)

#Damaged List
dlist = []
for x in range(len(items)):
    if items[x][3] == 'damaged':
        dlist.append(items)

#Writing a DamagedList file
with open('DamagedInventory.csv', 'w') as dfile:
    dwrite = csv.writer(dfile)
    dwrite.writerows(dlist)

