import list_1_100

sorted_list = []

for x in range(len(list_1_100.random_number_list)):
       for i in range(x+1, len(list_1_100.random_number_list)):
           if list_1_100.random_number_list[x] > list_1_100.random_number_list[i]:
               list_1_100.random_number_list[x], list_1_100.random_number_list[i] = list_1_100.random_number_list[i], list_1_100.random_number_list[x]
print(list_1_100.random_number_list)
    