# -*- coding: utf-8 -*-


def bubble_sort(numbers):
    new_list = list(numbers)
    for _ in new_list:
        for idx, num in enumerate(new_list):
            if idx == len(new_list)-1:  # if last element, do nothing
                pass
            elif num > new_list[idx+1]:  # exchange if higher value than next
                new_list.insert(idx+1, new_list.pop(idx))
    return new_list


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1),):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
