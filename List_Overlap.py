list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

unique_list1 = set(list1)
unique_list2 = set(list2)

diff_element = unique_list2 - unique_list1

output = list1 + list(diff_element)

def remove(output):
    final_list = []
    for num in output:
        if num not in final_list:
            final_list.append(num)
            final_list.sort()
    return final_list


print(remove(output))






