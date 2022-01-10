import random
"""
это простая сортировка пузырьком. Сделана для теста собственных сил
"""

n = 10
a = []
for i in range(n):
    a.append(random.randint(1, 99))
print(a)

def bubble_sort(array):
    for i in range(n-1):
        for b in range(n-i-1):
            if array[b] > array[b+1]:
                array[b], array[b+1] = array[b+1], array[b]

bubble_sort(a)
print(a)