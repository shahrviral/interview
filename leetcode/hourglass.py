input = [[1, 1, 1, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0],
         [0, 0, 2, 4, 4, 0],
         [0, 0, 0, 2, 0, 0],
         [0, 0, 1, 2, 4, 0]]

input = [[1, 1, 1, 1],
         [0, 1, 0, 0],
         [1, 1, 1, 0],
         [1, 2, 0, 3]]

print(input)


def hourglass(a):
    num_rows = len(a)
    for i in range(num_rows):
        num_columns = len(a[i])
        for j in range(num_columns):
            if i + 2 < 4 and j + 2 < 4:
                val = sum(
                    [a[i][j], a[i][j + 1], a[i][j + 2], a[i + 1][j + 1], a[i + 2][j], a[i + 2][j + 1], a[i + 2][j + 2]])
                print(val)


hourglass(input)

def calculate_total(i, j, a):
  return a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
