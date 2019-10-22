lst = [1, 3, 0, 2, 6, 4, 5]


def insertion_sort(unsorted_lst):
    for i in range(1, len(unsorted_lst)):
        j = i
        while j > 0 and unsorted_lst[j] < unsorted_lst[j - 1]:
            unsorted_lst[j], unsorted_lst[j - 1] = unsorted_lst[j - 1], unsorted_lst[j]
            j -= 1
    return unsorted_lst


print(insertion_sort(lst))
