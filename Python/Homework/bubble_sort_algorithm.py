# Bubble Sort Algorithm Implementation
my_list = [3, 5, 7, 2, 34, 8, 90, 0, -2, 78]


def bubble_sort(ls):
    k = 1
    while k != len(ls) - 1:
        for i in range(len(ls)-k):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
        k += 1
    return ls

print(bubble_sort(my_list))
