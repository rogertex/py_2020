# map

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 4, 9,16,25,36,49,64]


# def square(x):
#     return x*x
# # for x in list_x:
#     print(square(x))


r = map(lambda x,y : x*x+y, list_x,list_y)  #map 左边时函数, 右边时序列 iterable
print(list(r))
