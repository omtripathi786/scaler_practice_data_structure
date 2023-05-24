arr_list = [2,11,15,7]
target = 9


for i in len(arr_list):
    temp = target - arr_list[i]
    if temp in arr_list and temp != arr_list[i]:
        print(i, )







