my_list = [100, 106, 3, 5, 7, 2, 34, 83, 8, 90, 0, -2, 78]

def quick_sort_algorithm(ls):
    less = []
    equal = []
    grater = []
    l = len(ls)
    if l > 1:
        pivot = ls[0]
        for i in ls[0:l]:
            if i > pivot:
                grater.append(i)
            elif i == pivot:
                equal.append(i)
            elif i < pivot:
                less.append(i)
        res = quick_sort_algorithm(less) + equal + quick_sort_algorithm(grater)
        return res
    else:
        return ls

print(quick_sort_algorithm(my_list))