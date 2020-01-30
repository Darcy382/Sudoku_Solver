num_possibilities = [[1, (5, 4)], [2], [3], [4], [5], [6], [7], [8], [9]]

row_num = 5
column_num = 4
num = [1, 4, 6]
for possibility in num_possibilities:
    if possibility[0] in num:
        possibility.append((row_num, column_num))

for num in num_possibilities:
    if len(num) == 3:
        if num[1][0] == num[2][0]:
            print("Row", num)
        elif num[1][1] == num[2][1]:
            print("Column", num)

print(num_possibilities)