list1 = ['Blessing', 'Abode', 'Ige']
list2 = ['Blessing', 'Ige', 'Abode']

# order = {v:i for i,v in enumerate(list1)}
c = sorted(list2, key = lambda e: list1[e])

print(c)
