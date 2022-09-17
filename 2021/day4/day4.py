my_file = open("input.txt", "r")
bingo_list = list(map(lambda x: int(x), my_file.readline().strip().split(",")))

print(bingo_list)
# space = my_file.readline()
# l = filter(lambda x: x != '', my_file.read().split("\n"))
# x = map(lambda x: x.split(), l)
# bingos = []
# length = len(x)

# for i in range(length / 5):
#     b = []
#     for j in range(i * 5, (5 * i) + 5):
#         b.append(x[j])
#     bingos.append(b)

# bingos = [[[int(k) for k in j] for j in i] for i in bingos]
# def check_column(arr):
#     for i in range(5):
#         x = []
#         for j in range(5):
#             x.append(arr[j][i])
#             if (x == [1, 1, 1, 1, 1]):
#                 return True
#     return False


# def check_row(arr):
#     for row in arr:
#         if (row == [1, 1, 1, 1, 1]):
#             return True

# def list_elements_same(lst):
#     if (lst is None or len(lst) == 1):
#         return True
#     else:
#         return lst[0] == lst[1] and list_elements_same(lst[1:])

# def find(arr, x):
#     for row in range(5):
#         for col in range(5):
#             if arr[row][col] == x:
#                 return [row, col]

# def bingo(arr):
#     counter = 0
#     M = [[0] * 5 for _ in range(5)]
#     for num in bingo_list:
#         if check_column(M) != True and check_row(M) != True:
#             position = find(arr, num)
#             if position != None:
#                 M[position[0]][position[1]] = 1
#                 counter += 1
#             else:
#                 counter += 1
#         else:
#             return [counter, M]

# result = map(lambda x: bingo(x)[0], bingos)
# max_value = max(result)
# max_index = result.index(max_value)
# called_num = bingo_list[max_value - 1]
# max_arr = bingos[max_index]
# final_M = bingo(bingos[max_index])[1]
# sum = 0
# for i in range(5):
#     for j in range(5):
#         if (final_M[i][j] == 0):
#             sum += max_arr[i][j]

# print(sum * called_num)

# # min_value = min(result)
# # min_index = result.index(min_value)
# # called_num = bingo_list[min_value - 1]
# #
# # min_arr = bingos[min_index]
# # final_M = bingo(bingos[min_index])[1]
# # sum = 0
# # for i in range(5):
# #     for j in range(5):
# #         if (final_M[i][j] == 0):
# #             sum += min_arr[i][j]
# #
# # print(sum * called_num)
# #
# #
