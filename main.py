roy = [8, 11, 6, 4, 1, 20, 33, 19, 44]
print(roy)

roy2 = list(filter(lambda el: el % 2 == 0, roy))
print(roy2)

mevalar = ['olma', 'anjir', 'uzum', 'nok', 'ananas']
print(mevalar)

roy2 = list(filter(lambda el: len(el) > 4, mevalar))
print(roy2)

names = ['Abdulla', 'Tom', 'Alex', 'Ali', 'Bob', 'Sam', 'Jack', 'Aziza']
print(names)
roy = list(filter(lambda el: el[0] != 'A', names))
