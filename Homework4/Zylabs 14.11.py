# Bryan Nguyen
# 1855265
#Used Lab 14.10 as reference
def selection_sort_descend_trace(integer):
    for i in range(len(integer) - 1):
        list = i
        for y in range(i + 1, len(integer)):
            if integer[list] < integer[y]:
                list = y
        integer[i], integer[list] = integer[list], integer[i]
        print(' '.join([str(x) for x in integer]) + ' ')

if __name__ == '__main__':
    integer_list = [int(sort) for sort in input().split()]
    selection_sort_descend_trace(integer_list)
