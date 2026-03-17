from music import play_array, find_max
import random

def merge(arr_1: list[int], arr_2: list[int]) -> list[int]:
    size1 = len(arr_1)
    size2 = len(arr_2)
    size3 = size1 + size2


    result = [0] * size3

    point1 = 0
    point2 = 0
    point3 = 0

    while point1 < size1 and point2 < size2:
        if arr_1[point1] < arr_2[point2]:
            result[point3] = arr_1[point1]
            point1 += 1
        else:
            result[point3] = arr_2[point2]
            point2 += 1
        point3 += 1


    while point1 < size1:
        result[point3] = arr_1[point1]
        point1 += 1
        point3 += 1

    while point2 < size2:
        result[point3] = arr_2[point2]
        point2 += 1
        point3 += 1


    return result



def msort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr

    half = int(len(arr) / 2)

    segment1 = msort(arr[:half])
    segment2 = msort(arr[half:])

    play_array(segment1)
    play_array(segment2)

    return merge(segment1, segment2)

test = []


for i in range(10):
    test.append(random.randint(1, 100))
    
find_max(test)
play_array(msort(test))
