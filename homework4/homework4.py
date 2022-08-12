

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =69

def search_in_matrix(matrix, target):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if (matrix[y][x]) == target:
                return [y,x]
    return [-1,-1]

print(search_in_matrix(matrix,target))