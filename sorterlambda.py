#def sorter(item):
   # return item['name']

presenters = [
    {'name': 'Venu', 'age': 50},
    {'name': 'Mamatha', 'age': 42}
]

presenters.sort(key=lambda item: item['name'])
print('-- alphabetically --')
print(presenters)

presenters.sort(key=lambda item: len(item['name']))
print('--length--')
print(presenters)




