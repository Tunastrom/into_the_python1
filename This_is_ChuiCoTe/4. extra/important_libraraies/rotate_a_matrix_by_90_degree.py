def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res

def rotate_a_matrix_by_90_degree_reverse(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[column_length - 1 - c][r]= a[r][c]

    return res

def display(a):
    print('[', end='\n')
    for i in range(len(a)):
        print(f' {a[i]}', end=',\n')
    print(']', end='\n')

test_list = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11]
]

display(rotate_a_matrix_by_90_degree(test_list))
display(rotate_a_matrix_by_90_degree_reverse(test_list))