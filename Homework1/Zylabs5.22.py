#Bryan Nguyen
#1855265
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
service = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}
print()
first_service = input('Select first service:\n')
second_service = input('Select second service:\n')

print()
print("Davy's auto shop invoice")
print()
if (first_service == '-'):
    print('Service 1: No service')
else:
    print('Service 1:', first_service + str(','), '$' + str(service[first_service]))
if (second_service == '-'):
    print('Service 2: No service')
else:
    print('Service 2:', second_service + str(','), '$' + str(service[second_service]))
print()
invoice = service.get(first_service) + service.get(second_service)
print('Total:','$' + str(invoice))