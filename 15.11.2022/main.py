import random

length = int(input('length of lists ->'))

rand_list1 = []
rand_list2 = []

for i in range(length):
    rand_list1.append(random.randint(1, 10))
for e in range(length):
    rand_list2.append(random.randint(1, 10))
print(f'list1 -> {rand_list1}')
print(f'list2 -> {rand_list2}')
mylist = rand_list1 + rand_list2
print(f'all elements -> {mylist}')

new_list1 = list(set(rand_list1) | set(rand_list2))
print(f'duplicates removed -> {new_list1}')

new_list2 = []
for element in rand_list1:
    if element in rand_list2:
        new_list2.append(element)
print(f'only common elements -> {new_list2}')

new_list3 = []
new_list4 = []
for element in rand_list1:
    if element not in rand_list2:
        new_list3.append(element)
print(f'unique numbers for first list -> {new_list3}')

for element in rand_list2:
    if element not in rand_list1:
        new_list4.append(element)
print(f'unique numbers for second list-> {new_list4}')

print(f'minimum and maximum values in first list -> {min(rand_list1), max(rand_list1)}')
print(f'minimum and maximum values in second list -> {min(rand_list2), max(rand_list2)}')

