def snail(array):
    dimension = len(array[0])

    if dimension % 2 == 0:
        i = int(dimension / 2)
        jj = i - 1
    else:
        i = dimension // 2
        jj = dimension // 2

 ###################################  while  ##################################   
    clock_wise = []
    count_movement = 1
    start = 0
    end = 0
    first_time = True
    first_corner = 0
    first_up = 0
    while True:
###############################################################################
        if count_movement == 1:
            clock_wise.append(array[start][end])

            if dimension - 1 == end:
                count_movement = 2

                if start == i and end == jj:
                    break
            end += 1
###############################################################################
        if count_movement == 2:
            if first_time:
                start = start + 1
                end = end - 1
                first_time = False

            clock_wise.append(array[start][end])

            if start == dimension - 1:
                count_movement = 3
                first_time = True

                if start == i and end == jj:
                    break
            start += 1
###############################################################################
        if count_movement == 3:
            if first_time:
                start = start - 1
                first_time = False

            end -= 1
            clock_wise.append(array[start][end])

            if end == first_corner:
                first_corner += 1
                count_movement = 4
                first_time = True

                if start == i and end == jj:
                    break
###############################################################################

        if count_movement == 4:
            if first_time:
                start = start - 1
                first_time = False

            clock_wise.append(array[start][end])
            start -= 1

            if start == i and end == jj:
                break
            if start == first_up:
                first_up += 1
                count_movement = 1
                end += 1
                start += 1
                dimension -= 1
                first_time = True
    return clock_wise

def snail2(array):
    out = []
    # import pdb; pdb.set_trace()
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out
# lista = [[1, 2, 3, 4],
#          [12, 13, 14, 5],
#          [11, 16, 15, 6],
#          [10, 9, 8, 7]]

# lista = [[1,2,3,4,5],
#          [16,17,18,19,6],
#          [15,24,25,20,7],
#          [14,23,22,21,8],
#          [13,12,11,10,9]]

lista = [[1,2,3,4,5,6],
         [20,21,22,23,24,7],
         [19,32,33,34,25,8],
         [18,31,36,35,26,9],
         [17,30,29,28,27,10],
         [16,15,14,13,12,11]]
         
# snail(lista)
print(snail2(lista))
